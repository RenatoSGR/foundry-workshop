#!/usr/bin/env python3
"""
🔧 Script de Setup do Workshop Azure AI Foundry
================================================
Este script extrai automaticamente as configurações do teu projeto
Azure AI Foundry e popula o ficheiro .env.

Pré-requisitos:
  - Azure CLI instalado e autenticado (az login)
  - Projeto Azure AI Foundry já criado

Uso:
  python setup_env.py
"""

import subprocess
import json
import sys
import os


def run_az(cmd: str) -> dict | list | str:
    """Executa um comando az CLI e retorna o resultado."""
    result = subprocess.run(
        f"az {cmd} --output json",
        shell=True,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Erro ao executar 'az {cmd}':\n{result.stderr}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return result.stdout.strip()


def is_az_available() -> bool:
    """Verifica se a Azure CLI está instalada."""
    try:
        subprocess.run(
            "az version --output json",
            shell=True, capture_output=True, text=True, timeout=10,
        )
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def check_az_login():
    """Verifica se o utilizador está autenticado no Azure CLI."""
    try:
        account = run_az("account show")
        print(f"✅ Autenticado como: {account.get('user', {}).get('name', 'N/A')}")
        print(f"   Subscrição: {account.get('name', 'N/A')} ({account.get('id', 'N/A')})")
        return account
    except RuntimeError:
        print("❌ Não estás autenticado no Azure CLI.")
        print("   Executa: az login")
        return None


def list_foundry_projects():
    """Lista projetos AI Foundry disponíveis."""
    print("\n🔍 A procurar projetos AI Foundry...")
    try:
        # Procurar recursos do tipo AI Services / AI Project
        resources = run_az(
            "resource list --resource-type Microsoft.MachineLearningServices/workspaces "
            "--query \"[?kind=='Project' || kind=='Hub']\" "
        )
        if not resources:
            # Fallback: procurar por AI Services
            resources = run_az(
                "resource list --resource-type Microsoft.CognitiveServices/accounts"
            )
        return resources
    except RuntimeError as e:
        print(f"⚠️ Erro ao listar projetos: {e}")
        return []


def get_foundry_details(resource_group: str, project_name: str):
    """Obtém detalhes do projeto Foundry."""
    try:
        details = run_az(
            f"ml workspace show --name {project_name} --resource-group {resource_group}"
        )
        return details
    except RuntimeError:
        return None


def get_ai_services_key(resource_group: str, account_name: str):
    """Obtém a key do recurso AI Services."""
    try:
        keys = run_az(
            f"cognitiveservices account keys list "
            f"--name {account_name} --resource-group {resource_group}"
        )
        return keys.get("key1", "")
    except RuntimeError:
        return ""


def get_search_details(resource_group: str):
    """Procura um recurso AI Search no resource group."""
    try:
        search_resources = run_az(
            f"resource list --resource-group {resource_group} "
            f"--resource-type Microsoft.Search/searchServices"
        )
        if search_resources:
            search_name = search_resources[0]["name"]
            search_keys = run_az(
                f"search admin-key show --service-name {search_name} "
                f"--resource-group {resource_group}"
            )
            return {
                "endpoint": f"https://{search_name}.search.windows.net",
                "key": search_keys.get("primaryKey", ""),
            }
    except RuntimeError:
        pass
    return None


def prompt_user(message: str, default: str = "") -> str:
    """Pede input ao utilizador com valor por defeito."""
    if default:
        value = input(f"{message} [{default}]: ").strip()
        return value if value else default
    return input(f"{message}: ").strip()


def write_env(config: dict, filepath: str = ".env"):
    """Escreve o ficheiro .env."""
    lines = [
        "# ============================================",
        "# Azure AI Foundry - Workshop Configuration",
        "# ============================================",
        f"# Gerado automaticamente por setup_env.py",
        "",
        "# --- Azure AI Foundry Project ---",
        f"AZURE_AI_FOUNDRY_ENDPOINT={config.get('foundry_endpoint', '')}",
        f"AZURE_AI_FOUNDRY_PROJECT={config.get('foundry_project', '')}",
        f"AZURE_AI_FOUNDRY_KEY={config.get('foundry_key', '')}",
        "",
        "# --- Azure AI Agent Service (Lab 3.1) ---",
        f"AZURE_AI_AGENT_ENDPOINT={config.get('agent_endpoint', '')}",
        "",
        "# --- Model Deployments ---",
        f"MODEL_DEPLOYMENT={config.get('model_deployment', 'gpt-4o')}",
        f"EMBEDDING_DEPLOYMENT={config.get('embedding_deployment', 'text-embedding-ada-002')}",
        "",
        "# --- Azure AI Search (Lab 4 - RAG) ---",
        f"AZURE_SEARCH_ENDPOINT={config.get('search_endpoint', '')}",
        f"AZURE_SEARCH_KEY={config.get('search_key', '')}",
        f"AZURE_SEARCH_INDEX={config.get('search_index', 'workshop-index')}",
        "",
        "# --- Azure API Management (Lab 6 - APIM) - Opcional ---",
        f"APIM_ENDPOINT={config.get('apim_endpoint', '')}",
        f"APIM_SUBSCRIPTION_KEY={config.get('apim_key', '')}",
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n✅ Ficheiro {filepath} criado com sucesso!")


def main():
    print("=" * 55)
    print("  🚀 Setup do Workshop Azure AI Foundry")
    print("=" * 55)

    config = {}
    auto_mode = False

    # 1. Verificar se az CLI está disponível
    if is_az_available():
        account = check_az_login()
        if account:
            auto_mode = True
    else:
        print("\n⚠️  Azure CLI não encontrada.")
        print("   A funcionar em modo manual (Codespaces / ambiente sem az CLI).")
        print("   Vai precisar de copiar os valores do portal: https://ai.azure.com")

    # 2. Auto-descoberta (se az disponível e autenticado)
    if auto_mode:
        projects = list_foundry_projects()

        if projects:
            print(f"\n📋 Projetos encontrados ({len(projects)}):")
            for i, p in enumerate(projects):
                print(f"   {i + 1}. {p.get('name', 'N/A')} ({p.get('resourceGroup', 'N/A')})")

            if len(projects) == 1:
                chosen = projects[0]
                print(f"\n→ A usar: {chosen['name']}")
            else:
                idx = int(prompt_user("\nEscolhe o número do projeto", "1")) - 1
                chosen = projects[idx]

            config["foundry_project"] = chosen.get("name", "")
            rg = chosen.get("resourceGroup", "")

            # Tentar obter endpoint e key
            # Para AI Services (Foundry v2), o endpoint é do tipo:
            # https://<name>.services.ai.azure.com ou https://<name>.cognitiveservices.azure.com
            ai_services = run_az(
                f"resource list --resource-group {rg} "
                f"--resource-type Microsoft.CognitiveServices/accounts"
            )
            if ai_services:
                svc = ai_services[0]
                svc_name = svc["name"]
                try:
                    svc_details = run_az(
                        f"cognitiveservices account show "
                        f"--name {svc_name} --resource-group {rg}"
                    )
                    config["foundry_endpoint"] = svc_details.get("properties", {}).get(
                        "endpoint", f"https://{svc_name}.services.ai.azure.com"
                    )
                    key = get_ai_services_key(rg, svc_name)
                    config["foundry_key"] = key
                except RuntimeError:
                    config["foundry_endpoint"] = f"https://{svc_name}.services.ai.azure.com"

            # Derivar Agent Service endpoint
            if config.get("foundry_endpoint") and config.get("foundry_project"):
                base = config["foundry_endpoint"].rstrip("/")
                # Agent endpoint needs services.ai.azure.com (not cognitiveservices)
                base = base.replace(".cognitiveservices.azure.com", ".services.ai.azure.com")
                config["agent_endpoint"] = f"{base}/api/projects/{config['foundry_project']}"

            # Procurar AI Search
            search = get_search_details(rg)
            if search:
                config["search_endpoint"] = search["endpoint"]
                config["search_key"] = search["key"]
                print(f"✅ AI Search encontrado: {search['endpoint']}")
        else:
            print("\n⚠️ Nenhum projeto encontrado automaticamente.")

    # 3. Confirmar/pedir valores manualmente
    if auto_mode:
        print("\n📝 Confirma os valores (Enter para manter o valor auto-detectado):\n")
    else:
        print("\n📝 Introduz os valores do teu projeto Azure AI Foundry:")
        print("   (encontras tudo em https://ai.azure.com → teu projeto → Overview)\n")

    config["foundry_endpoint"] = prompt_user(
        "  Foundry Endpoint",
        config.get("foundry_endpoint", "https://<nome>.services.ai.azure.com"),
    )
    config["foundry_project"] = prompt_user(
        "  Nome do projeto dentro do Foundry",
        config.get("foundry_project", ""),
    )
    config["foundry_key"] = prompt_user(
        "  Foundry Key",
        config.get("foundry_key", ""),
    )
    config["model_deployment"] = prompt_user(
        "  Deployment do modelo chat (nome)", 
        config.get("model_deployment", "gpt-4o"),
    )
    config["embedding_deployment"] = prompt_user(
        "  Deployment de embeddings (nome)",
        config.get("embedding_deployment", "text-embedding-ada-002"),
    )
    config["search_endpoint"] = prompt_user(
        "  AI Search Endpoint (vazio se não tiver)",
        config.get("search_endpoint", ""),
    )
    config["search_key"] = prompt_user(
        "  AI Search Admin Key",
        config.get("search_key", ""),
    )
    config["search_index"] = "workshop-index"

    # Derivar agent endpoint se ainda não definido
    if not config.get("agent_endpoint") and config.get("foundry_endpoint") and config.get("foundry_project"):
        base = config["foundry_endpoint"].rstrip("/")
        base = base.replace(".cognitiveservices.azure.com", ".services.ai.azure.com")
        config["agent_endpoint"] = f"{base}/api/projects/{config['foundry_project']}"

    config["agent_endpoint"] = prompt_user(
        "  Agent Service Endpoint (Lab 3.1)",
        config.get("agent_endpoint", ""),
    )

    # 4. Escrever .env
    write_env(config)

    print("\n📋 Resumo:")
    print(f"   Endpoint: {config['foundry_endpoint']}")
    print(f"   Agent EP: {config.get('agent_endpoint', 'N/A')}")
    print(f"   Projeto:  {config.get('foundry_project', 'N/A')}")
    print(f"   Modelo:   {config['model_deployment']}")
    print(f"   Embeddings: {config['embedding_deployment']}")
    if config.get("search_endpoint"):
        print(f"   AI Search: {config['search_endpoint']}")
    print("\n🎉 Pronto! Podes começar o Lab 1.")


if __name__ == "__main__":
    main()

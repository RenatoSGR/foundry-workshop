# 🚀 Workshop Azure AI Foundry - Iniciação (2 horas)

## Sobre este Workshop

Workshop prático de introdução ao **Azure AI Foundry** (v2), desenhado para participantes com poucas noções prévias. Em 2 horas, vais explorar modelos de IA, criar agentes inteligentes, configurar RAG com AI Search e muito mais.

## 📋 Pré-requisitos

Antes do workshop, certifica-te que tens:

- [ ] Uma conta Azure com uma **subscrição ativa** ([criar conta gratuita](https://azure.microsoft.com/free/))
- [ ] Um **projeto Azure AI Foundry** já criado ([portal](https://ai.azure.com))
- [ ] Um modelo **GPT-4o** deployado no projeto (deployment name: `gpt-4o`)
- [ ] Um modelo **text-embedding-ada-002** deployado (deployment name: `text-embedding-ada-002`)
- [ ] **Python 3.10+** instalado (já incluído no Codespaces)
- [ ] **Azure CLI** instalado e autenticado (`az login`) — opcional, permite auto-descoberta
- [ ] **VS Code** instalado (recomendado) com extensão Jupyter
- [ ] **Git** instalado

## ⚡ Setup Rápido (5 minutos)

### Opção A: GitHub Codespaces (mais rápido) ☁️

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/RenatoSGR/foundry-workshop/codespaces/new)

1. Clica no botão acima (ou vai a **Code → Codespaces → New codespace**)
2. Espera que o ambiente carregue (as dependências instalam-se automaticamente)
3. No terminal, executa:
   ```bash
   python setup_env.py
   ```
4. O script pede-te os valores do portal ([ai.azure.com](https://ai.azure.com) → teu projeto → Overview)

> No Codespaces a Azure CLI já vem instalada. Se fizeres `az login`, o script descobre tudo automaticamente.

### Opção B: Local

```bash
# 1. Clona o repositório
git clone https://github.com/RenatoSGR/foundry-workshop.git
cd foundry-workshop

# 2. Cria ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 3. Instala dependências
pip install -r requirements.txt

# 4. Configura o .env
python setup_env.py
```

O script `setup_env.py` funciona em **dois modos**:
- **Com Azure CLI** (`az login`): descobre automaticamente o teu projeto, extrai endpoints e keys
- **Sem Azure CLI** (Codespaces, etc.): pede os valores manualmente — copia do portal [ai.azure.com](https://ai.azure.com)

> **Alternativa manual:** Copia `.env.template` para `.env` e preenche os valores à mão.

## 📁 Estrutura do Repositório

```
workshop/
├── README.md                          # Este ficheiro
├── requirements.txt                   # Dependências Python
├── setup_env.py                       # Script automático de configuração
├── .env.template                      # Template de configuração (manual)
├── labs/
│   ├── lab01-intro-foundry.ipynb      # Lab 1: Intro e Componentes (10 min)
│   ├── lab02-modelos.ipynb            # Lab 2: Modelos e Deployments (15 min)
│   ├── lab03-agentes.ipynb            # Lab 3: Agentes com Tools (15 min)
│   ├── lab04-knowledge-rag.ipynb      # Lab 4: Knowledge, RAG & AI Search (15 min)
│   ├── lab05-workflows.ipynb          # Lab 5: Workflows com LLM (10 min)
│   ├── lab05b-agent-workflows.ipynb   # Lab 5b: Workflow de Agentes Sequencial (15 min)
│   ├── lab06-apim.ipynb               # Lab 6: API Management para IA (10 min)
│   ├── lab07-observabilidade.ipynb    # Lab 7: Observabilidade e Governance (10 min)
│   └── lab08-red-teaming.ipynb        # Lab 8: Red Teaming (10 min)
└── data/
    └── documentos/
        └── exemplo.md                 # Documento exemplo para RAG
```

## 🗺️ Agenda

| # | Lab | Duração | Tópicos |
|---|-----|---------|---------|
| 1 | Intro e Componentes Foundry | 10 min | O que é o Foundry, portal, componentes principais |
| 2 | Modelos e Deployment | 20 min | Deploy de modelos, playground, métricas, consumir via código |
| 3 | Agentes | 30 min | O que são agentes, criar agentes, tools, publicar no M365 |
| 4 | Knowledge & RAG | 15 min | RAG, indexação, AI Search, grounding |
| 5 | Workflows com LLM | 10 min | Pipelines de chamadas encadeadas ao modelo |
| 5b | Workflow de Agentes | 15 min | Pipeline sequencial de agentes Foundry |
| 6 | API Management | 10 min | APIM como gateway para modelos de IA |
| 7 | Observabilidade & Governance | 10 min | Monitoring, tracing, governance |
| 8 | Red Teaming | 10 min | Testes de segurança de modelos |
| - | Conclusões | 5 min | Recap e próximos passos |

## 🔧 Configuração do .env

### Opção 1: Automática (recomendado) 🚀

```bash
python setup_env.py
```

O script faz tudo por ti:
1. Verifica que estás autenticado na Azure CLI
2. Lista os teus projetos AI Foundry e pede-te para escolher
3. Extrai o endpoint e key do AI Services associado
4. Deteta AI Search (se existir) e extrai endpoint/key
5. Gera o ficheiro `.env` pronto a usar

### Opção 2: Manual

Copia `.env.template` para `.env` e preenche:

| Variável | Onde encontrar |
|----------|---------------|
| `AZURE_AI_FOUNDRY_ENDPOINT` | Portal Foundry → Project → Overview → Endpoint |
| `AZURE_AI_FOUNDRY_KEY` | Portal Foundry → Project → Overview → Keys |
| `MODEL_DEPLOYMENT` | Nome do deployment do modelo de chat (ex: `gpt-4o`) |
| `EMBEDDING_DEPLOYMENT` | Nome do deployment de embeddings (ex: `text-embedding-ada-002`) |
| `AZURE_SEARCH_ENDPOINT` | Portal Azure → AI Search → Overview → URL |
| `AZURE_SEARCH_KEY` | Portal Azure → AI Search → Keys → Admin Key |

> **Nota:** No Foundry v2, precisas apenas de **um endpoint e uma key** para tudo (chat, embeddings, agentes). Já não é necessário configurar variáveis `AZURE_OPENAI_*` separadas.

## 💡 Dicas

- **Não te preocupes com código complexo** — os notebooks estão prontos, só precisas de executar `python setup_env.py`
- **Segue os passos por ordem** — cada lab constrói sobre o anterior
- **Em caso de erro** — verifica se o `.env` está correcto e se os modelos estão deployados
- **Pede ajuda** — o instrutor está cá para isso!

## 📚 Recursos Adicionais

- [Documentação Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)
- [Azure AI Foundry Portal](https://ai.azure.com)
- [SDK azure-ai-projects](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [SDK azure-ai-inference](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme)
- [Azure AI Search](https://learn.microsoft.com/azure/search/)

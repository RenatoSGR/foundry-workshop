# 🚀 Workshop Azure AI Foundry - Iniciação (2 horas)

## Sobre este Workshop

Workshop prático de introdução ao **Azure AI Foundry** (v2), desenhado para participantes com poucas noções prévias. Em 2 horas, vais explorar modelos de IA, criar agentes inteligentes, configurar RAG com AI Search e muito mais.

## 📋 Pré-requisitos

Antes do workshop, certifica-te que tens:

- [ ] Uma conta Azure com uma **subscrição ativa** ([criar conta gratuita](https://azure.microsoft.com/free/))
- [ ] Um **projeto Azure AI Foundry** já criado ([portal](https://ai.azure.com))
- [ ] Um modelo **GPT-4o** deployado no projeto (deployment name: `gpt-4o`)
- [ ] Um modelo **text-embedding-ada-002** deployado (deployment name: `text-embedding-ada-002`)
- [ ] **Python 3.10+** instalado
- [ ] **VS Code** instalado (recomendado) com extensão Jupyter
- [ ] **Git** instalado

## ⚡ Setup Rápido (5 minutos)

```bash
# 1. Clona o repositório
git clone <URL_DO_REPO>
cd workshop

# 2. Cria ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 3. Instala dependências
pip install -r requirements.txt

# 4. Copia o ficheiro de configuração e preenche com os teus valores
cp .env.template .env
```

Abre o ficheiro `.env` e preenche com os teus endpoints e keys do Azure AI Foundry.

## 📁 Estrutura do Repositório

```
workshop/
├── README.md                          # Este ficheiro
├── requirements.txt                   # Dependências Python
├── .env.template                      # Template de configuração
├── labs/
│   ├── lab01-intro-foundry.ipynb      # Lab 1: Intro e Componentes (10 min)
│   ├── lab02-modelos.ipynb            # Lab 2: Modelos e Deployments (20 min)
│   ├── lab03-agentes.ipynb            # Lab 3: Agentes com Tools (30 min)
│   ├── lab04-knowledge-rag.ipynb      # Lab 4: Knowledge, RAG & AI Search (15 min)
│   ├── lab05-workflows.ipynb          # Lab 5: Workflows Sequenciais (10 min)
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
| 5 | Workflows | 10 min | Workflows sequenciais com agentes |
| 6 | API Management | 10 min | APIM como gateway para modelos de IA |
| 7 | Observabilidade & Governance | 10 min | Monitoring, tracing, governance |
| 8 | Red Teaming | 10 min | Testes de segurança de modelos |
| - | Conclusões | 5 min | Recap e próximos passos |

## 🔧 Configuração do .env

Após criar o teu projeto no [Azure AI Foundry Portal](https://ai.azure.com), copia os seguintes valores:

| Variável | Onde encontrar |
|----------|---------------|
| `AZURE_AI_FOUNDRY_ENDPOINT` | Portal Foundry → Project → Overview → Endpoint |
| `AZURE_AI_FOUNDRY_KEY` | Portal Foundry → Project → Overview → Keys |
| `AZURE_AI_FOUNDRY_PROJECT` | Portal Foundry → Project → Overview → Project name |
| `AZURE_OPENAI_ENDPOINT` | Portal Foundry → Models → Deployment → Endpoint |
| `AZURE_OPENAI_KEY` | Portal Foundry → Models → Deployment → Key |
| `AZURE_OPENAI_DEPLOYMENT` | Nome do teu deployment (ex: `gpt-4o`) |
| `AZURE_SEARCH_ENDPOINT` | Portal Azure → AI Search → Overview → URL |
| `AZURE_SEARCH_KEY` | Portal Azure → AI Search → Keys → Admin Key |

## 💡 Dicas

- **Não te preocupes com código complexo** — os notebooks estão prontos, só precisas de configurar o `.env`
- **Segue os passos por ordem** — cada lab constrói sobre o anterior
- **Em caso de erro** — verifica se o `.env` está correcto e se os modelos estão deployados
- **Pede ajuda** — o instrutor está cá para isso!

## 📚 Recursos Adicionais

- [Documentação Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)
- [Azure AI Foundry Portal](https://ai.azure.com)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Search](https://learn.microsoft.com/azure/search/)

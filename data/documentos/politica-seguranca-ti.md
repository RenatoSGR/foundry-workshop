# Política de Segurança de TI — Contoso

## Objetivo
Esta política define as regras e boas práticas de segurança da informação para todos os colaboradores da Contoso. O cumprimento é obrigatório e sujeito a auditorias periódicas.

---

## 1. Gestão de Passwords

- As passwords devem ter no mínimo **14 caracteres**, incluindo maiúsculas, minúsculas, números e caracteres especiais.
- É obrigatório alterar a password a cada **90 dias**.
- Não é permitido reutilizar as últimas **12 passwords**.
- A utilização de um gestor de passwords aprovado (1Password Business) é **obrigatória**.
- A partilha de passwords entre colaboradores é **estritamente proibida**.

## 2. Autenticação Multi-Fator (MFA)

- Todos os acessos a sistemas corporativos exigem **MFA ativado**.
- Métodos aceites: Microsoft Authenticator, chave de segurança FIDO2, Windows Hello.
- SMS como segundo fator **não é permitido** desde janeiro de 2025.
- Em caso de perda do dispositivo MFA, contactar o Service Desk imediatamente.

## 3. Dispositivos e Endpoints

- Apenas dispositivos geridos pelo **Microsoft Intune** podem aceder a recursos corporativos.
- O disco deve estar encriptado com **BitLocker** (Windows) ou **FileVault** (macOS).
- As atualizações de segurança do sistema operativo devem ser instaladas no prazo de **72 horas** após disponibilização.
- Dispositivos pessoais (BYOD) podem aceder apenas ao email e Teams, mediante registo no Intune.

## 4. Classificação de Dados

| Nível | Descrição | Exemplo | Controlo |
|-------|-----------|---------|----------|
| **Público** | Informação sem restrições | Website, blog posts | Nenhum especial |
| **Interno** | Uso interno geral | Apresentações, newsletters | Acesso autenticado |
| **Confidencial** | Informação sensível do negócio | Dados financeiros, roadmaps | Encriptação + ACL |
| **Restrito** | Altamente sensível | Dados pessoais (RGPD), contratos | Encriptação + MFA + auditoria |

## 5. Utilização de Email

- Não abrir anexos de remetentes desconhecidos.
- Reportar emails suspeitos usando o botão **"Report Phishing"** no Outlook.
- Não enviar dados classificados como **Confidencial** ou **Restrito** por email sem encriptação.
- O reencaminhamento automático para emails externos é **bloqueado**.

## 6. Acesso Remoto e VPN

- O acesso remoto é feito via **Azure VPN Gateway** ou **Microsoft Entra Private Access**.
- Ligações a redes Wi-Fi públicas devem usar sempre a VPN corporativa.
- Sessões inativas são terminadas automaticamente após **15 minutos**.
- O acesso a partir de países não autorizados é bloqueado por geofencing.

## 7. Resposta a Incidentes

Em caso de incidente de segurança:

1. **Não desligar** o computador (preservar evidências).
2. Desligar o cabo de rede ou desativar o Wi-Fi.
3. Contactar o **Security Operations Center (SOC)**: soc@contoso.com ou extensão **9111**.
4. Documentar o que aconteceu (hora, ação, ecrãs).
5. Aguardar instruções da equipa de segurança.

> ⚠️ O tempo máximo de reporte de incidentes é de **1 hora** após deteção.

## 8. Software Aprovado

- Apenas software do catálogo **Company Portal** pode ser instalado.
- Pedidos de software adicional devem ser feitos via ticket no ServiceNow.
- A instalação de software não autorizado resulta em **bloqueio automático** pelo Intune.
- Ferramentas de IA generativa externas (ex: ChatGPT free) **não são permitidas** para dados corporativos. Usar apenas o **Azure OpenAI** interno.

## Contactos de Segurança

- **Service Desk**: servicedesk@contoso.com | Extensão 5000
- **SOC (24/7)**: soc@contoso.com | Extensão 9111
- **CISO**: ciso@contoso.com
- **Portal de Incidentes**: https://security.contoso.com

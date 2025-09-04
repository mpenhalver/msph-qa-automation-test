# Padrões de Qualidade Cogna - Testes Automatizados

## 🎯 Diretrizes Gerais

### Nomenclatura
- Nomes de testes devem ser descritivos e em português
- Usar snake_case para funções Python
- Usar kebab-case para arquivos Robot Framework
- Prefixar testes com `test_` em Python

### Estrutura de Código
- Máximo 20 linhas por função de teste
- Separar setup, ação e verificação claramente
- Usar comentários para explicar lógica complexa
- Evitar código duplicado entre testes

## 🌐 Selenium WebDriver

### Waits e Timing
- NUNCA usar `time.sleep()` - sempre usar WebDriverWait
- Timeout padrão: 10 segundos para elementos
- Timeout para páginas: 30 segundos
- Usar Expected Conditions apropriadas

### Seletores
- Prioridade: ID > CSS Selector > XPath
- Evitar seletores baseados em texto que pode mudar
- Usar data-testid quando disponível
- Documentar seletores complexos

### Configuração de Driver
- Sempre usar WebDriverManager para drivers
- Configurar modo headless para CI/CD
- Definir window size explicitamente
- Implementar cleanup adequado (driver.quit())

### Page Object Model
- Implementar POM para testes UI complexos
- Separar locators de ações
- Usar properties para elementos
- Documentar cada página/componente

## 🤖 Robot Framework

### Estrutura de Arquivos
- Um arquivo .robot por funcionalidade
- Separar keywords customizadas em arquivos resource
- Usar variáveis externas para dados de teste
- Organizar em suites lógicas

### Keywords
- Nomes em português e descritivos
- Documentar propósito e parâmetros
- Máximo 10 steps por keyword
- Usar [Arguments] e [Return] quando necessário

### Variáveis e Configuração
- Usar ${VARIAVEL} para valores configuráveis
- Definir timeouts como variáveis
- Separar dados de teste em arquivos .yaml
- Usar variáveis de ambiente para credenciais

### Bibliotecas
- Preferir bibliotecas padrão do Robot Framework
- Documentar bibliotecas customizadas
- Versionar dependências no requirements.txt
- Testar compatibilidade entre versões

## 🔌 Testes de API

### Estrutura de Requests
- Validar sempre status code HTTP
- Verificar Content-Type das respostas
- Implementar retry para requests instáveis
- Usar timeout adequado (5-10 segundos)

### Validação de Dados
- Verificar estrutura JSON com schema
- Validar tipos de dados retornados
- Testar casos de erro (4xx, 5xx)
- Verificar headers de segurança

### Autenticação
- Usar variáveis de ambiente para tokens
- Implementar refresh de tokens quando necessário
- Testar cenários de token expirado
- Não logar credenciais sensíveis

### Dados de Teste
- Usar factories para criar dados de teste
- Limpar dados após execução
- Usar IDs únicos para evitar conflitos
- Separar dados por ambiente (dev, staging, prod)

## 📱 Testes Mobile (Appium)

### Configuração de Capabilities
- Definir capabilities mínimas necessárias
- Usar variáveis para diferentes dispositivos
- Configurar timeouts adequados
- Implementar reset de app quando necessário

### Seletores Mobile
- Priorizar accessibility id
- Usar resource-id quando disponível
- Evitar xpath complexos
- Testar em diferentes resoluções

### Gestos e Interações
- Usar métodos nativos do Appium
- Implementar waits para elementos móveis
- Testar orientação de tela
- Verificar estados de conectividade

## 🔄 CI/CD e Pipeline

### GitHub Actions
- Usar versões fixas de actions
- Implementar cache para dependências
- Configurar artifacts para relatórios
- Definir timeouts para jobs

### Execução Paralela
- Dividir testes em grupos lógicos
- Usar matrix strategy quando apropriado
- Evitar dependências entre testes
- Configurar retry para testes flaky

### Relatórios
- Gerar relatórios em formato HTML
- Incluir screenshots de falhas
- Configurar notificações de falha
- Armazenar logs detalhados

## 🛡️ Segurança e Boas Práticas

### Credenciais
- NUNCA commitar senhas ou tokens
- Usar GitHub Secrets para CI/CD
- Implementar rotação de credenciais de teste
- Usar contas específicas para automação

### Dados Sensíveis
- Mascarar dados pessoais em logs
- Usar dados fictícios para testes
- Implementar LGPD compliance
- Verificar vazamentos de dados

### Performance
- Monitorar tempo de execução dos testes
- Otimizar seletores lentos
- Usar paralelização quando possível
- Implementar health checks

## 📊 Monitoramento e Métricas

### Cobertura de Testes
- Manter cobertura mínima de 80%
- Priorizar cenários críticos de negócio
- Documentar cenários não automatizáveis
- Revisar cobertura regularmente

### Qualidade dos Testes
- Taxa de falsos positivos < 5%
- Tempo médio de execução por teste
- Frequência de manutenção necessária
- Feedback de desenvolvedores

### Relatórios
- Dashboard com métricas em tempo real
- Histórico de execuções
- Análise de tendências de falhas
- ROI da automação

## ⚠️ Tratamento de Erros

### Exceções
- Capturar exceções específicas
- Logar contexto suficiente para debug
- Implementar retry inteligente
- Falhar rápido quando apropriado

### Debug
- Incluir screenshots em falhas UI
- Logar requests/responses de API
- Capturar logs do browser/app
- Implementar modo verbose para debug

### Recovery
- Implementar cleanup em caso de falha
- Resetar estado entre testes
- Verificar pré-condições antes de executar
- Documentar dependências externas

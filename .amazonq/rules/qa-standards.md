# Regras Básicas de Qualidade

## Selenium
- Nunca usar time.sleep() - sempre usar WebDriverWait
- Usar seletores específicos (ID > CSS > XPath)
- Sempre fechar WebDriver com driver.quit()

## Testes
- Nomes descritivos em português
- Máximo 20 linhas por função
- Tratar exceções adequadamente

## API
- Validar status code HTTP
- Usar timeout adequado (5-10s)
- Não logar credenciais

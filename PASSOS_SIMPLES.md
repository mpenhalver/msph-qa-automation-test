# 🚀 Passos Simples - Teste Amazon Q Developer + GitHub

## ✅ O QUE FAZER (15 minutos)

### PASSO 1: Criar Repositório no GitHub
1. Acesse https://github.com
2. Clique em "New repository"
3. Nome: `cogna-qa-test`
4. Marque "Public"
5. Clique "Create repository"

### PASSO 2: Instalar Amazon Q Developer
1. Acesse: https://github.com/marketplace/amazon-q-developer
2. Clique "Install it for free"
3. Selecione sua organização
4. Escolha "Selected repositories"
5. Selecione o repositório `cogna-qa-test`
6. Clique "Install"

### PASSO 3: Subir Arquivos para o GitHub
```bash
# No terminal, dentro desta pasta:
cd /Users/msph/Library/CloudStorage/OneDrive-amazon.com/_MyDocuments/Clientes/Cogna/Projetos/Qualidade/Cogna_Quality_Test

# Inicializar Git
git init
git add .
git commit -m "Initial commit"

# Conectar com seu repositório (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/cogna-qa-test.git
git push -u origin main
```

### PASSO 4: Criar Branch com Problemas
```bash
# Criar nova branch
git checkout -b feature/testes-problematicos

# Adicionar apenas o arquivo problemático
git add test_github_integration.py
git add .amazonq/
git commit -m "feat: Adicionar testes automatizados com problemas"

# Subir branch
git push origin feature/testes-problematicos
```

### PASSO 5: Criar Pull Request
1. No GitHub, vá para seu repositório
2. Clique "Compare & pull request"
3. Título: "Adicionar testes de login automatizados"
4. Descrição: "Implementação inicial dos testes Selenium"
5. Clique "Create pull request"

### PASSO 6: Aguardar Amazon Q Developer
- Amazon Q Developer vai analisar automaticamente
- Aguarde 2-3 minutos
- Você verá comentários automáticos no PR

### PASSO 7: Testar Comandos
No PR, adicione comentários com:
```
/q review
```
```
/q Como posso melhorar estes testes?
```
```
/q Corrija os problemas de timing
```

## 🎯 O QUE ESPERAR

Amazon Q Developer deve identificar:
- ❌ `time.sleep()` em vez de WebDriverWait
- ❌ Seletores frágeis (`.btn`)
- ❌ Driver não fechado
- ❌ URLs hardcoded
- ❌ Credenciais hardcoded

## 📋 CHECKLIST

- [ ] Repositório criado no GitHub
- [ ] Amazon Q Developer instalado
- [ ] Arquivos enviados para GitHub
- [ ] Branch criada
- [ ] Pull Request aberto
- [ ] Amazon Q Developer analisou o código
- [ ] Comandos `/q` testados
- [ ] Problemas identificados
- [ ] Sugestões recebidas

## ❓ PROBLEMAS COMUNS

**Erro de permissão no Git:**
```bash
git config --global user.email "seu@email.com"
git config --global user.name "Seu Nome"
```

**Amazon Q não aparece:**
- Aguarde 5 minutos
- Verifique se a instalação foi feita corretamente
- Certifique-se que o repositório está público

**Comandos `/q` não funcionam:**
- Certifique-se que está comentando no PR
- Aguarde alguns segundos entre comandos

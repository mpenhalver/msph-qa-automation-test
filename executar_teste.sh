#!/bin/bash

# Script para executar teste Amazon Q Developer + GitHub
# Execute: chmod +x executar_teste.sh && ./executar_teste.sh

echo "🚀 INICIANDO TESTE AMAZON Q DEVELOPER + GITHUB"
echo "=============================================="

# Verificar se Git está configurado
if ! git config user.name > /dev/null; then
    echo "⚠️  Configurando Git..."
    read -p "Digite seu nome: " nome
    read -p "Digite seu email: " email
    git config --global user.name "$nome"
    git config --global user.email "$email"
fi

# Inicializar repositório se necessário
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositório Git..."
    git init
fi

# Adicionar arquivos
echo "📄 Adicionando arquivos..."
git add test_github_integration.py
git add .amazonq/
git add PASSOS_SIMPLES.md

# Commit inicial
if ! git log --oneline -1 > /dev/null 2>&1; then
    echo "💾 Fazendo commit inicial..."
    git commit -m "Initial commit: Teste Amazon Q Developer"
fi

# Criar branch para teste
echo "🌿 Criando branch de teste..."
git checkout -b feature/testes-problematicos 2>/dev/null || git checkout feature/testes-problematicos

# Commit dos arquivos problemáticos
git add test_github_integration.py .amazonq/
git commit -m "feat: Adicionar testes automatizados com problemas intencionais

- Implementar testes Selenium para login
- Adicionar testes de API 
- Incluir problemas para demonstração Amazon Q Developer"

echo ""
echo "✅ PREPARAÇÃO CONCLUÍDA!"
echo ""
echo "🎯 PRÓXIMOS PASSOS MANUAIS:"
echo "1. Criar repositório no GitHub: msph-qa-automation-test"
echo "2. Instalar Amazon Q Developer: https://github.com/marketplace/amazon-q-developer"
echo "3. Conectar repositório:"
echo "   git remote add origin https://github.com/SEU_USUARIO/msph-qa-automation-test.git"
echo "   git push -u origin main"
echo "   git push origin feature/testes-problematicos"
echo "4. Criar Pull Request no GitHub"
echo "5. Aguardar análise do Amazon Q Developer"
echo ""
echo "📖 Consulte PASSOS_SIMPLES.md para detalhes"

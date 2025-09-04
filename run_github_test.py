#!/usr/bin/env python3
"""
Script para executar teste de integração Amazon Q Developer + GitHub
Simula o processo completo de criação de PR e revisão automática
"""

import os
import subprocess
import sys
from pathlib import Path

def print_header(title):
    print("\n" + "="*70)
    print(f"🎯 {title}")
    print("="*70)

def print_step(step_num, title, description):
    print(f"\n📋 PASSO {step_num}: {title}")
    print(f"📝 {description}")
    print("-" * 50)

def check_git_repo():
    """Verifica se está em um repositório Git"""
    try:
        subprocess.run(["git", "status"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_git_repo():
    """Configura repositório Git se necessário"""
    if not check_git_repo():
        print("🔧 Inicializando repositório Git...")
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        return True
    return False

def create_problematic_branch():
    """Cria branch com código problemático"""
    print("🌿 Criando branch para teste...")
    
    try:
        # Criar nova branch
        subprocess.run(["git", "checkout", "-b", "feature/qa-automation-problematic"], check=True)
        
        # Adicionar arquivos problemáticos
        subprocess.run(["git", "add", "test_github_integration.py"], check=True)
        subprocess.run(["git", "add", ".amazonq/"], check=True)
        
        # Commit com problemas intencionais
        commit_message = """feat: Adicionar testes de login automatizados

- Implementar testes Selenium para login
- Adicionar testes de API para usuários
- Configurar estrutura básica de testes

Closes #123"""
        
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        print("✅ Branch criada com código problemático")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar branch: {e}")
        return False

def simulate_github_integration():
    """Simula a integração com GitHub"""
    print_step(1, "PREPARAÇÃO", "Configurando ambiente para teste")
    
    # Verificar arquivos necessários
    required_files = [
        "test_github_integration.py",
        ".amazonq/rules/qa-standards.md",
        "github_integration_test.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Arquivos faltantes: {missing_files}")
        return False
    
    print("✅ Todos os arquivos necessários estão presentes")
    
    print_step(2, "REPOSITÓRIO GIT", "Configurando controle de versão")
    
    if setup_git_repo():
        print("✅ Repositório Git inicializado")
    else:
        print("✅ Repositório Git já existe")
    
    print_step(3, "BRANCH PROBLEMÁTICA", "Criando branch com código para revisão")
    
    if create_problematic_branch():
        print("✅ Branch criada com sucesso")
    else:
        print("❌ Falha ao criar branch")
        return False
    
    print_step(4, "SIMULAÇÃO AMAZON Q", "Demonstrando análise automática")
    
    # Simular análise do Amazon Q Developer
    problems_found = analyze_code_problems()
    display_analysis_results(problems_found)
    
    print_step(5, "PRÓXIMOS PASSOS", "Instruções para GitHub real")
    
    display_github_instructions()
    
    return True

def analyze_code_problems():
    """Simula análise de problemas pelo Amazon Q Developer"""
    problems = [
        {
            "file": "test_github_integration.py",
            "line": 15,
            "type": "timing",
            "severity": "high",
            "message": "Uso de time.sleep() detectado. Recomenda-se WebDriverWait.",
            "suggestion": "Substituir por WebDriverWait com Expected Conditions"
        },
        {
            "file": "test_github_integration.py", 
            "line": 25,
            "type": "selector",
            "severity": "medium",
            "message": "Seletor CSS frágil detectado: '.btn'",
            "suggestion": "Usar seletor mais específico como '[data-testid=\"login-button\"]'"
        },
        {
            "file": "test_github_integration.py",
            "line": 35,
            "type": "resource_leak",
            "severity": "high", 
            "message": "WebDriver não está sendo fechado adequadamente",
            "suggestion": "Adicionar driver.quit() no teardown ou usar context manager"
        },
        {
            "file": "test_github_integration.py",
            "line": 45,
            "type": "hardcoded_data",
            "severity": "medium",
            "message": "Credenciais hardcoded detectadas",
            "suggestion": "Usar variáveis de ambiente ou arquivo de configuração"
        },
        {
            "file": "test_github_integration.py",
            "line": 85,
            "type": "api_error_handling",
            "severity": "high",
            "message": "Falta tratamento de erro HTTP",
            "suggestion": "Verificar response.status_code antes de processar JSON"
        }
    ]
    
    return problems

def display_analysis_results(problems):
    """Exibe resultados da análise simulada"""
    print("\n🤖 ANÁLISE AMAZON Q DEVELOPER:")
    print("=" * 50)
    
    severity_colors = {
        "high": "🔴",
        "medium": "🟡", 
        "low": "🟢"
    }
    
    for i, problem in enumerate(problems, 1):
        color = severity_colors.get(problem["severity"], "⚪")
        print(f"\n{color} PROBLEMA {i}:")
        print(f"   📁 Arquivo: {problem['file']}")
        print(f"   📍 Linha: {problem['line']}")
        print(f"   🏷️  Tipo: {problem['type']}")
        print(f"   ⚠️  Severidade: {problem['severity'].upper()}")
        print(f"   💬 Mensagem: {problem['message']}")
        print(f"   💡 Sugestão: {problem['suggestion']}")
    
    print(f"\n📊 RESUMO:")
    print(f"   Total de problemas: {len(problems)}")
    print(f"   Alta severidade: {len([p for p in problems if p['severity'] == 'high'])}")
    print(f"   Média severidade: {len([p for p in problems if p['severity'] == 'medium'])}")

def display_github_instructions():
    """Exibe instruções para usar no GitHub real"""
    print("\n🚀 INSTRUÇÕES PARA GITHUB:")
    print("=" * 50)
    
    instructions = [
        "1. Criar repositório no GitHub: 'cogna-qa-automation-test'",
        "2. Instalar Amazon Q Developer: https://github.com/marketplace/amazon-q-developer",
        "3. Fazer push desta branch: git push origin feature/qa-automation-problematic",
        "4. Criar Pull Request no GitHub",
        "5. Aguardar revisão automática do Amazon Q Developer",
        "6. Usar comandos no PR:"
    ]
    
    for instruction in instructions:
        print(f"   {instruction}")
    
    print("\n💬 COMANDOS PARA TESTAR NO PR:")
    commands = [
        "/q review - Executar nova revisão",
        "/q Como posso melhorar a estabilidade destes testes?",
        "/q Corrija os problemas de timing neste código",
        "/q Refatore usando Page Object Model",
        "/q Adicione tratamento de erro adequado"
    ]
    
    for command in commands:
        print(f"   {command}")
    
    print("\n📋 CHECKLIST DE VALIDAÇÃO:")
    checklist = [
        "[ ] Amazon Q identificou problemas de timing",
        "[ ] Sugestões de WebDriverWait foram fornecidas", 
        "[ ] Problemas de seletores foram detectados",
        "[ ] Correções de resource leak foram sugeridas",
        "[ ] Melhorias de tratamento de erro foram propostas",
        "[ ] Código refatorado segue padrões de qualidade"
    ]
    
    for item in checklist:
        print(f"   {item}")

def main():
    """Executa teste completo de integração"""
    print_header("TESTE DE INTEGRAÇÃO: AMAZON Q DEVELOPER + GITHUB")
    print("🎯 Demonstração prática para time de Qualidade Cogna")
    print("📖 Baseado na documentação oficial da AWS")
    
    input("\n🎬 Pressione ENTER para iniciar o teste...")
    
    try:
        if simulate_github_integration():
            print_header("TESTE CONCLUÍDO COM SUCESSO")
            print("✅ Simulação executada com sucesso!")
            print("🎯 Próximo passo: Executar no GitHub real")
        else:
            print_header("TESTE FALHOU")
            print("❌ Problemas durante a execução")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Teste interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()

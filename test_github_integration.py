"""
Teste com problemas intencionais para demonstrar Amazon Q Developer no GitHub
Este arquivo será usado em Pull Request para testar a integração
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCognaLogin:
    """Testes de login com problemas intencionais para demonstração"""
    
    def setup_method(self):
        # ❌ Problema: Driver não configurado adequadamente
        self.driver = webdriver.Chrome()
        # ❌ Problema: Não define window size
        # ❌ Problema: Não configura timeouts
    
    def test_login_usuario_valido(self):
        """Teste de login com usuário válido - COM PROBLEMAS"""
        
        # ❌ Problema: URL hardcoded
        self.driver.get("https://app-dev.cogna.com/login")
        
        # ❌ Problema: Sem wait, pode falhar por timing
        self.driver.find_element(By.ID, "username").send_keys("admin@cogna.com")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        
        # ❌ Problema: Seletor frágil baseado em classe genérica
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        
        # ❌ Problema: Sleep fixo em vez de wait inteligente
        time.sleep(3)
        
        # ❌ Problema: Assertion frágil baseada em texto
        assert "Dashboard" in self.driver.page_source
        
        # ❌ Problema: Não fecha driver (memory leak)
    
    def test_login_usuario_invalido(self):
        """Teste de login com credenciais inválidas - COM PROBLEMAS"""
        
        self.driver.get("https://app-dev.cogna.com/login")
        
        # ❌ Problema: Credenciais hardcoded
        self.driver.find_element(By.ID, "username").send_keys("wrong@email.com")
        self.driver.find_element(By.ID, "password").send_keys("wrongpass")
        
        # ❌ Problema: XPath frágil
        self.driver.find_element(By.XPATH, "//button").click()
        
        # ❌ Problema: Sleep fixo
        time.sleep(2)
        
        # ❌ Problema: Não verifica mensagem de erro específica
        assert "error" in self.driver.page_source.lower()
    
    def test_formulario_cadastro(self):
        """Teste de preenchimento de formulário - COM PROBLEMAS"""
        
        # ❌ Problema: URL diferente hardcoded
        self.driver.get("https://forms.cogna.com/cadastro")
        
        # ❌ Problema: Não verifica se página carregou
        self.driver.find_element(By.NAME, "nome").send_keys("João Silva")
        self.driver.find_element(By.NAME, "email").send_keys("joao@test.com")
        
        # ❌ Problema: Elemento pode não estar visível
        self.driver.find_element(By.ID, "telefone").send_keys("11999999999")
        
        # ❌ Problema: Textarea pode não estar pronto
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Comentário de teste")
        
        # ❌ Problema: Submit sem verificar se botão está habilitado
        self.driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
        
        # ❌ Problema: Sleep em vez de wait
        time.sleep(5)
        
        # ❌ Problema: Assertion muito genérica
        assert "sucesso" in self.driver.page_source.lower()

class TestAPIEndpoints:
    """Testes de API com problemas intencionais"""
    
    def setup_method(self):
        # ❌ Problema: URL base hardcoded
        self.base_url = "https://api-dev.cogna.com"
        # ❌ Problema: Token hardcoded
        self.token = "abc123-dev-token"
    
    def test_listar_usuarios(self):
        """Teste de listagem de usuários via API - COM PROBLEMAS"""
        
        # ❌ Problema: Headers inadequados
        headers = {"Authorization": self.token}
        
        # ❌ Problema: Sem tratamento de erro HTTP
        response = requests.get(f"{self.base_url}/users", headers=headers)
        
        # ❌ Problema: Não verifica status code
        data = response.json()
        
        # ❌ Problema: Assertion sem contexto
        assert len(data) > 0
        
        # ❌ Problema: Não valida estrutura da resposta
        assert data[0]["name"]
    
    def test_criar_usuario(self):
        """Teste de criação de usuário via API - COM PROBLEMAS"""
        
        # ❌ Problema: Dados hardcoded
        user_data = {
            "name": "Teste User",
            "email": "teste@cogna.com",
            "role": "student"
        }
        
        # ❌ Problema: Headers incompletos
        headers = {"Authorization": self.token}
        
        # ❌ Problema: Sem timeout
        response = requests.post(f"{self.base_url}/users", 
                               json=user_data, 
                               headers=headers)
        
        # ❌ Problema: Não trata erro de criação
        assert response.status_code == 201
        
        # ❌ Problema: Não limpa dados criados
        created_user = response.json()
        assert created_user["email"] == user_data["email"]

def test_funcao_sem_classe():
    """Função de teste fora de classe - MÁ PRÁTICA"""
    
    # ❌ Problema: Teste sem contexto de classe
    # ❌ Problema: Sem setup/teardown adequado
    
    driver = webdriver.Chrome()
    
    try:
        # ❌ Problema: Lógica complexa em uma função
        driver.get("https://app.cogna.com")
        
        # ❌ Problema: Múltiplas responsabilidades
        driver.find_element(By.ID, "login").click()
        time.sleep(1)
        
        driver.find_element(By.ID, "username").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("test")
        driver.find_element(By.ID, "submit").click()
        
        time.sleep(3)
        
        # ❌ Problema: Assertion inadequada
        assert driver.current_url != "https://app.cogna.com"
        
    except Exception as e:
        # ❌ Problema: Tratamento genérico de exceção
        print(f"Erro: {e}")
        
    finally:
        # ❌ Problema: Cleanup pode falhar
        driver.quit()

# ❌ Problema: Execução direta sem framework
if __name__ == "__main__":
    test = TestCognaLogin()
    test.setup_method()
    test.test_login_usuario_valido()
    test.test_login_usuario_invalido()
    
    api_test = TestAPIEndpoints()
    api_test.setup_method()
    api_test.test_listar_usuarios()
    
    test_funcao_sem_classe()

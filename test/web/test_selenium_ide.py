# 1 - Importar Bibliotecas / Pacotes


# 2 - Classe e Definições
class TestConsultarMantis():
    def setup_method(self, method):
        # Instanciar o objeto do Selenium WebDriver como Chrome
        self.driver = webdriver.Chrome(
            'C:/Users/corre/PycharmProjects/fts132_inicial/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O robô irá esperar por até 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultarMantis(self):
        self.driver.get("https://iterasys.com.br/plataforma/home/index.php?action=initial")
        self.driver.set_window_size(1280, 680)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.ID, "btn_form_search").click()
        # time.sleep(3) # pausa forçada / "alfinete" / sempre deve remover antes de salvar no repositório
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"


36
test / web / test_selenium_wedriver.py
Comment
on
this
file


@ @-0

, 0 + 1, 36 @ @
# 1 Importar Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 Classe
class Test_Selenium_Webdriver():

    # Definição de Início - Executa antes do teste
    def setup_method(self, method):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/corre/PycharmProjects/fts132_inicial/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O Selenium vai esperar até 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador

    # Definição de Fim - Executa depois do teste
    def teardown_method(self, method):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    def testar_comprar_curso_mantis(self):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O Selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

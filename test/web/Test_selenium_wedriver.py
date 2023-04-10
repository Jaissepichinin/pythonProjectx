import datetime  # 1 importar bibliotecas

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

caminho_print = 'C:/Users/corre/pycharmproject/fts132_inicial/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


# 2 Classe
class Test_Selenium_Webdriver:
    # definicao de inicio - executa antes do teste
    def before_all(self):

    # criar a pasta com data e hora para criar os prints
    os.mkdriver(caminho_print)

    # Definicao  de Inicio- executa antes do teste
    def setup_method(self):
        # declarar o objeto do selenium e insranciar como o navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/jaiss_f3yllmx/PycharmProjects/pythonProject2/fts132_inicialjb/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # o selenium vai esperar ate 30 segundos pelos elementos
        self.driver.maximize_window()  # maximizar a janela do navegador

        # definicao de fim - executa depois do teste

    def teardown_method(self):
        # destruir o objeto do selenium
        self.driver.quit()
        # definicao do teste

        # Definicao do Teste

    @pytest.mark.parametrize('termo, curso, preco', [
        ('1', mantis', 'Mantis', 'R$ 59, 90'),
        ('2', ctfl', 'preparatorio CTFL', 'R$199, 00'),
        ])
    def testar_comprar_curso_mantis_com_click(self, termo, curso, preco):
        # selenium abre o site alvo do teste
        self.driver.get('https://iterasys.com.br/pt')
        # o selenium clica na caixa de pesquisa
        self.driver.get_screenshot_as_file(f'{caminho_print} passo 1 -home.png')
        self.driver.find_element(By.ID, 'searchtext').click()
        # o selenium apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # o selenium escreve 'mantis'na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print} passo 2 - pesquisa pelo curso.png')
        # o selenium clica no botao da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # o selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # o selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # o selenium valida o preco do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
        # selenium abre o site alvo do teste
        self.driver.get('https://iterasys.com.br/pt')
        self.driver.get_screenshot_as_file(
            ('C:/Users/jaiss_f3yllmx/PycharmProjects/pythonProject2/fts132_inicialjb/Prints'))
        # o selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # o selenium apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # o selenium escreve 'mantis'na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # o selenium pressiona a tecla enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        # o selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # o selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # o selenium valida o preco do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

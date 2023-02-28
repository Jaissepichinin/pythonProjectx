# Bibliotecas
import requests  # Framework de Teste API - Request

# Endereco da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # nos .asmx seria 'text.xml'


def test_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1008'

    # Executa
    resposta = requests.post(  # faz a requisicao passando: o endpoint da API
        url=base_url,  # o body json
        data=open('C:/Users/jaiss_f3yllmx/PycharmProjects/pythonProject2/test/db/user1.json', 'rb'),
        # o header com o Content - Type
        headers=headers
    )
    # Formatacao
    corpo_da_resposta = resposta.json()
    print(resposta)  # resposta bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # resposta formatada

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    status_code = 200
    id = 1008
    username = 'MMs'
    firstName = 'Minnie'
    lastName = 'Mouses'
    email = 'mms@teste.com'
    password = 'dev'
    phone = '999000'
    userStatus = 0

    # Executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formatacao
    corpo_da_resposta = resposta.json()
    print(resposta)  # resposta bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # resposta formatada

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone

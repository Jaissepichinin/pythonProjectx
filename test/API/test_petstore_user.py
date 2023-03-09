# Bibliotecas

import requests  # Framework de Teste API - Request

# Endereco da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # nos .asmx seria 'text.xml'


# token_usuario = ''

def testar_criar_usuario():
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

    print(f'Token: {token_usuario}')

def testar_consultar_usuario_com_token(token_usuario):
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

    print(f'Token: {token_usuario}')


def testar_alterar_usuario():
    # Configura
    username = 'MMs'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1009'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/jaiss_f3yllmx/PycharmProjects/pythonProject2/test/db/user2.json', 'rb'),
        headers=headers
    )

    # Formatacao
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # validacao
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_excluir_usuario():
    # Configura
    username = 'MMs'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'MMs'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )
    # Formatacao
    match resposta.status_code:
        case 200:  # apagar um usuario encontrado
            corpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

            # validacao
            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada

        case 400:  # apagar um usuario encontrado
            print('username fornecido incorreto')

        case 404:  # apagar um usuario encontrado
            print('usuario nao encontrado')


def testar_login_do_usuario():
    # configura
    username = 'MMs'
    password = 'sucesso'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

    # executa
    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )

    # formata
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find(inicio_mensagem_esperada) != -1

    frase = 'Neste fim do ano planeje o seu sucesso'
    assert frase.find('sucesso') != -1

    # extrair
    # na mensagem "logged in user session 1677681830418" queremos pegar os numeros
    mensagem_recebida = corpo_da_resposta['message']
    print(f'A mensagem recebida é: {mensagem_recebida}')
    token_usuario = mensagem_recebida[23:37]
    print(f'0 token do usuario é : {token_usuario}')
    testar_consultar_usuario_com_token(token_usuario)

    # Exemplo
    frase = "Saldo: R$ 1.987,65"  # 166 extrair
    valor = frase[7:18]
    print(f'0 valor é: {valor}')


''''
def testar_sequencia_de_testes():
    testar_login_do_usuario()
    time.sleep(3)
    testar_consultar_usuario()
'''

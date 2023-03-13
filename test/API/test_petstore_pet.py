import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


def testar_incluir_pet():
    # Configura
    # dados de entrada vem do pet1.json
    status_code_esperado = 200
    nome_pet_esperado = 'Snoopy'
    tag_esperada = 'vacinado'

    # executa
    resposta = requests.post(  # faz a requisicao passando: o endpoint da API
        url=base_url,  # o body json
        data=open('C:/Users/jaiss_f3yllmx/PycharmProjects/pythonProject2/test/db/pet1.json', 'rb'),
        # o header com o Content - Type
        headers=headers
    )

    # formata
    print(resposta)
    print(resposta.status_code)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)

    # valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada

import pytest

from main import calcular_volume_do_paralelograma


# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Nao é possivel dividir por zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

    # Calcular e testar a area de um quadrado
    # Area = Lado
def area_do_quadrado(lado):
        return lado ** 2

    # Calcular e testar a area de um retangulo
    # Area = Lado 1 * Lado 2
def area_do_retangulo(largura, comprimento):
        return largura * comprimento

    # Calcular e Testar a area de um triangulo
    # area = lado 1 * lado 2/2
def area_do_triangulo(lado1, lado2):
    return lado1 * lado2/2

#Calcular a área de um circulo
def area_do_circulo(raio):
    try:
     return 3.14 * raio ** 2
    except TypeError:
     return 'Falha no calculo - Raio não é um número'



if __name__ == '__main__':

    #Garcom - Requisicoes / Chamadas
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}') # <-- Prato

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtracao é {resultado}')

    resultado = multiplicar_dois_numeros(3,5)
    print(f'A multiplicacao é {resultado}')

    resultado = dividir_dois_numeros(8,0)
    print(f'A divisao é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 2)
    print(f'A exponenciação é {resultado}')

    resultado = area_do_quadrado(4)
    print(f'A área do quadrado é {resultado}')

    resultado = area_do_retangulo(3, 4)
    print(f'A área do retangulo é {resultado}')

    resultado = area_do_triangulo(6, 6)
    print(f'A área do triangulo é {resultado}')

    resultado = area_do_circulo(2)
    print(f'A área do circulo é {resultado}')


    #Degustador / Teste

def test_somar_dois_numeros():
    # - 1' Etapa : Configura / Prepara
    # Dados / Valores
    # Entradas / Input
    num1 = 4
    num2 = 5
    #Saida / Output
    resultado_esperado = 9

    # - 2 ' Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3' Etapa: Confirma / Check / valida
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    # 1ª Etapa - Configura / Prepara
    # Dados / Valores
    # Entradas / Inputs
    num1 = 2
    num2 = 2
    # Saida / Output
    resultado_esperado = 4
    # 2ª Etapa - Executar
    resultado_atual = elevar_um_numero_pelo_outro(num1,num2)
    # 3ª Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_area_do_quadrado():
    lado = 4
    resultado_esperado = 16
    resultado_atual = area_do_quadrado(lado)
    assert resultado_esperado == resultado_atual

def testar_area_do_retangulo():
    largura = 3
    comprimento = 4
    resultado_esperado = 12
    resultado_atual = area_do_retangulo(largura,comprimento)
    assert resultado_esperado == resultado_atual

def testar_area_do_triangulo():
    lado1 = 6
    lado2 = 6
    resultado_esperado = 18
    resultado_atual = area_do_triangulo(lado1,lado2)
    assert resultado_esperado == resultado_atual

#anotacao para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
    #valores
    (1,3.14), #teste n 1
    (2,12.56), #teste n 2
    (3,28.26), #teste n 3
    (4, 50.24), #teste n 4
    ('A', 'falha no calculo - raio e um numero'), #teste n 5
  ])

def testar_area_do_circulo(raio, resultado_esperado):
        # 1 Configura / comentamos para que os parametros sejam lidos
        raio = 2
        resultado_esperado = 12.56

        # 2 Executa
        resultado_atual = area_do_circulo(raio)

        # 3 Valida
        assert resultado_esperado == resultado_atual

def testar_calcular_volume_do_paralelograma():
    #1 Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    #2 Executa

    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    #3 valida
    assert resultado_atual == resultado_esperado
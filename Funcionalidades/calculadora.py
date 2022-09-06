def calculadora():
    from Visual.interface_simples import interface_simples

    interface_simples('Calculadora')
    operacoes = ('+', '-', '*', '/', '^')
    print("Digite o cálculo que deseja. Ex: x + y")
    existe1 = False
    existe2 = False

    while True:
        calculo = input()
        caracteres = calculo.split()
        if len(caracteres) == 3 and (caracteres[1] in operacoes):
            num1, existe1 = converte_int(caracteres[0])
            num2, existe2 = converte_int(caracteres[2])
            operacao = caracteres[1]
            if existe1 and existe2:
                break
        else:
            print('Valor(es) ou operação inválido(s)')

    if operacao == '+':
        print(somar(num1, num2))

    elif operacao == '-':
        print(subtrair(num1, num2))

    elif operacao == '*':
        print(multiplicar(num1, num2))

    elif operacao == '/':
        print(dividir(num1, num2))

    elif operacao == '^':
        print(elevar(num1, num2))


def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

def elevar(num1, num2):
    return num1 ** num2

def converte_int(num):
    try:
        return int(num), True
    except:
        print('Valor(es) ou operação inválido(s)')
        return None, None


if __name__ == '__main__':
    calculadora()

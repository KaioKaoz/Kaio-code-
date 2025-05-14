def calcula_soma1 (s_valor, ss_valor):
    return s_valor + ss_valor

def calcula_soma(valor1, valor2):
    calcula_soma = valor1 + valor2
    return calcula_soma

if __name__ == '__main__':
    n1=int(input('digite um valor inteiro'))
    n2=int(input('digite outro valor inteiro'))
    print(f'a soma dos valores é {calcula_soma(n1, n2)}')

    print(f'a soma dos valores é: {calcula_soma1(2.1,3.3)}')
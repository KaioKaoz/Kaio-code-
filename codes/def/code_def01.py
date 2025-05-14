def mostra_valor(valor):
    print(f'valor recebido:{valor}')

def mostra_dois_valores(valor1 ,valor2):
    print('valor 1:',valor1)
    print('valor 2:',valor2)

if __name__ == '__main__':
    print('primeira forma de fazer (sem variáveis, passa o valor direto):')
    mostra_valor(5)
    mostra_valor(23.8)

    print('Segunda forma de fazer (com variáveis, sem input):')
    v_inteiro = 43
    mostra_valor(v_inteiro)
    v_real=37.4
    mostra_valor(v_real)

    print('terceira forma de fazer (com variáveis, com input):')
    v_inteiro =int(input('digite um valor inteiro:'))
    v_real =int(input('digite um valor real:'))
    mostra_valor(v_inteiro)
    mostra_valor(v_real)

    print('quarta forma de fazer (chamar outra função para mostrar dois valores:')
    mostra_dois_valores(5,10)

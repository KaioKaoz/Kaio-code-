def calcula_dobro(b_valor):
    calculo_dobro= b_valor * 2
    return calculo_dobro

def calcula_triplo(t_valor):
    calculo_triplo= t_valor * 3
    return  calculo_triplo

if __name__ == "__main__":
    valor = int(input('digite um número que você queira saber o dobro:'))
    print(f'valor retornado pela função:{calcula_dobro(valor)}')

    valor1 = int(input('digite um número que você queira saber o triplo:'))
    print(f'valor do triplo: {calcula_triplo(valor1)}')
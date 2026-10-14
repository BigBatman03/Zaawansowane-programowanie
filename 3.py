def wyswietl_parzyste(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)

lista = range(1, 11)
wyswietl_parzyste(lista)
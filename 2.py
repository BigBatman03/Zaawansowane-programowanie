def liczby(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

def liczby2(lista):
    return [x * 2 for x in lista]

lista = [1, 2, 3, 4, 5]

print(liczby(lista))
print(liczby2(lista))

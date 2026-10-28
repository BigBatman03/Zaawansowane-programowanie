def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0


wynik = czy_parzysta(8)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

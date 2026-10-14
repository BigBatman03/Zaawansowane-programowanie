def polacz_i_podnies_do_szescianu(lista1: list, lista2: list) -> list:
    polaczone = list(dict.fromkeys(lista1 + lista2))
    return [element ** 3 for element in polaczone]


print(polacz_i_podnies_do_szescianu([1, 2, 3], [3, 4, 5]))

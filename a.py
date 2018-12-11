def super_size(n):
    lista = list(str(n))
    lista.sort(reverse = True)
    for liczba in lista:
        print(liczba)
    liczba = int("".join(lista))
    print(liczba)
    print(liczba*2)

super_size(1234)

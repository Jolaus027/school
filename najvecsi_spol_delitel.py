prve_cislo = int(input("1: "))
druhe_cislo = int(input("2: "))
zvysok = 100

while zvysok != 0:

    if druhe_cislo > prve_cislo:

        prve_cislo,druhe_cislo = druhe_cislo,prve_cislo

    zvysok = prve_cislo%druhe_cislo

    prve_cislo = druhe_cislo
    druhe_cislo = zvysok


print(f"Najvacsi spolocny delitel je {prve_cislo}")
terminal = input("Zadaj binarne cislo: ")

spravne_c = ""
konvertuj = True
decimalne_c = 0

for cislo in terminal:

    if cislo.isdigit():

        if cislo == "1" or cislo == "0":

         spravne_c += cislo

        else:
            
            print("Toto neni binarne cislo buzerant!")
            break

    else:

        print("Tak su kokot uz!?") 
        konvertuj = False
        break

spravne_c = spravne_c[::-1]

print(spravne_c)

index = -1
for i in spravne_c:

    index += 1
    

    if i == "1":

        i = int(i)
        decimalne_c += (i * 2)**index


print(decimalne_c)


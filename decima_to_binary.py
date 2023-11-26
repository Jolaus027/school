terminal = input("Zadaj decimalne cislo: ")

spravne_c = ""
konvertuj = True
binarne_c = ""

#toto len kontruluje ci si zadal len cisla a nie nejake ine sracky cislo sa zapise do spravne_c
for cislo in terminal:

    if cislo.isdigit():

         spravne_c += cislo

    else:

        print("Tak su kokot uz!?") 
        konvertuj = False
        break

spravne_c = int(spravne_c)

print(spravne_c)


while spravne_c > 0 and konvertuj == True:

    if spravne_c % 2 == 0:
        
        binarne_c += "0"

    else:

        binarne_c += "1"

    spravne_c = spravne_c // 2


print(binarne_c[::-1])



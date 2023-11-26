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

#while cyklus ide az pokial cislo uz neni viac delitelne dvomi
#alebo pokial uz je teda to cislo 0.5 alebo take daco

while spravne_c > 0 and konvertuj == True:

    #ak je cislo delitelne dvoma bez zvysku tak sa zapise 0
    if spravne_c % 2 == 0:
        
        binarne_c += "0"

    else:

        binarne_c += "1"

    #tu sa deli cislo a vide cislo bez zvysku
    spravne_c = spravne_c // 2

#napise ten string odzadu je to definovane v tych hranatych zatvorkach

print(binarne_c[::-1])



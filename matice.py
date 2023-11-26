import random

pocet_matic = int(input("Pocet matic: "))
def matica_fun(pocet):
    matica1 = []
    temp = []

    for i in range(pocet):

        for p in range(pocet):

                temp.append(random.randrange(10))

        matica1.append(temp)
        temp = []

    return(matica1)


matica1 = matica_fun(pocet_matic) 
matica2 = matica_fun(pocet_matic)


def sum(pocet):
     
    matica_sum = []
    temp = []

    for i in range(pocet):

        for p in range(pocet):

            temp.append(matica1[i][p] + matica2[i][p])

        matica_sum.append(temp)
        temp = []

    return(matica_sum)       
  

def multi(pocet):
     
    matica_multi = []
    temp = []

    for i in range(pocet):

        for p in range(pocet):

            temp.append(matica1[i][p] * matica2[i][p])

        matica_multi.append(temp)
        temp = []

    return(matica_multi)       
  

print("\nMATICA 1")
for i in matica1:
    print(i)

print("\nMATICA 2")
for p in matica2:
    print(p)

print("\nSUCET MATIC")
for z in (sum(pocet_matic)):
    print(z)

print("\nNASOBENIE")
for g in (multi(pocet_matic)):
    print(g)
     
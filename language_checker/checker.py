import csv 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letter_index_sorted = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]
letter_index_unsorted = []
data = []
vysledok = [["English",0],["French",0],["German",0],["Czech",0],["Slovak",0]]
has_letter = False




while has_letter == False:

    input_text = str.lower(input("Write: "))

    for element in input_text:

        if element.isalpha():

            has_letter = True

    if has_letter == False:

        print("You didn't entered any letters")




for alphabet_letter in alphabet:

    for input_letter in input_text:

        if alphabet_letter == input_letter:

            letter_index_unsorted.append(input_letter)





def fun_sort_index(letter_index_unsorted,letter_index_sorted):

    for i in range(len(letter_index_sorted)):

        for letter in letter_index_unsorted:

            if letter_index_sorted[i][0] == letter:

                letter_index_sorted[i][1] += 1




def fun_percent_index(letter_index_sorted):
    for index in range(len(letter_index_sorted)):

        temp = letter_index_sorted[index][1]
        letter_index_sorted[index][1] -= temp
        letter_index_sorted[index][1] += round(temp/len(letter_index_unsorted)*100, 2)








def fun_data(data):


    
    for number in range(5):

        temp = []

        with open('pomery.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            for row in reader:

                temp.append(float(row[number]))

        data.append(temp)

    


input_data = letter_index_sorted


def fun_compare(data, input_data, vysledok):

    for number in range(len(data)):

        for inner_number in range(len(input_data)):

            data[number][inner_number] = round((abs(data[number][inner_number] - input_data[inner_number][1])),2)
            vysledok[number][1] += data[number][inner_number]



fun_sort_index(letter_index_unsorted,letter_index_sorted)
fun_percent_index(letter_index_sorted)
fun_data(data)
fun_compare(data,input_data,vysledok)



write = min(vysledok, key=lambda x: x[1])
print("Your text is in",write[0])




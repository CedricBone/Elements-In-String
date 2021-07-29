#Enter a string and the program will find any of the elemenet symbols in that string 

import json

#lods in the periodic_table.json file as pt
with open('periodic_table.json') as file:
    pt = json.load(file)

# creates an empty list called symbolList
symbolList = []

#loops through every element in pt 
for element in pt['elements']:
    symbol = element['symbol']
    #fills symbol list with all of the element symbols
    symbolList.append(symbol)


userString = input("Enter your text here: ")

#This function returns a list of the user entered string, with each element having a unique element symbols in the given string bolded
def uniqueSymbols(uString):
    nameList = []
    for symbol in symbolList:
        start = 0
        for end in range(len(symbol), len(uString)):
            if (symbol.lower() == uString[start:end].lower()):
                nameList.append(uString[:start] + '\033[92m' + '\033[1m' + uString[start:end].upper() + '\033[0m' + uString[end:])
            else:
                start += 1
    return nameList

for output in uniqueSymbols(userString):
    print(output)


    




#This function will take in the user inputted string and findout if the an Element Symbol is present

"""projekt_1.1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Rossmanith
email: rossmanith.tomas@email.cz
discord: tomasrossmanith
"""





TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# Users table

ohraniceni = "+" + 7 * "-" + "+" + 13 * "-" + "+"
print(ohraniceni)
print("|  user |   password  |")
print(ohraniceni)
print("|  bob  |     123     |")
print("|  ann  |   pass123  |")
print("|  mike | password123 |")     
print("|  liz  |   pass123   |")  
print(ohraniceni) 
ohraniceni_carka = "-" * 40
print(ohraniceni_carka)




# Variables

users = ["bob", "ann", "mike", "liz"]

passwords = ["123", "pass123", "password123", "pass123"]

name = input("User name:")

words_1 = TEXTS[0].split()

words_2 = TEXTS[1].split()

words_3 = TEXTS[2].split()

occurancy_1 = [len(slovo) for slovo in TEXTS[0].split() if slovo.strip(","".")]

occurancy_dict_1 = {}

occurancy_2 = [len(slovo) for slovo in TEXTS[1].split() if slovo.strip(","".")]

occurancy_dict_2 = {}

occurancy_3 = [len(slovo) for slovo in TEXTS[2].split() if slovo.strip(","".")]

occurancy_dict_3 = {}


# Text analyzer

if name in users:
    password = input("Password:")
    if password in passwords:
        print("Welcome to the app", name)
        print("We have 3 texts to be analyzed.")
        print(ohraniceni_carka)
        
        
        analyz_number = input("Enter a number btw. 1 and 3 to select:")
        
        
        if analyz_number.isalpha():
            print("Terminating the program..")
        elif int(analyz_number) <= 3:
            if int(analyz_number) == 1:
                text_1_words = len(TEXTS[0].split(" "))
                print("There are", text_1_words, "words in the selected text.")
                text_1_words_title = sum(1 for word in words_1 if word[0].isupper())
                print("There are", text_1_words_title, "titlecase words.")
                text_1_words_upper = sum(1 for word in words_1 if word[:].isupper and word.isalpha())
                print("There are", text_1_words_upper, "uppercase words.")
                text_1_words_lower = sum(1 for word in words_1 if word[0].islower())
                print("There are", text_1_words_lower, "lowercase words.")
                text_1_words_num = sum(1 for word in words_1 if word[:].isnumeric())
                print("There are", text_1_words_num, "numeric strings.")
                text_1_sum_all_numbers = sum(int(word) for word in words_1 if word.isdigit())
                print("The sum of all the numbers", text_1_sum_all_numbers)
                for values in occurancy_1:
                    if values not in occurancy_dict_1:
                        occurancy_dict_1[values] = 1
       
                    else:
                        occurancy_dict_1[values] =  occurancy_dict_1[values] + 1

                import matplotlib.pyplot as plt

                # Sort items by word length
                sorted_occurancy = [sorted(occurancy_dict_1.values())]
                
                # Data for graph
                lenght_words = list(occurancy_dict_1.keys())

                occurancy_words = list(occurancy_dict_1.values())

                # Graph rendering
                plt.bar(lenght_words, occurancy_words, color = "blue")
                plt.xlabel("Lenght words")
                plt.ylabel("Occurancy words")
                plt.title("Frequency of different word")
                plt.grid(axis="y")
                
                # Graph display
                plt.show()
            elif int(analyz_number) == 2:
                text_2_words = len(TEXTS[1].split(" "))
                print("There are", text_2_words, "words in the selected text.")
                text_2_words_title = sum(1 for word in words_2 if word[0].isupper())
                print("There are", text_2_words_title, "titlecase words.")
                text_2_words_upper = sum(1 for word in words_2 if word[:].isupper and word.isalpha())
                print("There are", text_2_words_upper, "uppercase words.")
                text_2_words_lower = sum(1 for word in words_2 if word[0].islower())
                print("There are", text_2_words_lower, "lowercase words.")
                text_2_words_num = sum(1 for word in words_2 if word[:].isnumeric())
                print("There are", text_2_words_num, "numeric strings.")
                text_2_sum_all_numbers = sum(int(word) for word in words_2 if word.isdigit())
                print("The sum of all the numbers", text_2_sum_all_numbers)
                for values in occurancy_2:
                    if values not in occurancy_dict_2:
                        occurancy_dict_2[values] = 1
       
                    else:
                        occurancy_dict_2[values] =  occurancy_dict_2[values] + 1
                
                import matplotlib.pyplot as plt

                # Sort items by word length
                sorted_occurancy = [sorted(occurancy_dict_2.values())]
                
                # Data for graph
                lenght_words = list(occurancy_dict_2.keys())

                occurancy_words = list(occurancy_dict_2.values())

                # Graph rendering
                plt.bar(lenght_words, occurancy_words, color = "blue")
                plt.xlabel("Lenght words")
                plt.ylabel("Occurancy words")
                plt.title("Frequency of different word")
                plt.grid(axis="y")
                
                # Graph display
                plt.show()
            elif int(analyz_number) == 3:
                text_3_words = len(TEXTS[2].split(" "))
                print("There are", text_3_words, "words in the selected text.")
                text_3_words_title = sum(1 for word in words_3 if word[0].isupper())
                print("There are", text_3_words_title, "titlecase words.")
                text_3_words_upper = sum(1 for word in words_3 if word[:].isupper and word.isalpha())
                print("There are", text_3_words_upper, "uppercase words.")
                text_3_words_lower = sum(1 for word in words_3 if word[0].islower())
                print("There are", text_3_words_lower, "lowercase words.")
                text_3_words_num = sum(1 for word in words_3 if word[:].isnumeric())
                print("There are", text_3_words_num, "numeric strings.")
                text_3_sum_all_numbers = sum(int(word) for word in words_3 if word.isdigit())
                print("The sum of all the numbers", text_3_sum_all_numbers)
                for values in occurancy_3:
                    if values not in occurancy_dict_3:
                        occurancy_dict_3[values] = 1
       
                    else:
                        occurancy_dict_3[values] =  occurancy_dict_3[values] + 1
                
                import matplotlib.pyplot as plt

                # Sort items by word length
                sorted_occurancy = [sorted(occurancy_dict_3.values())]
                
                # Data for graph
                lenght_words = list(occurancy_dict_3.keys())

                occurancy_words = list(occurancy_dict_3.values())

                # Graph rendering
                plt.bar(lenght_words, occurancy_words, color = "blue")
                plt.xlabel("Lenght words")
                plt.ylabel("Occurancy words")
                plt.title("Frequency of different word")
                plt.grid(axis="y")
                # Graph display
                plt.show()
                
            else:   
                print("Terminating the program..")
        else:
            print("Terminating the program..")
    else:
        print("Unregistered password, terminating the program..")
else:
    print("Unregistered user, terminating the program..")

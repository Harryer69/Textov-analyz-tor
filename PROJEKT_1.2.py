"""projekt_1.2.py: první projekt do Engeto Online Python Akademie
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
print("|  ann  |   pass123   |")
print("|  mike | password123 |")     
print("|  liz  |   pass123   |")  
print(ohraniceni) 
ohraniceni_carka = "-" * 40
print(ohraniceni_carka)

# Users and passwords

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


# Login user

while True:
    username = input("User name: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        break
    else:
        print("Unregistered user or password, terminating the program..")

# Text analyz

print(ohraniceni_carka)
print("Welcome to the app", username)
print("We have 3 texts to be analyzed.")
print(ohraniceni_carka)

analyze_number = input("Enter a number btw. 1 and 3 to select:")


if analyze_number.isalpha():
    print("Terminating program...")
elif int(analyze_number) > 3:
    print("Terminating program...")
elif int(analyze_number) > 0 and int(analyze_number) <= (len(TEXTS)):
        selected_text = TEXTS[int(analyze_number)-1]
        
        import re
        
        words = re.findall(r"\b[a-zA-Z0-9]+\b", selected_text) 

        print("There are", len(words), "words in the selected text.")
        print("There are", sum(1 for word in words if word[0].istitle()), "titlecase words.")
        print("There are", sum(1 for word in words if word[:].isupper() and word[:].isalpha()), "uppercase words.")
        print("There are", sum(1 for word in words if word[0].islower()), "lowercase words.")
        print("There are", sum(1 for word in words if word[:].isdigit()), "numeric strings.")
        print("The sum of all the number", sum(int(word) for word in words if word[:].isdigit()))

# Graph display

        word_lengths = [len(word) for word in words]
        
        lengh_freq = {}

        for frequency in word_lengths:
            if frequency not in lengh_freq:
                lengh_freq[frequency] = 1
            else:
                lengh_freq[frequency] = lengh_freq[frequency] + 1

        for length in sorted(lengh_freq.keys()):
            bar = '*' * lengh_freq[length]
            print(f'{length:2}|{bar:<20}|{lengh_freq[length]}') 


       


             

    
    
    
        
   
        
    
   

      
    


    







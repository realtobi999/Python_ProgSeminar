##############################################################
### Základní verze - vždy stejná odpověď

import random
import time
import datetime

first_name = input("Enter fist name: ")
last_name = input("Enter last name: ")

print(f"Hello {last_name} {first_name}")

##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

greetings = (
    f"Good Day! {first_name} {last_name}.",
    f"Hi! {first_name} {last_name}.",
    f"Nice to meet you! {first_name} {last_name}.",
)

print(random.choice(greetings))

##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

random.seed(time.time())

print(random.choice(greetings))

##############################################################
### Verze - pozdrav podle denní doby

current_hour = datetime.datetime.now()

if current_hour.hour > 0 and current_hour.hour <= 12:
    print(f"Good Morning! {first_name} {last_name}")
elif current_hour.hour > 12 and current_hour.hour <= 18:
    print(f"Good Evening! {first_name} {last_name}")
elif current_hour.hour > 18 and current_hour.hour <= 24:
    print(f"Good Night! {first_name} {last_name}")
else:
    print("ERROR! Invalid time.") 
    

import random
import time
import datetime
from iridis import print_title, print_error

print_title("[*] 01 - Greeting Basics\n")

first_name = input("[*] Enter fist name: ")
last_name = input("[*] Enter last name: ")

print(f"[*] Hello {last_name} {first_name}")

greetings = (
    f"Good Day! {first_name} {last_name}.",
    f"Hi! {first_name} {last_name}.",
    f"Nice to meet you! {first_name} {last_name}.",
)

print(f"[*] {random.choice(greetings)}")

random.seed(time.time())

print(f"[*] {random.choice(greetings)}")

current_hour = datetime.datetime.now()

if current_hour.hour > 0 and current_hour.hour <= 12:
    print(f"[*] Good Morning! {first_name} {last_name}")
elif current_hour.hour > 12 and current_hour.hour <= 18:
    print(f"[*] Good Evening! {first_name} {last_name}")
elif current_hour.hour > 18 and current_hour.hour <= 24:
    print(f"[*] Good Night! {first_name} {last_name}")
else:
    print_error("ERROR! Invalid time.")

import numbers
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()<>/?."

all = lower + upper + number + symbol

length = int(input("How long do you want the password to be: "))

password = "".join(random.sample(all, length))

print(password)
#generate password of n length whicch should be random.
import random
import string
char_values=string.ascii_letters+string.digits+string.punctuation
n=int(input("enter how many digits password you need: "))
pw=""
for i in range(n):
    pw+=(random.choice(char_values))
print(f"your random password of {n} length is {pw}")

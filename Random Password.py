import random 
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 8

password = "".join(random.sample(total, length))

print(password)
import random

elements="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pas=""
lin=int(input("Дина пороля: "))
for i in range(lin):
    pas+=random.choice(elements)
print(pas)

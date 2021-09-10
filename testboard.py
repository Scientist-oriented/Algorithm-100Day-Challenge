a = "DOG"
b = "DOL"

a1 = filter(lambda x: x not in b, a)
print(list(a1))
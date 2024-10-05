nana = int(input("How many number would you :"))
nanas= []

for i in range(nana):
    ask = input("number?: ")
    nanas.append (ask)

print(nanas)


for nana in nanas:
    if nana > "0":
        print(nana + "positive")
    elif nana < "0":
        print (nana + "negative")
    else:
        print("error")
    
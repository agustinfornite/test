#Introducir una letra y ver si es consonante o vocal
letra=input("Dame una letra").lower()
if letra in "aeiou":
    print("vocal")
else:
    print("consonante")   
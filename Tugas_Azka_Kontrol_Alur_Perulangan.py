print("Bilangan Ganjil dan Genap")
angka = 1
while angka <= 50 : 
    if angka % 2 == 0 :
        print(f"Angka {angka}  bilangan genap")
    else:
        print(f"Angka {angka}  bilangan ganjil")
    angka += 1
print("\nEnd Program")

#Bilangan Prima

print("bilangan prima dari 1-100")
for angka in range(1, 101):
    pembagi = 0
    for i in range(1,101) :
        if angka % i == 0:
            pembagi += 1
    if pembagi == 2:
        print(f"Angka {angka} adalah bilangan prima")
    else : 
        print(f"Angka {angka} bukan bilangan prima")
print("\nEnd Program")
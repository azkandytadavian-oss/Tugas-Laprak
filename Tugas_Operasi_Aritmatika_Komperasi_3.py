p = panjang = 12 
l = lebar = 5 
t = tinggi = 8 

print("A. Luas, Volume, dan Keliling")

print("1. Luas") #Mencetak data string
hasil = 2 * ( p * l + p * t + l * t) 

print(hasil) #Mencetak hasil
 
print("2. Volume") #Mencetak data string
hasil = p * l * t 

print(hasil) 

print("3. Keliling") #Mencetak data string
hasil = 4 * (p + l + t) 
print(hasil) #Mencetak hasil

#soal b
p = panjang = 12 
l = lebar = 5 
t = tinggi = 8 

print("B. Luas bangunan lebih dari 50") #Mencetak data string
Luas = 2 * ( p * l + p * t + l * t) 
hasil = Luas > 50 #Variabel hasil
print(hasil) #Mencetak hasil

#soal c 
p = panjang = 12 
l = lebar = 5 
t = tinggi = 8 

print("C. Volume sama dengan 480") 
Volume = p * l * t 
hasil = Volume == 480 
print(hasil) 

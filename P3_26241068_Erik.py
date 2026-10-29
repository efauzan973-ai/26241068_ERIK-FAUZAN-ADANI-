#input_output

nama = input("masukan nama anda:")
nim = input("masukan nim anda:")
alamat = input("masukan alamat anda:")

print("========output========")
print("nama anda :",nama )
print("nim anda :",nim)
print("alamat anda :",alamat)

#data

#tipe data interger, bilangan bulat
a = 10
print("nilai a :", a)
print("tipe data a :", type(a))

# tipe data string, tulisan
b = "f"
print("nilai b :", b)
print("tipe data b :", type(b))

# tipe data float, bilangan pecahan
c = 10.5
print("nilai c :", c)
print("tipe data c :", type(c))

# tipe data bolean
d = True
print("nilai d :", d)
print("tipe data d :", type(d))

# Latihan tugas 3
# Mata kuliah: pemrograman dasar
# Materi: variabel dan input data pengguna

print("=======================================")
print("        IDENTITAS MAHASISWA")
print("=======================================")
      
nama = input("masukan nama anda:")
nim = int(input("masukan nim anda:"))
prodi = input("masukan prodi anda:")
dua_digit_terakhir_nim = int(input("masukan 2 digit nim anda:"))

print("=================================")
print("         HASIL PROGRAM")
print("=================================")

print("nama anda         :", nama)
print("nim anda          :", nim)
print("prodi anda        :", prodi)
print("dua 2 nim anda    :", dua_digit_terakhir_nim )

print("tipe data nama:", type(nama))
print("tipe data nim:", type(nim))
print("tipe data prodi:", type(prodi))
print("tipe data 2 digit nim:", type(dua_digit_terakhir_nim))
# # PR pertama buat input masukkan angka, soalnya:
"""
   1. ----0++++5----8++++11---- 
   2. ++++0----5++++8----11++++
"""
# # Menjawab soal no 1
# # ----0++++5----8++++11----

inputdata = float(input("Masukkan Data: "))

Angka1 = inputdata > 0 and inputdata < 5
print("Data diantara 0 dan 5  =",Angka1)

Angka2 = inputdata > 8 and inputdata < 11
print("Data diantara 8 dan 11 =",Angka2)

Hasilnya = Angka1 or Angka2
print("Nilai:", Hasilnya)

# # Menjawab soal no 2
# # ++++0----5++++8----11++++
print("\n",10*"=","\n")

inputdata = float(input("Masukkan Data: "))

Angka1 = inputdata < 0 or inputdata > 11
print("Data < 0 atau > 11     =", Angka1)

Angka2 = inputdata > 5 and inputdata < 8
print("Data diantara 5 dan 8  =", Angka2)

Hasilnya = Angka1 or Angka2
print("Nilai:",Hasilnya)



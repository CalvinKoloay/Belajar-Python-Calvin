# latihan konversi satuan temperature

# program koversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin adalah", kelvin, "Kelvin")

## PR BUAT FAHRENHEIT KE KELVIN DAN KELVIN KE FAHRENHEIT

# FAHRENHEIT KE KELVIN
fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("suhu adalah", fahrenheit, "Fahrenheit")

kelvin = (5/9 * (fahrenheit - 32)) + 273.15
print("suhu dalam Kelvin adalah", kelvin, "Kelvin")

# KELVIN KE FAHRENHEIT
kelvin = float(input("Masukkan suhu dalam kelvin : "))
print("suhu adalah", kelvin, "Kelvin")

fahrenheit = (9/5 * (kelvin - 273.15)) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")


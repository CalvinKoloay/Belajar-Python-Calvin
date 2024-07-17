# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus %
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor divison //
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi, operational precedence

"""
    Urutan operasi :
    1. ()
    2. Eksponen **
    3. Perkalian dan teman-teman * / ** % //
    4. Pertambahan dan pengurangan + -
"""
x = 1
y = 2
z = 3

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)

# kurung dioperasikan paling pertama
hasil = (x + y) * z
print("(",x,'+',y,') *',z, '=', hasil)



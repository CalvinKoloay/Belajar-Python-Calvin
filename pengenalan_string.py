data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..." 
"""

data = "Menggunakan single quote"
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('ayok jalan hari jum\'at')
print('g\'day,  isn\'t it?')

# backlash
print("C:\\user\\calvin")

# tab
print("ini\tberjarak")

# backspace
print("ini \bnempel")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return

# 3. string literal atau raw

# hati-hati
print("C:\new folder") # akan salah pathnya

# menggunakan raw string
print(r"C:\new folder")

# multiline literal string
print("""
Nama    : Calvin
Umur    : 21 Tahun
""")

# multiline literal string dan raw
print("""
Nama    : Calvin
Umur    : 21 Tahun
Website : www.calvin.com/contoh
""")

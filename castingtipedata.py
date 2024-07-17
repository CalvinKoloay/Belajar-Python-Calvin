# Kita belajar casting
# casting = merubah dari satu tipe data ke tipe lain
# tipe data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 8
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
print("data = ", data_float, ",type = ", type(data_float))

data_str = str(data_int)
print("data = ", data_str, ",type = ", type(data_str))

data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_bool, ",type = ", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 8.8
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float) # akan dibulatkan kebawah
print("data = ", data_int, ",type = ", type(data_int))

data_str = str(data_float)
print("data = ", data_str, ",type = ", type(data_str))

data_bool = bool(data_float) # akan false jika nilai int = 0
print("data = ", data_bool, ",type = ", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False
print("data = ", data_bool, ",type = ", type(data_bool))

data_int = int(data_bool) # True = 1, False = 0
print("data = ", data_int, ",type = ", type(data_int))

data_str = str(data_bool) 
print("data = ", data_str, ",type = ", type(data_str))

data_float = float(data_bool) # True = 1,0, False = 0,0
print("data = ", data_float, ",type = ", type(data_float))

## STRING
print("====STRING====")
data_str = "11"
print("data = ", data_str, ",type = ", type(data_str))

data_int = int(data_str) # string harus angka
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_str) # string harus angka
print("data = ", data_float, ",type = ", type(data_float))

data_bool = bool(data_str) # false jika string kosong
print("data = ", data_bool, ",type = ", type(data_bool))
# operasi aritmatika

a = 10
b = 3

# operasi penjumlahan (TAMBAH)
print("====TAMBAH====")
hasil = a + b
print(a,"+", b, "=",hasil)

# operasi pengurangan (KURANG)
print("====KURANG====")
hasil = a - b
print(a,"-", b, "=",hasil)

# operasi perkalian (KALIH)
print("====KALIH====")
hasil = a * b
print(a,"*", b, "=",hasil)

# operasi pembagian (BAGI)
print("====KURANG====")
hasil = a / b
print(a,"/", b, "=",hasil)

# operasi pemankatan (exponetiol)
print("====PANGKAT====")
hasil = a ** b
print(a,"**", b, "=",hasil)

# operasi sisa pembagian (MODULUS)
print("====MODULUS====")
hasil = a % b
print(a,"%", b, "=",hasil)

# operasi floor devision
print("====FLOOR DECISION====")
hasil = a // b
print(a,"//", b, "=",hasil)

# prioritas perhitungan (operasi)
"""
     1. ()
     2.perkalian,pembagian,dll * / ** % //
     3.penjumlahan dan pengurangan =
     + -
"""
x = 3
y = 4
z = 2

hasil = x**z * (y + x) / z-z % y // x
print(x,"**",z,"*", y, "+", x, "/", z, "-",z, "%",y, "//", x,"=",hasil)

hasil = x + y * z
print(x, "+",y, "*", z, "=",hasil)
hasil = (x + y) * z
print("(",x, "+", y,")", "*", z, "=",hasil)
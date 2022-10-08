# Ejercicio 3:
print("-------------------------")
print("--- SERIE - FIBONACCI ---")
print("-------------------------")

#Input
a = 0
b = 1
c = a + b

#Processing
while c < 10000:
    print (c)
    a = b
    b = c
    c = a + b
print("Programa terminado")
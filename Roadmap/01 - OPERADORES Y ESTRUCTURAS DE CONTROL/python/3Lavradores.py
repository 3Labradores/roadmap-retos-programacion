#Operadores aritmeticos 
a1 = 1+3
a2 = 8-4
a3 = 8*3
a4 = 56/9
a5 = 56%12
a6 = 123//34

print(a1, a2, a3, a4, a5, a6,)

#Operadores asignacion

b1 = 2
print(b1)
b1 += 3
print(b1)
b1 -=1
print(b1)
b1 *= 3
print(b1)
b1 **= 3
print(b1)
b1 /= 2
print(b1)
b1 //= 3
print(b1)
b1 %= 10
print(b1)

#Operadores logicos

c1 = 13
print("El valor de la variable c1 es", c1)
if c1 == b1 :
 print("La variable b1 y c1 tienes el mismo valor")
elif c1 < b1 :
 print("La variable c1 es menor a la variable b1")
elif c1 > b1 :
 print("La variable c1 es mayor a la variable b1")
elif c1 <= b1 :
 print("Que sorpresa")
elif c1 >= b1 :
 print("No me esperaba esto")
elif c1 == b1 :
 print(" c1 y b1 tienes valores iguales en este momento")

 #Operadores Logicos

if a3 < a4 and b1 >= c1 :
  print(True)
elif a3 < a4 or b1 >= c1:
 print(False)
elif not a3 <= a4  :
 print("Supongo que no")


#Operadores de identidad

resultado = None

if resultado is None:
    print("No hay resultados")

elif resultado is not None:
    print("Se encontró información")

#Operadores de pertenencia

d1 = [1,2,3,4,5,6]

if 2 in d1:
  print("El numero 2 se encuentra en la lista d1")
if 7 not in d1:
  print("Elnumero 7 no se encuentra en la lista d1")
print("Los valores de d1 son:", d1)


#Operadores bit a bit(bitwise)

# Definimos permisos como potencias de 2
LEER = 1       # 001
ESCRIBIR = 2   # 010
EJECUTAR = 4   # 100

# 1. Asignar permisos usando OR (|)
permisos = LEER | ESCRIBIR  # 001 | 010 = 011 (3)

# 2. Verificar si tiene un permiso usando AND (&)
puede_escribir = (permisos & ESCRIBIR) != 0  # True
puede_ejecutar = (permisos & EJECUTAR) != 0  # False

# 3. Alternar (activar/desactivar) un permiso usando XOR (^)
permisos ^= EJECUTAR  # Ahora tiene LEER, ESCRIBIR y EJECUTAR (111 = 7)
permisos ^= EJECUTAR  # Si lo vuelves a ejecutar, le quita EJECUTAR (011 = 3)

numero = 6  # Binario: 110

# Multiplicar por 2 (desplazar 1 lugar a la izquierda)
print(numero << 1)  # 12 (Binario: 1100)

# Multiplicar por 4 (desplazar 2 lugares a la izquierda: 6 * 2^2)
print(numero << 2)  # 24 (Binario: 11000)

# División entera entre 2 (desplazar 1 lugar a la derecha)
print(numero >> 1)  # 3  (Binario: 11)

estado = 0b1010  # 10 en decimal
mascara = 0b0010 # Queremos cambiar el segundo bit

estado = estado ^ mascara  # Resultado: 0b1000 (8) - Apagado
estado = estado ^ mascara  # Resultado: 0b1010 (10) - Encendido de nuevo


numeros = [4, 1, 2, 1, 2]
unico = 0
for n in numeros:
    unico ^= n
print(unico)

mensaje = 42
clave = 123

cifrado = mensaje ^ clave      # 81
descifrado = cifrado ^ clave 

permisos = 0b1111  # Todos los permisos activos (15)
borrar = 0b0010    # Bit que queremos apagar (2)

# ~borrar invierte los bits a ...11111101
permisos = permisos & ~borrar
print(bin(permisos))

letras = ['a', 'b', 'c', 'd']
i = 0

print(letras[i])   # 'a' (primero)
print(letras[~i])  # 'd' (último, porque ~0 es -1)

#Reto OPcional


list = []
for i in range(10, 56, 2):
 list.append(i)
 print(i)  
 if i %3 == 0:
  list.remove(i)
list.remove(16)
list.append(55)
print (list) 

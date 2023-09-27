#definir variables primitivas 
texto = "hola soy Esteban"
entero  = 4
flotante= 3.1416
#concatenar 
concatenacion=texto + " " + str(entero) + " " + str(flotante)
# Los enteros en Python tienen un límite superior dependiendo de la arquitectura del sistema. Puedes verificar el límite en tu sistema con sys.maxsize.
# Para los flotantes, Python utiliza el estándar IEEE 754 de 64 bits para números de punto flotante, lo que proporciona una precisión de aproximadamente 15-17 dígitos decimales.

# fórmula de la suma de los primeros n números pares
n = int(input("Ingrese un valor entero para n: ")) 
suma_numeros_pares = n * (n + 1)

print(entero)
print(texto)
print(flotante)
print(concatenacion)
print(suma_numeros_pares)




def saludo(nombre):

  print(f"Hola, {nombre}!")

def suma(a, b):
  
  return a + b

def area_rectangulo(base, altura):
  
  return base * altura

def par_impar(numero):
  
  return "Par" if numero % 2 == 0 else "Impar"

def celsius_a_fahrenheit(celsius):
  
  return (celsius * 9/5) + 32

def maximo_tres_numeros(a, b, c):
  
  return max(a, b, c)

def palindromo(cadena):
  
  cadena = cadena.lower()
  return cadena == cadena[::-1]

def factorial(numero):
  
  return 1 if numero == 0 else numero * factorial(numero - 1)

def contar_vocales(cadena):
  
  vocales = "aeiouAEIOU"
  return sum(1 for letra in cadena if letra in vocales)

def numero_primo(numero):
  
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

while True:
  print("\nMenú de Funciones:")
  print("1. Saludo")
  print("2. Suma")
  print("3. Área de un Rectángulo")
  print("4. Número Par o Impar")
  print("5. Conversión de Celsius a Fahrenheit")
  print("6. Máximo de Tres Números")
  print("7. Palíndromo")
  print("8. Factorial")
  print("9. Contar Vocales")
  print("10. Número Primo")
  print("0. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    nombre = input("Ingrese un nombre: ")
    saludo(nombre)
  elif opcion == "2":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print(f"La suma de {a} y {b} es: {suma(a, b)}")
  elif opcion == "3":
    base = int(input("Ingrese la base del rectángulo: "))
    altura = int(input("Ingrese la altura del rectángulo: "))
    print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
  elif opcion == "4":
    numero = int(input("Ingrese un número: "))
    print(f"El número {numero} es: {par_impar(numero)}")
  elif opcion == "5":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print(f"{celsius} grados Celsius equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")
  elif opcion == "6":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    print(f"El máximo de {a}, {b} y {c} es: {maximo_tres_numeros(a, b, c)}")
  elif opcion == "7":
    cadena = input("Ingrese una cadena: ")
    print(f"La cadena '{cadena}' {'es' if palindromo(cadena) else 'no es'} un palíndromo")
  elif opcion == "8":
    numero = int(input("Ingrese un número: "))
    print(f"El factorial de {numero} es: {factorial(numero)}")
  elif opcion == "9":
    cadena = input("Ingrese una cadena: ")
    print(f"La cadena '{cadena}' tiene {contar_vocales(cadena)} vocales")
  elif opcion == "10":
    numero = int(input("Ingrese un número: "))
    print(f"El número {numero} {'es' if numero_primo(numero) else 'no es'} un número primo")
  elif opcion == "0":
    break
  else:
    print("Opción inválida.")
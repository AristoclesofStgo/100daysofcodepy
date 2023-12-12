# Este programa nos dice si el tipo de numero que ingresemos es par o impar 

number= int(input("Ingrese el número: \n"))
calculo = number % 2 
if calculo == 0:
  print("This is an even number.")
else: 
  print("This is an odd number.")
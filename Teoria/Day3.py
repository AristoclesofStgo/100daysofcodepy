# Condiciones if / else    
# if condition:
# Haz esto (Cuando es verdadera, o sea que cumple la primera condicion)
# else    
# Haz lo otro (Cuando es falsa y no cumple con la condition) 
# Ejemplo 
print("Bienvenidos al GYM!")
validation = int(input("Ingrese su peso: "))
if validation >= 75: 
  print("Pongase a hacer cardio")
else:
  print("Pongase a darle a los hierros")
  
# Hay que tener pendiente la sangria en todo lo que hacemos,el if y else deben de estar al mismo nivel, de lo contrario nos devolverá un Identationerror 
# Signos de comparacion
# > (Mayor que)
# < (Menor que)
# >= (Mayor o igual que)
# <= (Menor o igual que)
# == (Igual que) Cuando se utiliza = solamente es para asignar el valor a una variable, cuando son dos (==) es para verificar que la condicion de la izquierda se cumpla con la de la derecha, el caso de las condiciones if / else 
# != (Diferente que)

# Nested if and elif: 
# Podemos agregar mas condiciones entre el if y else, esto es lo que se llama nested (anidados) if y elif
# En el nested if, se agrega otra condicion nueva dentro del if que ya esta presente. Ejemplo:
print("Bienvenidos al GYM!")
validation = int(input("Ingrese su peso: "))
if validation >= 75: 
  print("Pongase a hacer cardio")
  age = int(input( "Ingrese su edad: "))
  if age >= 18:
    print("Tienes que pagar: $50")
  else: 
    print("Puedes entrar gratis!")
else:
  print("Pongase a darle a los hierros")

# elif: Nos ayuda a poner mas de dos condiciones, si la primera se cumple, por favor verifica la segunda condicion, si no, verifica la tercera condicion, etc. Se agrega dentro del if/else anidado 
# Ejemplo 
print("Bienvenidos al GYM!")
validation = int(input("Ingrese su peso: "))
if validation >= 60: 
  print("Pongase a hacer cardio")
  age = int(input( "Ingrese su edad: "))
  if age <= 23:
    print("Tienes que pagar: $50")
  elif age <= 16:
    print("No puedes entrar al GYM")
  else: 
    print("Puedes entrar gratis!")
else:
  print("Pongase a darle a los hierros")

# Ejercicio sobre la masa corporal 
print("Ejercicio para conocer tu masa corporal!")
weight = int(input("Ingrese su peso: "))
height = float(input("Ingrese su altura: "))

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25: 
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else: 
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Programa para saber si un año es bisiesto o no (Lógica dificil)
year = int(input("Ingrese un año: "))

if year % 4 == 0: 
  if year % 100 == 0:
    if year % 400 == 0:
      print ("Leap year")
    else: 
      print ("Not leap year")
  else: 
    print ("Leap year")
else: 
  print ("Not leap year")

# Cuando utilizamos if/elif solo se cumple una condicion, si la primera es cierta se pasa la segunda, si queremos que se cumplan todas las condiciones debemos de utilizar diferentes sentencias "if" 
print("Bienvenidos al GYM!")
validation = int(input("Ingrese su peso: "))
pago = 0

if validation <= 70: 
  print("Pongase a darle a los hierros")
  age = int(input( "Ingrese su edad: "))
  if age <= 23:
    pago = 20
    print("Tienes que pagar: $20")
  elif age <= 16:
    pago = 10
    print("Debes pagar $10")
  elif age >= 24:
    pago = 30
    print("Debes pagar $30")
  else:
    print("Bienvenido al GYM!")

  water = input("Quieres agua con la entrada? (S/N): ")
  if water == "S":
    pago += 10
    print(f"Tu pago es de: ${pago}")
else:
  print("Pongase a correr, no le toca hierros")

# Pizzeria La Volanta
print("Bienvenido a la pizzeria La Volanta!")
size = input("Ingrese el tamaño de la pizza: S, M, L: ")
extra = input("Ingrese si quiere pepperoni (S/N): ")
extra2 = input("Ingrese si quiere queso (S/N): ")
price = 0

if size == "S":
  price += 15
elif size == "M":
  price += 20
else:
  price += 25

if extra == "Y":
  if size == "S":
    price += 2
  else:
    price += 3

if extra2 == "Y":
  price += 1

print(f"Your final bill is: ${price}.")

# Podemos utilizar operadores logicos dentro de los if and else statements. para que and sea verdaderos debe de cumplir todas las condiciones y para que or sea verdadero solo debe de cumplir una de las condiciones. Podemos utilizar not antes de la condicion para que cambie el valor de la condicion y lo vuelva falso o viceversa. 
print("Bienvenidos al GYM!")
peso = int(input("Ingrese su peso: "))
pago = 0

if peso <= 70: 
  print("Pongase a darle a los hierros")
  age = int(input( "Ingrese su edad: "))
  if age <= 23:
    pago = 20
    print("Tienes que pagar: $20")
  elif age <= 16:
    pago = 10
    print("Debes pagar $10")
  elif age >= 24:
    pago = 30
  elif age >= 45 or age <= 55:
    pago = 0
    print("Debes pagar $0")
  else:
    print("Bienvenido al GYM!")

  water = input("Quieres agua con la entrada? (S/N): ")
  if water == "S":
    pago += 10
    print(f"Tu pago es de: ${pago}")
else:
  print("Pongase a correr, no le toca hierros")

# Calculadora del amor (Se utiliza el comando .lower() para que convierta el string en minusculas y lo pueda combinar con las palabras true love, y al utilizar .count() en la variables de los nombres en minusculas, se cuentan las letras que hay en el string))
name1 = input("Ingrese el nombre de la esposa ")
name2 = input("Ingrese el nombre del esposo ")
combined_names = name1 + name2
lowercase_names = combined_names.lower()
t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
first_digit = t + r + u + e

l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
second_digit = l + o + v + e

digits =int(str(first_digit) + str(second_digit))

if digits < 10 or digits > 90:
  print(f"Your score is {digits}, you go together like coke and mentos.")
elif digits >= 40 and digits <= 50:
  print(f"Your score is {digits}, you are alright together.")
else:
  print(f"Your score is {digits}.")

# Podemos utilizar \' para poner comillas en un string y \n para poner un salto de linea en un string.
print("Hola, \n ¿como estas?")
print('You\'re amazing!')

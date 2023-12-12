print(len("bonito"))
#Data types 
#Strings: Ponemos el numero entre de los corchetes indicando el primer caracter del String, en este caso la L. Esto se llama subscript. Todo lo que se ponga dentro de las comillas, lo identificará como un String. Ej: "1254"
print("Luis"[0])
#Integers: Son los numeros enteros, si vamos a tratar con miles, se deben separar con _ 
print(1_000_000 + 2_000_000)
#Floats: Son los numeros decimales. Ej: 3.14159 que es pi 
3.14159
#Booleans: Cuando vayamos a indicar si algo es verdadero o falso. Se empieza con la letra mayuscula
True
False 

#No podemos mezclar las cadenas de strings con intergers, de lo contrario, recibimos un TypeError. 
mom_char = len(input("Como se llama tu madre?"))
# print ("El nombre de tu madre tiene" + mom_char + "caracteres")

# Para saber el tipo de datos que tiene una variable, usamos la función type()
print(type(mom_char))

# Podemos cambiar el tipo de datos de una variable a string con el comando str. Ej: (Tambien podemos cambiar el tipo a float() int() y bool() )
new_mom_char = str(mom_char)
print ("El nombre de tu madre tiene " + new_mom_char + " caracteres")

# Operaciones matematicas: En una linea de codigo se hacen en orden jerarquico las operaciones matematicas. Ej: 2 + 2 * 2 Se hacen en base al PEMDAS Parentesis, Exponentes, Multiplicacion, Division, Addicion y Sustraction.
# Suma
print(1 + 2)
# Resta
print(1 - 2)
# Multiplicacion
print(1 * 2)
# Division: Siempre el resultado será una variable float,  
print(1 / 2)
# Division entera
print(1 // 2)
# Potencia
print(2 ** 3)
# Modulo
print(1 % 2)

# Para redondear un float, podemos utilizar la funcion round
print(round(8/3,2))

# Una forma facil de hacer una operacon con el valor actual de una variable es utilizando el simbolo de igual (=) Ej: /= or x= 
result = 4 / 2 
result /= 2
print(result)

# Otro ejemplo: 
score = 1 

# Anotan otro punto 
score += 1
print(score)

#Para ahorrar lineas de codigo, podemos representar diferentes tipos de variables utilizando f strings o cadenas de caracteres, lo cual nos evita estar modificando el tipo de variable a cada una. Ej: 
Nombre = "Luis"
Peso = 72
Altura = 1.4
Soltero = True 
print(f"Mi nombre es: {Nombre} Mi peso es: {Peso} Mi altura es: {Altura} Situacion sentimental, Soltero: {Soltero}")



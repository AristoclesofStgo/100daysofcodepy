#Dia 1 
# La funcion Print, nos muestra en pantalla lo que queramos escribir. Los valores "String" se ponen entre comillas, porque son caracteres (Texto) que no va incluido con el codigo. 

print ("Hello World")

print('Day 1 - Python Print Function')
print("The function is declared like this:")
print("print('what to print')")
#Se utilizan comillas dobles si el texto que queremos de output, tiene signos de puntuacion o caracteres especiales y la linea entera se cambia a comillas simples.

print ("Hello World!\nHello World!")
#Se utiliza el \n para ahorrar escribir el comando de nuevo y tirar en La linea siguiente lo que queremos imprimir

print ("Hello " + "David")
#Se utiliza el + para concatenar dos o mas cadenas de texto. Para añadir un espacio se debe de dejar el espacio despues del texto 
#IndentationError: Es el error que aparece cuando hay algun espacio de mas.
#SyntaxError: Error que aparece cuando faltan comillas en el codigo

print("Hello " + input ("What is your name?"))
#Input es una funcion que nos permite introducir datos por teclado. Se combina con print para que imprima el resultado de los datos introducidos.

name = input("What is your name?")
caracteres = len(name)
print (caracteres)
#len() es una funcion que nos permite saber la cantidad de caracteres que tiene una cadena de texto.Otra forma de hacerlo es: print(len(input("What is your name?")))

name = input ("What is your name?")
print (name)
#Al declarar una variable, le estamos informando al sistema que esa linea tiene un nombre y la podemos utilizar delante en el codigo

a = input ("Ingrese un numero ")
b = input ("Ingrese un numero ")
c = a
a = b
b = c 
print ("a ")
print ("b ")
#Si queremos cambiar de posicion alguna variable, tenemos que declarar una tercera para poder asignarla a la variable que queremos mover y poner reorganizar la variable. Para nombrar una variable, debe de tener el mismo nombre que cuando se esta declarando. 
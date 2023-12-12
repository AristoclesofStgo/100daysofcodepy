# Calcular la masa corporal del cuerpo: MC = peso / altura ^ 2
peso = input("Ingrese su peso: ")
altura = input("Ingrese su altura: ")
peso_int = int(peso)
altura_float = float(altura)
mc = peso_int / altura_float ** 2 
mc_int = int(mc)
print("Su masa corporal es: " + str(mc_int))
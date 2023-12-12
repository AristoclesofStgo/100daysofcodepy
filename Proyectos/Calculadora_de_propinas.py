
print("Bienvenido a la calculadora de propinas")
cuenta = input("Cuanto hizo la cuenta? $")
porciento = input("Cuanto porciento desea darle? 10%, 12% o 15%? ")
personas = input("Cuantas personas son? ")

cuenta_int = float(cuenta)
total_porciento = int(porciento) / 100 * cuenta_int + cuenta_int
total_porciento_fl = float(total_porciento) / int(personas)
total_porciento_fl = round(total_porciento_fl, 2)
total_porciento_fl = "{:.2f}".format(total_porciento_fl)

# Resultado 
total = print(f"Cada persona debe de pagar: ${total_porciento_fl}")


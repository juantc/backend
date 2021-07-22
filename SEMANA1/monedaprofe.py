#Programa para convertir monedas
print("========================")
print("Cambista 1.0")
print("========================")

print("Ingresa el valor en dolares: ")
moneda=float(input())
print("Ingrese la moneda a convertir:")
monedaConvertir=input()

if monedaConvertir=="soles":
    tipoCambio=3.98
elif monedaConvertir=="euros":
    tipoCambi=0.85
else:
    tipoCambio=1
    
valorMonedaConvertir=moneda*tipoCambio

if(valorMonedaConvertir==moneda):
    print("No indico una moneda valida")
else:
    print(" el valor en "+monedaConvertir+" es de "+str(valorMonedaConvertir))
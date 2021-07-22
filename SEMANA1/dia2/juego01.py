#Juego de piedra papel o tijera
#Definir variables de entrada y salida
jugador = input("ingresa tu jugada: ")
computadora="papel"
ganador=""

#Logica de la solucion
if jugador=="piedra":
    if computadora=="piedra":
        ganador="empate"
    elif computadora =="papel":
        ganador="computador"
    elif computadora=="tijera":
        ganador="jugador"
elif jugador=="papel":
    if computadora=="piedra":
        ganador="jugador"
    elif computadora =="papel":
        ganador="empate"
    elif computadora=="tijera":
        ganador="computador"
elif jugador=="tijera":
    if computadora=="piedra":
        ganador="computador"
    elif computadora =="papel":
        ganador="jugador"
    elif computadora=="tijera":
        ganador="empate"
        
#Muestra resultados
print("El ganador es : "+ganador)
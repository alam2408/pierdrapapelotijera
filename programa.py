import random

print("¡Bienvenido al juego de piedra, papel o tijera!")
print("1 = Piedra, 2 = Papel, 3 = Tijera")

opciones = ["Piedra", "Papel", "Tijera"]
jugador = int(input("Elige una opción (1, 2, 3): "))
computadora = random.randint(1, 3)

print("Tu elegiste: ", opciones[jugador-1])
print("La computadora eligió: ", opciones[computadora-1])

if jugador == computadora:
    print("Empate!")
elif jugador == 1 and computadora == 3:
    print("Ganaste!")
elif jugador == 2 and computadora == 1:
    print("Ganaste!")
elif jugador == 3 and computadora == 2:
    print("Ganaste!")
else:
    print("Perdiste!")

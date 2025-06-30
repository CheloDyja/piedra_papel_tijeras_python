
nombre1 = input ("Jugador 1, igrese su nombre: ")
nombre2 = input ("Jugador 2, igrese su nombre: ")

print("Hola", nombre1,"Hola", nombre2,
       """
       Bienvenidos al juego de Piedra, papel  o tijeras
       """)

print("Hola", nombre1, "Empezas vos")

jugador1 = input("Debes elegir una opcion: piedra, papel o tijeras: ")
jugador1 = jugador1.lower()
if jugador1 not in ["piedra", "papel", "tijeras"]:
    print("Opcion invalida")
    jugador1 = input("Debes elegir una opcion: piedra, papel o tijeras: ")

print("Hola", nombre2, "Ahora es tu turno")

jugador2 = input("Debes elegir una opcion: Piedra, papel o tijeras: ")
jugador2 = jugador2.lower()
if jugador2 not in ["piedra", "papel", "tijeras"]:
    print("Opcion invalida")
    jugador2 = input("Debes elegir una opcion: Piedra, papel o tijeras: ")
    
# Piedra gana a tijeras, papel gana a piedra, tijeras gana a papel
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Han empatado")
elif condicion1 or condicion2 or condicion3:
    print("Felicitaciones:", nombre1, "Has ganado la partida")
else:
    print("Felicitaciones:", nombre2, "Has ganado la partida")

# Paso 4: Añadir la opción de jugar de nuevo

jugar_de_nuevo = input("¿Desean jugar de nuevo? (s/n): ").lower()
while jugar_de_nuevo == "s":
    jugador1 = input("Debes elegir una opcion: piedra, papel o tijeras: ")
    jugador1 = jugador1.lower()
    if jugador1 not in ["piedra", "papel", "tijeras"]:
        print("Opcion invalida")
        jugador1 = input("Debes elegir una opcion: piedra, papel o tijeras: ")
    print("Hola", nombre2, "Ahora es tu turno")

    jugador2 = input("Debes elegir una opcion: Piedra, papel o tijeras: ")
    jugador2 = jugador2.lower()
    if jugador2 not in ["piedra", "papel", "tijeras"]:
        print("Opcion invalida")
        jugador2 = input("Debes elegir una opcion: Piedra, papel o tijeras: ")
    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
    if jugador1 == jugador2:
        print("Han empatado")
    elif condicion1 or condicion2 or condicion3:
        print("Felicitaciones:", nombre1, "Has ganado la partida")
    else:
        print("Felicitaciones:", nombre2, "Has ganado la partida")
    jugar_de_nuevo = input("¿Desean jugar de nuevo? (s/n): ").lower()

print("Gracias por jugar, hasta la proxima!")
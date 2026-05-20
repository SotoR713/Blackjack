import random
from Baraja import Mazo

#arreglo que mantiene las cartas repartidas al jugador en la mano actual
MANO=[]

#funcion para repartir una carta al jugador y mostrar el valor actual de la mano
def repartirCarta():
    print("-"*30)
    carta = random.choice(Mazo)
    MANO.append(carta)
    print(f"Carta repartida:  {carta.nombre}{carta.palo}")
    valorMano=calcularValorMano(MANO)
    print(f"Valor actual de la mano: {valorMano}")
    mostrarMano(MANO)
    validarVictoria(valorMano)

#funcion para mostrar la mano actual y su valor total
def mostrarMano(mano):
    print("-"*30)
    print("Mano actual: ")
   
    lineaSuperior = ""
    lineaMedia = ""
    lineaInferior = ""

    for carta in mano:
        sup, med, inf = mostrarCarta(carta)
        lineaSuperior += sup
        lineaMedia += med
        lineaInferior += inf

    print(lineaSuperior)
    print(lineaMedia)
    print(lineaInferior)
    
    valorMano = calcularValorMano(mano)    
    print(f"{valorMano} puntos actuales")
    print("-"*30)


#Funcion principal que corre el juego y muestra el menu
def jugar():
    while True:
        print("\nOpciones:")
        print("1. Repartir carta")
        print("2. Mostrar mano")
        print("3. Mostrar resultado y salir")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            repartirCarta()
        elif opcion == "2":
            mostrarMano(MANO)
        elif opcion == "3":
            mostrarMano(MANO)
            print(f"¡Gracias por jugar! resultado final: {sum(carta.valor for carta in MANO)} puntos")
            MANO.clear()
        elif opcion == "4":
            print("hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

            
#funcion para calcular el valor total de la mano
def calcularValorMano(mano):
    sumatoriaPuntos = sum(carta.valor for carta in mano)
    for carta in mano:
        if carta.nombre == "A" and sumatoriaPuntos + 10 <= 21:
            sumatoriaPuntos += 10

    return sumatoriaPuntos

#funcion para validar si el jugador ha ganado o perdido
def validarVictoria(valorMano):
    if valorMano > 21:
        print("¡Has perdido! El valor de tu mano ha superado los 21 puntos.")
        MANO.clear()
        print("-"*30)
    elif valorMano == 21:
        print("¡Felicidades! Has ganado con un Blackjack.")
        MANO.clear()
        print("-"*30)

#funcion para mostrar una carta en formato visual
def mostrarCarta(carta):
        sup = "┌─────┐ "
        med = f"│ { "" if carta.nombre == "10" else " "  }{carta.nombre}{carta.palo} │ "
        inf = "└─────┘ "
        return sup, med, inf


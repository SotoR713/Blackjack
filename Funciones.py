import random
from Baraja import crearMazo


#funcion para repartir una carta al jugador y mostrar el valor actual de la mano
def repartirCarta(Mazo, manoJugador, manoCasa):
    print("-"*30)
    validarMazoVacio(Mazo)    
    carta = random.choice(Mazo)
    manoJugador.append(carta)
    eliminarCarta(Mazo, carta)
    print(f"Carta repartida:  {carta.nombre}{carta.palo}")
    valorMano=calcularValorMano(manoJugador)
    print(f"Valor actual de la mano: {valorMano}")
    mostrarManoCasaOculta(manoCasa)
    mostrarMano(manoJugador)
    

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
def iniciarJuego():
    manoJugador = []
    manoCasa = []

    while True:
        Mazo = crearMazo()
        print("\nOpciones:")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            termino = repartirCartaPrimero(Mazo, manoJugador, manoCasa)

            if not termino:
                seguirJuego(Mazo, manoJugador, manoCasa)

        elif opcion == "2":
            print("hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def seguirJuego(Mazo, manoJugador, manoCasa):
    while True:
        print("\n¿que deseas hacer?")
        print("1. Repartir carta")
        print("2. Quedarme con mi mano actual")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            repartirCarta(Mazo, manoJugador, manoCasa)
            termino = validarVictoria(
                calcularValorMano(manoJugador), manoCasa, manoJugador
            )
            if termino:
                break

        elif opcion == "2":
            print(
                f"¡Gracias por jugar! resultado final: "
                f"{calcularValorMano(manoJugador)} puntos"
            )
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
def validarVictoria(valorMano,manoCasa,manoJugador):
    if valorMano > 21:
        print("¡Has perdido! El valor de tu mano ha superado los 21 puntos.")
        mostrarMano(manoCasa)
        mostrarMano(manoJugador)
        manoJugador.clear()
        manoCasa.clear()
        print("-"*30)
        return True
    elif valorMano == 21:
        print("¡Felicidades! Has ganado con un Blackjack.")
        manoJugador.clear()
        manoCasa.clear()
        print("-"*30)
        return True
    
    return False    

#funcion para mostrar una carta en formato visual
def mostrarCarta(carta):
        sup = "┌─────┐ "
        med = f"│ { "" if carta.nombre == "10" else " "  }{carta.nombre}{carta.palo} │ "
        inf = "└─────┘ "
        return sup, med, inf



def eliminarCarta(Mazo, carta):
    Mazo.remove(carta)

def repartirCartaPrimero(Mazo, manoJugador, manoCasa):
    print("-"*30)
    carta = random.choice(Mazo)
    manoJugador.append(carta)
    eliminarCarta(Mazo, carta)
    carta = random.choice(Mazo)
    manoJugador.append(carta)
    eliminarCarta(Mazo, carta)
    carta = random.choice(Mazo)
    manoCasa.append(carta)
    eliminarCarta(Mazo, carta)
    carta = random.choice(Mazo)
    manoCasa.append(carta)
    eliminarCarta(Mazo, carta)
    mostrarManoCasaOculta(manoCasa)
    mostrarMano(manoJugador)
    print(f"Valor actual de la mano: {calcularValorMano(manoJugador)}")
    return primeraVictoria(manoJugador, manoCasa)

def primeraVictoria(manoJugador, manoCasa):
    valorMano = calcularValorMano(manoJugador)
    if valorMano == 21:
        print("¡Felicidades! Has ganado con un Blackjack.")
        mostrarMano(manoCasa)
        mostrarMano(manoJugador)
        manoJugador.clear()
        manoCasa.clear()
        print("-"*30)
        return True 
    return False

def mostrarManoCasaOculta(mano):
    if len(mano) == 0:
        return
    print("-"*30)
    print("Mano de la casa: ")
   
    lineaSuperior = ""
    lineaMedia = ""
    lineaInferior = ""

    for carta in mano[:-1]:
        sup, med, inf = mostrarCarta(carta)
        lineaSuperior += sup
        lineaMedia += med
        lineaInferior += inf

    lineaSuperior += "┌─────┐ " 
    lineaMedia +=    "│ ? ? │ " 
    lineaInferior += "└─────┘ " 


    print(lineaSuperior)
    print(lineaMedia)
    print(lineaInferior)
    
def validarMazoVacio(Mazo):
    if len(Mazo) == 0:
        Mazo.clear()
        print("El mazo se ha quedado sin cartas, reiniciando el mazo...")
        Mazo.extend(crearMazo())  
     
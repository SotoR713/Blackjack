import random
from Baraja import crearMazo


#funcion para repartir una carta al jugador y mostrar el valor actual de la mano
def repartirCarta(Mazo, manoJugador, manoCasa):
    print("-"*30)
    validarMazoVacio(Mazo)    
    carta = lanzarCarta(manoJugador, Mazo)
    print(f"Carta repartida:  {carta.nombre}{carta.palo}")
    valorManoJugador=calcularValorMano(manoJugador)
    print(f"Valor actual de la mano: {valorManoJugador}")
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

    while True:
        Mazo = crearMazo()
        manoJugador = []
        manoCasa = []
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
            repartirCartaCasa(Mazo, manoCasa)

            mostrarMano(manoCasa)
            mostrarMano(manoJugador)
            # print(
            #     f"¡Gracias por jugar! resultado final: "
            #     f"{calcularValorMano(manoJugador)} puntos"
            # )
            compararResultados(calcularValorMano(manoCasa), calcularValorMano(manoJugador))
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
        print("-"*30)
        return True
    elif valorMano == 21:
        print("¡Felicidades! Has ganado con un Blackjack.")
        mostrarMano(manoCasa)
        mostrarMano(manoJugador)
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
    lanzarCarta(manoJugador, Mazo)
    lanzarCarta(manoCasa, Mazo)
    lanzarCarta(manoJugador, Mazo)
    lanzarCarta(manoCasa, Mazo)
    mostrarManoCasaOculta(manoCasa)
    mostrarMano(manoJugador)
#   print(f"Valor actual de la mano: {calcularValorMano(manoJugador)}")
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
     

def lanzarCarta(mano, mazo):
    carta = random.choice(mazo)
    mano.append(carta)
    eliminarCarta(mazo, carta)
    return carta

def repartirCartaCasa(Mazo, manoCasa):
        validarMazoVacio(Mazo)
        valorManoCasa = calcularValorMano(manoCasa)

        while valorManoCasa < 17:
            print("La casa decide repartir una carta...")
            carta = lanzarCarta(manoCasa, Mazo)
            print(f"Carta repartida a la casa: {carta.nombre}{carta.palo}")
            valorManoCasa = calcularValorMano(manoCasa)
            print(f"Valor actual de la mano de la casa: {valorManoCasa}")
        return valorManoCasa

def compararResultados(valorManoCasa, valorManoJugador):
    if valorManoCasa > 21:
        print("¡La casa se ha pasado de 21! Has ganado.")
    elif valorManoCasa > valorManoJugador:
        print("¡La casa gana! Mejor suerte la próxima vez.")
    elif valorManoCasa < valorManoJugador:
        print("¡Felicidades! Has ganado.")
    else:
        print("¡Es un empate!")
import random

class Cartas:
    def __init__(self, id,valor,nombre, palo,color,):
        self.id = id
        self.valor = valor
        self.nombre = nombre
        self.palo = palo
        self.color = color

Mazo = [
Cartas( 1,  1,  "A",    "♠",   "Negro"),
Cartas( 2,  1,  "A",    "♥",   "Rojo"),
Cartas( 3,  1,  "A",    "♦",   "Rojo"),
Cartas( 4,  1,  "A",    "♣",   "Negro"),
Cartas( 5,  2,  "2",    "♠",   "Negro"),
Cartas( 6,  2,  "2",    "♥",   "Rojo"),
Cartas( 7,  2,  "2",    "♦",   "Rojo"),
Cartas( 8,  2,  "2",    "♣",   "Negro"),
Cartas( 9,  3,  "3",    "♠",   "Negro"),
Cartas(10,  3,  "3",    "♥",   "Rojo"),
Cartas(11,  3,  "3",    "♦",   "Rojo"),
Cartas(12,  3,  "3",    "♣",   "Negro"),
Cartas(13,  4,  "4",    "♠",   "Negro"),
Cartas(14,  4,  "4",    "♥",   "Rojo"),
Cartas(15,  4,  "4",    "♦",   "Rojo"),
Cartas(16,  4,  "4",    "♣",   "Negro"),
Cartas(17,  5,  "5",    "♠",   "Negro"),
Cartas(18,  5,  "5",    "♥",   "Rojo"),
Cartas(19,  5,  "5",    "♦",   "Rojo"),
Cartas(20,  5,  "5",    "♣",   "Negro"),
Cartas(21,  6,  "6",    "♠",   "Negro"),
Cartas(22,  6,  "6",    "♥",   "Rojo"),
Cartas(23,  6,  "6",    "♦",   "Rojo"),
Cartas(24,  6,  "6",    "♣",   "Negro"),
Cartas(25,  7,  "7",    "♠",   "Negro"),
Cartas(26,  7,  "7",    "♥",   "Rojo"),
Cartas(27,  7,  "7",    "♦",   "Rojo"),
Cartas(28,  7,  "7",    "♣",   "Negro"),
Cartas(29,  8,  "8",    "♠",   "Negro"),
Cartas(30,  8,  "8",    "♥",   "Rojo"),
Cartas(31,  8,  "8",    "♦",   "Rojo"),
Cartas(32,  8,  "8",    "♣",   "Negro"),
Cartas(33,  9,  "9",    "♠",   "Negro"),
Cartas(34,  9,  "9",    "♥",   "Rojo"),
Cartas(35,  9,  "9",    "♦",   "Rojo"),
Cartas(36,  9,  "9",    "♣",   "Negro"),
Cartas(37, 10, "10",    "♠",   "Negro"),
Cartas(38, 10, "10",    "♥",   "Rojo"),
Cartas(39, 10, "10",    "♦",   "Rojo"),
Cartas(40, 10, "10",    "♣",   "Negro"),
Cartas(41, 10,  "J",    "♠",   "Negro"),
Cartas(42, 10,  "J",    "♥",   "Rojo"),
Cartas(43, 10,  "J",    "♦",   "Rojo"),
Cartas(44, 10,  "J",    "♣",   "Negro"),
Cartas(45, 10,  "Q",    "♠",   "Negro"),
Cartas(46, 10,  "Q",    "♥",   "Rojo"),
Cartas(47, 10,  "Q",    "♦",   "Rojo"),
Cartas(48, 10,  "Q",    "♣",   "Negro"),
Cartas(49, 10,  "K",    "♠",   "Negro"),
Cartas(50, 10,  "K",    "♥",   "Rojo"),
Cartas(51, 10,  "K",    "♦",   "Rojo"),
Cartas(52, 10,  "K",    "♣",   "Negro")
]

MANO = []

def repartir_carta():
    print("----------------------------------")
    valorMano=0
    carta = random.choice(Mazo)
    MANO.append(carta)
    print(f"Carta repartida:  {carta.nombre}{carta.palo}")
    for carta in MANO:
        valorMano += carta.valor
    print(f"Valor actual de la mano: {valorMano}")
    print("----------------------------------")
    if valorMano > 21:
        print("¡Has perdido! El valor de tu mano ha superado los 21 puntos.")
        MANO.clear()
        print("----------------------------------")
    elif valorMano == 21:
        print("¡Felicidades! Has ganado con un Blackjack.")
        MANO.clear()
        print("----------------------------------")


def mostrar_mano():
    print("----------------------------------")
    valorMano=0
    print("Mano actual: ")
    for carta in MANO:
        print(f"{carta.nombre}{carta.palo} de {carta.valor} puntos")
        valorMano += carta.valor
    print(f"{valorMano} puntos actuales")
    print("----------------------------------")



def jugar():
    while True:
        print("\nOpciones:")
        print("1. Repartir carta")
        print("2. Mostrar mano")
        print("3. Mostrar resultado y salir")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            repartir_carta()
        elif opcion == "2":
            mostrar_mano()
        elif opcion == "3":
            mostrar_mano()
            print(f"¡Gracias por jugar! resultado final: {sum(carta.valor for carta in MANO)} puntos")
            MANO.clear()
        elif opcion == "4":
            print("hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

jugar()

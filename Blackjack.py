
from dataclasses import dataclass
class Carta:
    def __init__(self, pinta:str, valor: str, tapada: bool):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False

class Mano:
cdcdcd
    def __init__(self, cartas: tuple):
        self.cartas = []

    def es_blackjack(self)-> bool:
        if self.calcular_valor_mano() == 21 and len(self.cartas) == 2:
            return True
        else:
            "el numero de cartas no supera 21"
            return False


    def calcular_valor_mano(self) -> int:
        valor_total= 0
        ases= 0

        for carta in self.cartas:
            if carta.valor in ["K", "Q", "J"]:
                valor_total += 10
            elif carta.valor == "A":
                valor_total += 11
                ases += 1
            else:
                valor_total += int(carta.valor)

        while ases > 0 and valor_total > 21:
            valor_total -= 10
            ases -= 1
        return valor_total



class Baraja:


    def __init__(self):
        self.cartas: list[Carta] = []


    def revolver(self):
        pinta = ["corazon", "trebol", "diamante", "espada"]
        valor = ["A","2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

        for pinta in pinta:
              for valor in valor:
                carta = Carta(pinta, valor, False)
                self.cartas.append(carta)

    def repartir_carta(self, tapada:bool)-> Carta:

        if self.cartas:
            carta = self.cartas.pop()
            carta.tapada = tapada
            return carta
        else:
            print("La baraja está vacía. Debes volver a barajar las cartas.")
            self.revolver()
            return self.repartir_carta(tapada)



class Jugador:
    def __init__(self,nombre: str, fichas: int):
        self.nombre = nombre
        self.fichas = fichas
        self.mano: Mano = Mano
        self.baraja: Baraja= Baraja()
        self.casa= Casa

    def inicializar_mano(self, cartas):
        self.mano = Mano(cartas)

    def jugada_jugador(self, Jugador):
        while True:
            Jugada= input("desea pedir una carta (p) o plantarse? (a)")
            if Jugada== "p":
                carta_nueva = self.baraja.repartir_carta(False)
                self.mano.cartas.append(carta_nueva)
                self.mostrar_mano()

                print(f"Has recibido una carta: {carta_nueva.valor} de {carta_nueva.pinta}")
                print(f"Cartas en mano: {len(self.mano.cartas)}")
                if self.mano.calcular_valor_mano() > 21:
                    print("Te has pasado de 21. ¡Has perdido!")
            elif Jugada == "a":
                valor_mano = self.mano.calcular_valor_mano()
                print(f"Valor de la mano: {valor_mano}")
                self.casa.jugada_casa(self.mano)
                break

    def mostrar_mano(self):
        print(f"Mano de {self.nombre}:")
        for carta in self.mano.cartas:
            print(f"{carta.valor} de {carta.pinta}")

class Casa:

    def __init__(self):
        self.mano: Mano= Mano


    def inicializar_mano(self, cartas: tuple):
        self.mano = Mano(cartas)

    def jugada_casa(self):
        while self.mano.calcular_valor_mano() < 17:
            carta_nueva = self.baraja.repartir_carta(False)
            self.mano.cartas.append(carta_nueva)


        if self.mano.calcular_valor_mano() > 21:
            print("¡La Casa se ha pasado de 21! ¡Ganas!")
            return True
        return False


    def mostrar_mano(self, revelar= False):
        print("Mano de la Casa:")
        for carta in self.mano.cartas:
            if not revelar and carta.tapada:
                print("Carta tapada")
            else:
                print(f"{carta.valor} de {carta.pinta}")

class Blackjack():

    def __init__(self):
        self.Jugador: Jugador= None
        self.Casa: Casa = Casa()
        self.baraja: Baraja = Baraja()

    def registrar_jugador(self, nombre: str):
        self.nombre= nombre
        print("bienvenido a Backjack " + nombre)
        self.Jugador = Jugador( nombre, 100)
        self.Jugador.inicializar_mano(())
        nuevo_juego= input("desea iniciar un nevo juego? si: a   no: b ")
        if nuevo_juego == "a":
             self.iniciar_juego()




    def iniciar_juego(self):
        self.apuesta= int(input(f"{self.nombre}, ¿cuántas fichas desea apostar? (Tiene {self.Jugador.fichas} fichas disponibles): "))
        print(self.apuesta)
        if self.apuesta > self.Jugador.fichas:
            print("no es posible hacer la apuesta, supera la cantidad de fichas")
            return
        else:
            self.baraja.revolver()
            self.Jugador.inicializar_mano([self.baraja.repartir_carta(False), self.baraja.repartir_carta(False)])
            self.Casa.inicializar_mano([self.baraja.repartir_carta(False), self.baraja.repartir_carta(True)])

            if self.Jugador.mano.es_blackjack():
                print("el numero de cartas supera 21, has perdido el juego")
                self.finalizar_juego()
                self.jugador.fichas -= self.apuesta # Pago por Blackjack (1.5 veces la apuesta)
                print(f"Tus fichas restantes: {self.jugador.fichas}")
                nuevo_juego = input("¿Desea jugar de nuevo? (si: S, no: N): ").upper()

            else:
                self.Jugador.jugada_jugador(self.Jugador)



    def finalizar_juego(self):
        pass

nombre = input("Ingrese su nombre: ")
jugadorw = Blackjack()
jugadorw.registrar_jugador(nombre)


print(jugadorw.nombre)

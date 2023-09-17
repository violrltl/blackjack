import random
from dataclasses import dataclass, field
from typing import ClassVar, Optional
#se refiere a que una variable puede tomr varios tipos de valores


@dataclass
class Carta:
    VALORES: ClassVar[list[str]] = ["A","2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"] #classvar indica que una variable es variable de clase y no de instancia
    PINTAS:  ClassVar[list[str]] = ["corazon", "trebol", "diamante", "espada"]
    pinta: str
    valor: str
    tapada: bool = field(init= False, default= False) #field se usa para establecer un valor con rpedeterminado

    def calcular_valor(self, as_11=True)->int:
        if self.valor== "A":
            if as_11:
                return 11
            else:
                return 1
            pass
        elif self.valor in ["J", "Q", "K"]:
            return 10
        else:
            return int(self.valor)

    def __str__(self)-> str:
        return  f"{self.valor}{self.pinta}"


class Mano:
    def __init__(self, cartas: tuple[Carta, Carta]):
        self.cartas: list[Carta] = []
        self.cartas.extend(self.cartas)

    def es_blackjack(self)-> bool:
      if len(self.cartas)> 2:

          print("tu mano pasa de 21, has perdido e juego")
          return False
      else:
          return self.cartas[0].valor == "A" and self.cartas[1].valor in ["10", "J", "Q", "K"]\
                 or self.cartas[1].valor == "A" and self.cartas[0].valor in ["10", "J", "Q", "K"]


    def agregar_carta(self, carta:Carta):
        self.cartas.append(carta)

    def calcular_valor(self)-> int:
        valor= 0
        for carta in self.cartas:
            valor += carta.calcular_valor(valor < 11)
        return valor

    def destapar(self):
        for self.carta in self.cartas:
            self.tapada = False




class Baraja:

    def __init__(self):
        self.cartas:list[Carta]=[Carta(pinta, valor)for valor in Carta.VALORES for pinta in Carta.PINTAS]

    def revolver(self):
        random.shuffle(self.cartas)


    def repartir_carta(self, tapada:False)-> Optional[Carta]:
        if len(self.cartas) > 0:
            carta = self.cartas.pop()
            carta.tapada = tapada
            return carta
        else:
            return None



class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre = nombre
        self.fichas = fichas
        self.baraja: Baraja = Baraja()
    def inicializar_mano(self, cartas):
        self.Mano = Mano(cartas)
        print(self.Mano)

    def recibir_carta(self, carta: Carta):
        carta= self.baraja.repartir_carta(carta)
        if carta:
            self.Mano.agregar_carta(carta)


    def agregar_fichas(self):
        pass
    def tiene_fichas(self)->bool:
        pass



class Casa:

    def __init__(self):
        pass


    def inicializar_mano(self, cartas: tuple):
        pass

    def jugada_casa(self):
        pass



    def mostrar_mano(self, revelar= False):
        pass

class Blackjack():
    baraja: Baraja= Baraja()

    def __init__(self):
        pass
    def registrar_jugador(self, nombre:str):
        self.Jugador = Jugador(nombre, 100)
        print(f"bienvenido {self.Jugador.nombre}")
        nuevo_juego= input("desea iniciar un nuevo juego? a:si b:no")
        if nuevo_juego== "a":
            self.iniciar_juego()
        else:
            pass

    def iniciar_juego(self):
        self.apuesta = int(input(f"cuantas fichas desea apostar {self.Jugador.nombre}, actualmente tiene {self.Jugador.fichas} "))
        self.Jugador.inicializar_mano(Carta)

        if self.apuesta > self.Jugador.fichas:
            print("no es posible realizar la apuesta")
        else:
            self.baraja.revolver()
            carta_nueva=self.baraja.repartir_carta(tapada=False)
            self.Jugador.recibir_carta(carta_nueva)




    def finalizar_juego(self):
        pass


jugadorw = Blackjack()
nombre= input("Ingrese su nombre: ")
jugadorw.registrar_jugador(nombre)


print(jugadorw)

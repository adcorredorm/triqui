def bienvenida():
    pass

def ganador(tablero:list) -> bool:
    pass

def jugar(jugador_actual:str, tablero:list):
    pass

def alternar_jugador(jugador_actual:str) -> str:
    pass

def mensaje_final(tablero:list):
    pass

def main():
    bienvenida()
    jugador:str = 'X'
    tablero:list = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
    while not ganador(tablero):
        jugar(jugador, tablero)
        jugador = alternar_jugador(jugador)
    mensaje_final(tablero)


if __name__ == '__main__':
    main()
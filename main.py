def bienvenida():
    print('Bienvenidos a el mejor juego de triqui del mundo mundial')
    print('Preparados?')

def comprobar_tablero(tablero:list) -> int:
    ganador:int = 0

    for i in range(3):
        #filas       
        if tablero[i][0]==1 and tablero [i][1]==1 and tablero [i][2]==1:
            ganador = 1
            break
        if tablero[i][0]==-1 and tablero [i][1]==-1 and tablero [i][2]==-1:
            ganador = -1
            break

        #columnas
        if tablero[0][i]==1 and tablero [1][i]==1 and tablero [2][i]==1:
            ganador = 1
            break
        if tablero[0][i]==-1 and tablero [1][i]==-1 and tablero [2][i]==-1:
            ganador = -1
            break

#COMPROBAR DIAGONALES

    #diagonal
    if tablero[0][0]==1 and tablero[1][1]==1 and tablero[2][2]==1:
        ganador = 1
    if tablero[0][0]==-1 and tablero[1][1]==-1 and tablero[2][2]==-1:
        ganador = -1

    #diagonal inversa
    if tablero[0][2]==1 and tablero[1][1]==1 and tablero[2][0]==1:
        ganador = 1
    if tablero[0][2]==-1 and tablero[1][1]==-1 and tablero[2][0]==-1:
        ganador = -1
    
    return ganador

#TODO: comprobar que el tablero no este lleno
def ganador(tablero:list) -> bool:
    return comprobar_tablero(tablero) != 0

def imprimir_tablero(tablero:list):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",tablero[0][0],"   |   ",tablero[0][1],"   |   ",tablero[0][2],"   |",sep="")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",tablero[1][0],"   |   ",tablero[1][1],"   |   ",tablero[1][2],"   |",sep="")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",tablero[2][0],"   |   ",tablero[2][1],"   |   ",tablero[2][2],"   |",sep="")
    print("|       |       |       |")
    print("+-------+-------+-------+")

#TODO: verificar que la casilla no este ocupada
def leer_coordenada(objetivo:str) -> int:
    bandera:bool = True
    while bandera or x < 0 or x > 2:
        bandera = False
        x:int = int(input(f"Seleccione una coordenada valida para la coordenada en {objetivo} "))
    return x

def jugar(jugador_actual:str, tablero:list):
    imprimir_tablero(tablero)
    x:int = leer_coordenada('x')
    y:int = leer_coordenada('y')

    if jugador_actual == 'X':
        jugada:int = 1
    else:
        jugada:int = -1

    tablero[y][x] = jugada


def alternar_jugador(jugador_actual:str) -> str:
    if jugador_actual == 'X':
        return 'O'
    if jugador_actual == 'O':
        return 'X'

def mensaje_final(tablero:list):
    ganador:int = comprobar_tablero(tablero)
    
    if ganador == 0:
        print('El juego quedo en empate')
    else:
        print(f'El ganador fue el jugador {ganador}')

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
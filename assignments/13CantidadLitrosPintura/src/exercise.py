import math
def main():
    #escribe tu código abajo de esta línea
    area=float(input('Area a pintar en metros:"))
    rend=float(input('Rendimiento (m2/1):'))
    litros= area/rend               
    res=math.ceil(litros)
    print(f'Litros a comprar: {res}')
                     
if __name__ == '__main__':
    main()

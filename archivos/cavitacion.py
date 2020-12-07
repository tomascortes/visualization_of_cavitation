
def funcion_cavitacion_1(h1, h2, temp):
    gamma = 9.8 
    radio = 1 # lo fijamos por simplicidad
    rho = 1000
    Q = 100
    pv = 0.001316* 10 ** (8.0713 - (1730.63/(temp + 233.426)))
    parte_arriba = 2*(gamma*(h1 - h2 - Q**2/(2*radio**2*3.1416)**2*9.18) - pv)
    parte_abajo = rho*(Q/(3.1416*radio**2))**2


    indice = parte_arriba/parte_abajo
    print(indice, pv)
    #si es negativo hay cavitaccion
    return (True, indice) if indice < 0 else (False, indice)

def funcion_cavitacion_2(p2, v2, temp):
    pv = 10 ** (8.0713 - (1730.63/(temp + 233.426)))
    indice = 2 *  (9.8 *p2 - pv) / (v2**2)
    return (True, pv/10) if indice < 0 else (False, pv/10)
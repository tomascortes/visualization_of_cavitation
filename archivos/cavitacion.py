import math
def funcion_cavitacion_1(h1, h2, temp):
    gamma = 0.98
    v = math.sqrt(h1*2*gamma) # lo fijamos por simplicidad (depende del radio)
    rho = 1
    pa = rho*9.8*h1
    p2 = pa - gamma*h2- (rho/2)*(v)**2
    # print("pedos", p2, v)
    pv = 10 ** (8.0713 - (1730.63/(temp + 233.426)))
    indice = 2 * (9.8*p2 - pv)/v**2


    # parte_arriba = 2*(gamma*(h1 - h2 - v*9.18) )
    # parte_arriba -= 2*pv
    # parte_abajo = rho*(Q/(3.1416*radio**2))**2


    # indice = parte_arriba/parte_abajo
    print(indice, pv)
    #si es negativo hay cavitaccion
    return (True, pv/10, p2) if indice < 0 else (False, pv/10, p2)

def funcion_cavitacion_2(p2, v2, temp):
    pv = 10 ** (8.0713 - (1730.63/(temp + 233.426)))
    indice = 2 *  (9.8 *p2 - pv) / (v2**2)
    return (True, pv/10) if indice < 0 else (False, pv/10)
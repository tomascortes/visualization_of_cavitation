
def funcion_cavitacion_1(h1, h2, temp):
    pv = 10 ** (8.0713 - (1730.63/(temp + 233.426)))

    return True if h2 > 12 else False

def funcion_cavitacion_2(p2, v2, temp):
    pv = 10 ** (8.0713 - (1730.63/(temp + 233.426)))
    indice = 2 *  (9.8 *p2 - pv) / (v2**2)
    print(v2)
    return (True, pv) if indice < 0 else (False, pv)
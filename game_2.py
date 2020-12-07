import pygame as pg
from archivos.inputbox import InputBox
from archivos.cavitacion import funcion_cavitacion_2
import archivos.const as CONST
from random import randint

pg.init()
width  = 900
height = 600
FONT = pg.font.Font(None, 32)

screen = pg.display.set_mode((width, height))

def main():
    clock = pg.time.Clock()
    
    #cajas de input
    input_size = (70,  35)
    input_size_2 = (100,  35)
    input_r1 = InputBox(20, height/5 - 20, input_size[0],  input_size[1], max_value=20, min_value=4, text=CONST.r1_inicial)
    input_r2 = InputBox(20, 2*height/5 - 20, input_size[0],  input_size[1], max_value=30, min_value=4, text=CONST.r2_inicial)
    input_p1 = InputBox(20, 3*height/5 - 20, input_size_2[0],  input_size_2[1], max_value=10, min_value=0.1, text=CONST.p1_inicial, new_w=True)
    input_v1 = InputBox(200, 3*height/5 - 20, input_size_2[0],  input_size_2[1], max_value=10, min_value=0.1, text=CONST.p2_inicial, new_w=True)
    input_temp = InputBox(20, 4*height/5 - 20, input_size[0],  input_size[1], max_value=100, min_value=0, text=CONST.temp_inicial)
    input_boxes = [input_r1, input_r2, input_p1, input_v1, input_temp]

    

    #variables a usar despues
    celeste = (81, 209, 246)
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.MOUSEBUTTONDOWN: 
                #if the mouse is clicked on the 
                # button the game is terminated 
                mouse = pg.mouse.get_pos()
                if 20 <= mouse[0] <= 200 and 3.5*height/5 -10 <= mouse[1] <= 3.5*height/5+30: 
                    print(mouse[0], mouse[1])
                    for i_box in input_boxes:
                        i_box.define_value()

        for box in input_boxes:
            box.update()
        
        
        #------------------------------------
        #se borra lo anterior y parte lo nuevo
        screen.fill((30, 30, 30))
        #lineas blancas que separan las pantallas
        pg.draw.line(screen, (255,255,255), (width*0.4 - 10,0), (width*0.4-10,height), 10)
        
        
        #dibuja las casillas de input
        for box in input_boxes:
            box.draw(screen)

        #dibuja texto input
        #texto sobre cajas de input
        text_radio_1 = FONT.render(f'Radio 1 = {input_r1.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_alt_1 = text_radio_1.get_rect(x=20, y=0.5*height/5)
        
        text_radio_2 = FONT.render(f'Radio 2 = {input_r2.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_alt_2 = text_radio_2.get_rect(x=20, y=1.5*height/5)

        text_p_1 = FONT.render(f'Presion 1', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_p_1 = text_radio_2.get_rect(x=20, y=2.5*height/5)

        text_v_1 = FONT.render(f'Velocidad 1', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_v_1 = text_v_1.get_rect(x=200, y=2.5*height/5)
        
        text_temp = FONT.render(f'Temperatura = {input_temp.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_temp = text_temp.get_rect(x=20, y=3.5*height/5)
        
        text_button = FONT.render('       Calcular     ', True, (0,0,0),celeste)
        text_rect_button = text_button.get_rect(x=20, y=4.5*height/5)

        text_r0 = FONT.render('r=0', True, (255,255,255), (30, 30, 30))
        text_rect_r0 = text_r0.get_rect(x=width*0.9 + 20, y= height/2 - 30)

        input_v2 = (input_v1.value * (input_r1.value**2)) / (input_r2.value**2)
        input_p2 = round(input_p1.value + ((input_v1.value**2) - (input_v2**2))*(1/2), 2)
        
        
        screen.blit(text_radio_1, text_rect_alt_1)
        screen.blit(text_radio_2, text_rect_alt_2)
        screen.blit(text_p_1, text_rect_p_1)
        screen.blit(text_v_1, text_rect_v_1)
        screen.blit(text_temp, text_rect_temp)
        screen.blit(text_button, text_rect_button)
        screen.blit(text_r0, text_rect_r0)


       
        #BOMBA
        bomba_img = pg.image.load('img/bomba.png')
        bomba_img = pg.transform.scale(bomba_img, (150, 100))
        screen.blit(bomba_img, (3.65*width/8,height/2 - 50)) 

        #dibujar radio 1
        pos_estanque = (
            5*width/8 , 
            height/2 - 5*input_r1.value,  
            width/8, 
            10* input_r1.value )

        pg.draw.rect(screen, celeste, pos_estanque)

        #dibujar radio 2
        pos_estanque_2 = (
            6*width/8 - 1, 
            height/2 - 5*input_r2.value,  
            width/8, 
            10* input_r2.value )

        pg.draw.rect(screen, celeste, pos_estanque_2)

        #linea que muestra h=0 (la hacemos al final para que este sobre el dibujo)
        pg.draw.line(screen, (255,255,255), (5*width/8, height/2), (width, height/2), 2)


        #las ultimas weaitas de h1 y h2 que dicen la altura
        string_webiado  = f'({input_r1.value}) r1-> ' if input_r1.value >= 10 else f'  ({input_r1.value}) r1->'
        
        text_r1 = FONT.render(string_webiado, True, (100,230,230))
        text_rect_r1 = text_r1.get_rect(x=pos_estanque[0] - 100, y=pos_estanque[1] + 10*input_r1.value - 10)
        screen.blit(text_r1, text_rect_r1)

        text_p1 = FONT.render(f'p1 = {input_p1.value}', True, (255,255,255))
        text_rect_p1 = text_p1.get_rect(x=pos_estanque[0], y=pos_estanque[1] - 30)
        screen.blit(text_p1, text_rect_p1)

        text_r2 = FONT.render(f'<-r2 ({input_r2.value})', True, (255,255,255))
        text_rect_r2 = text_r2.get_rect(x=pos_estanque_2[0] + 120, y=pos_estanque_2[1] + 10*input_r2.value - 10)
        screen.blit(text_r2, text_rect_r2)

        text_p2 = FONT.render(f'p2 = {input_p2}', True, (255,255,255))
        text_rect_p2 = text_p2.get_rect(x=pos_estanque_2[0], y=pos_estanque_2[1] - 30)
        screen.blit(text_p2, text_rect_p2)


        ## BUBBLES
        cav, pv = funcion_cavitacion_2(input_p2, input_v2, input_temp.value)
        if cav:
            center1 = pos_estanque_2[0] + 45, pos_estanque_2[1] + 10*input_r2.value - 25
            for i in range(15):
                rando = [randint(-40,20), randint(0,20)]
                pos = [x + y for x, y in zip(center1, rando)]
                pg.draw.circle(screen, (255,255,255), pos, randint(2,7))
                rando2 = [randint(-40,0), randint(-20,0)]
                pos2 = [x + y for x, y in zip(center1, rando2)]
                pg.draw.circle(screen, (255,255,255), pos2, randint(2,7))

            center2 = pos_estanque_2[0] + 45, pos_estanque_2[1] + 5
            for i in range(15):
                rando = [randint(-40,20), randint(0,20)]
                pos = [x + y for x, y in zip(center2, rando)]
                pg.draw.circle(screen, (255,255,255), pos, randint(2,7))
                rando2 = [randint(-40,0), randint(0,40)]
                pos2 = [x + y for x, y in zip(center2, rando2)]
                pg.draw.circle(screen, (255,255,255), pos2, randint(2,7))

        text_pv = FONT.render(f'Presion de vapor = {round(pv, 4)}', True, (255,255,255))
        text_rect_pv = text_pv.get_rect(x=width/2, y=3*height/4)
        screen.blit(text_pv, text_rect_pv)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
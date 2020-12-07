import pygame as pg
from archivos.inputbox import InputBox
from archivos.cavitacion import funcion_cavitacion_1
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
    input_h1 = InputBox(20, height/5, input_size[0],  input_size[1], max_value=20, min_value=1, text=CONST.h1_inicial)
    input_h2 = InputBox(20, 2*height/5, input_size[0],  input_size[1], max_value=20, min_value=2, text=CONST.h2_inicial)
    input_temp = InputBox(20, 3*height/5, input_size[0],  input_size[1], max_value=100, min_value=0, text=CONST.temp_inicial)
    input_radio = InputBox(20, 4*height/5, input_size[0],  input_size[1], max_value=4, min_value=1, text=CONST.radio_inicial)
    input_boxes = [input_h1, input_h2, input_temp]
    p_a = 0
    p_2 = 0
    

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
        text_altura_1 = FONT.render(f'altura h1 = {input_h1.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_alt_1 = text_altura_1.get_rect(x=20, y=0.5*height/5)
        
        text_altura_2 = FONT.render(f'altura h2 = {input_h2.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_alt_2 = text_altura_2.get_rect(x=20, y=1.5*height/5)
        
        text_temp = FONT.render(f'temperatura = {input_temp.value}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_temp = text_temp.get_rect(x=20, y=2.5*height/5)
        
        # text_radio = FONT.render('radio', True, pg.Color('lightskyblue3'), (30, 30, 30))
        # text_rect_radio = text_radio.get_rect(x=20, y=3.5*height/5)

        text_button = FONT.render('       Calcular     ', True, (0,0,0),celeste)
        text_rect_button = text_button.get_rect(x=20, y=3.5*height/5)

        text_h0 = FONT.render('h=0', True, (255,255,255), (30, 30, 30))
        text_rect_h0 = text_h0.get_rect(x=width*0.4 + 20, y=3.5*height/5 - 30)


        #presion label
        label_extra1 = FONT.render(f'presion de vapor temp = {round(p_a,2)}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_label_extra1 = label_extra1.get_rect(x=20, y=4*height/5)

        label_extra2 = FONT.render(f'presion2 = {p_2}', True, pg.Color('lightskyblue3'), (30, 30, 30))
        text_rect_label_extra2 = label_extra2.get_rect(x=20, y=4.5*height/5)
        screen.blit(label_extra1, text_rect_label_extra1)
        screen.blit(label_extra2, text_rect_label_extra2)

        
        
        screen.blit(text_altura_1, text_rect_alt_1)
        screen.blit(text_altura_2, text_rect_alt_2)
        screen.blit(text_temp, text_rect_temp)
        # screen.blit(text_radio, text_rect_radio)
        screen.blit(text_button, text_rect_button)
        screen.blit(text_h0, text_rect_h0)


       
        

        #dibujar estanque
        pos_estanque = (
            width/2 , 
            3.5*height/5 - 20*input_h1.value,  
            width/6, 
            120 + 20*input_h1.value )

        pg.draw.rect(screen, celeste, pos_estanque)

        # linea tuberia estanque -> tuberia alta 1
        pg.draw.rect(screen, celeste, ( 2*width/3 , 3.5*height/5 + 90, 50, 30))

        
        # coordenadas tuberias altas
        pos_tub_y = ( 
            4*width/6 + 50,
            3.5*height/5 - 20*input_h2.value, 
            30, 
            120 + 20*input_h2.value)

        # linea tuberia alta 1
        pg.draw.rect(screen, celeste, pos_tub_y)

        # linea tuberia alta 2
        pg.draw.rect(screen, celeste, 
            (pos_tub_y[0] + 100, 
            pos_tub_y[1], 
            pos_tub_y[2], 
            20*input_h2.value))

        # linea tuberia alta 1 -> tuberia alta 2
        pg.draw.rect(screen, celeste, ( pos_tub_y[0] , pos_tub_y[1], 100, 30))

        #linea que muestra h=0 (la hacemos al final para que este sobre el dibujo)
        pg.draw.line(screen, (255,255,255), (width*0.4, 3.5*height/5), (width, 3.5*height/5), 2)


        #las ultimas weaitas de h1 y h2 que dicen la altura
        string_webiado  = f'({input_h1.value}) h1-> ' if input_h1.value >= 10 else f'  ({input_h1.value}) h1->'
        
        text_h1 = FONT.render(string_webiado, True, (255,255,255))
        text_rect_h1 = text_h1.get_rect(x=pos_estanque[0]- 90 , y=pos_estanque[1] - 10 )
        screen.blit(text_h1, text_rect_h1)

        text_h2 = FONT.render(f'<-h2 ({input_h2.value})', True, (255,255,255))
        text_rect_h2 = text_h2.get_rect(x=pos_tub_y[0] + 130, y=pos_tub_y[1] - 10 )
        screen.blit(text_h2, text_rect_h2)

        cav, p_a, p_2 = funcion_cavitacion_1(input_h1.value, input_h2.value, input_temp.value)

        if cav:
            center = [pos_tub_y[0] + 50 , pos_tub_y[1]]
            for i in range(20):
                rando = [randint(-40,70), randint(0,20)]
                pos = [x + y for x, y in zip(center, rando)]
                pg.draw.circle(screen, (255,255,255), pos, randint(2,7))



        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
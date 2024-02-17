from turtle import *
import colorsys

def draw_rose():
    bgcolor('black')
    speed(5000)
    pensize(2)
    h = 0

    for i in range(200):
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        h += 0.006
        pencolor(color)

        lt(179)
        backward(i * 1.5)
        circle(i * 0.1, 120)
        rt(14)
        forward(i * 1.5)
        circle(i * 0.3, 120)

wn = Screen()
wn.title("¡Feliz Dia de San Valentin!")
wn.bgcolor('black')

width, height = wn.window_width(), wn.window_height()
setup(width=width, height=height)

draw_rose()

message_pos_1 = (0, -height // 2 + 50)
penup()
goto(message_pos_1)

bgcolor('black')
fillcolor('red')
color('white')
style = ('Courier', int(height / 20), 'italic')
begin_fill()
write("¡Feliz Dia de San Valentin!", font=style, align='center')
end_fill()

message_pos_2 = (0, -height // 2 + 20)
penup()
goto(message_pos_2)

bgcolor('black')
fillcolor('red')
color("white")
begin_fill()
write("Nosotros si resolvemos", font=style, align='center')
end_fill()

done
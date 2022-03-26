import turtle as trtl

screen = trtl.Screen()

screen.tracer(0)
screen.setup(500,500)

pen = trtl.Turtle()
pen.up()
pen.hideturtle()
pen.speed(0)



on_menu = True

font = ("MS Sans Serif", 20, "bold")

# Draw Menu Title
pen.setpos(0, 150)
pen.write("Carnival Games:", font=font, align="Center")
pen.setpos(0, 110)
pen.write("Throwing for Fun", font=font, align="Center")

def create_button(color, text):
    pen.fillcolor(color)
    pen.setheading(0)

    # Draw button
    pen.down()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.up()

    # Write button text
    pen.forward(100)
    pen.right(90)
    pen.forward(40)
    pen.write(text, font=font, align="Center")

def click_button(x, y):
    global on_menu

    # Event for clicking top game button
    if not on_menu:
        if x > -100 and x < 100:
            if y > 100 and y < 150:
                pass

    # Event for clicking middle game button
    if not on_menu:
        if x > -100 and x < 100:
            if y > 0 and y < 50:
                clown_game()

    # Event for clicking bottom game button
    if not on_menu:
        if x > -100 and x < 100:
            if y > -100 and y < -50:
                pass

    # Event for clicking top menu button
    if on_menu:
        if x > -100 and x < 100:
            if y > 0 and y < 50:
                pen.clear()
                pen.setpos(-100, 150)
                create_button("cyan", "Balloon Darts")
                pen.setpos(-100, 50)
                create_button("cyan", "Clown Ball")
                pen.setpos(-100, -50)
                create_button("cyan", "Placeholder")
                on_menu = False

    # Event for clicking bottom menu button
    if on_menu:
        if x > -100 and x < 100:
            if y > -100 and y < -50:
                # Add change to shop screen here eventually
                pass

    screen.update()

def draw_clown(size):
    pen.setheading(90)
    pen.down()
    pen.pencolor("gold")
    pen.forward(size*2/3)
    pen.pencolor("red")
    pen.forward(size/2)
    for _ in range(2):
        pen.right(90)
        pen.forward(size/2)
    pen.pencolor("gold")
    pen.forward(size*2/3)
    pen.up()

def clown_game():
    pen.clear()

    pen.setpos(-150, -100)
    pen.setheading(-45)

    # Draw Clown Ball frame
    pen.down()
    pen.circle(212.132035, 360, 4)

    # Draw clown shelving/platforms
    pen.setheading(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(300)

    # Draw clowns
    pen.up()
    # Top row
    pen.setpos(-105, 100)
    draw_clown(80)
    pen.setpos(-20, 100)
    draw_clown(80)
    pen.setpos(65, 100)
    draw_clown(80)
    # Middle row
    pen.setpos(-118, 0)
    draw_clown(70)
    pen.setpos(-51, 0)
    draw_clown(70)
    pen.setpos(16, 0)
    draw_clown(70)
    pen.setpos(83, 0)
    draw_clown(70)
    # Bottom row
    pen.setpos(-125, -100)
    draw_clown(60)
    pen.setpos(-70, -100)
    draw_clown(60)
    pen.setpos(-15, -100)
    draw_clown(60)
    pen.setpos(40, -100)
    draw_clown(60)
    pen.setpos(95, -100)
    draw_clown(60)

    # Draw throwing bar
    pen.up()
    pen.setpos(-150, -150)
    pen.setheading(0)
    pen.fillcolor("red")
    pen.pencolor("black")
    pen.down()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(300)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.up()

    screen.update()

# Create Menu Buttons
pen.setpos(-100, 50)
create_button("lime", "Choose Game")
pen.setpos(-100, -50)
create_button("yellow", "Shop")

screen.onclick(click_button)

screen.mainloop()
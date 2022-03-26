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
                pass

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

# Create Menu Buttons
pen.setpos(-100, 50)
create_button("lime", "Choose Game")
pen.setpos(-100, -50)
create_button("yellow", "Shop")

screen.onclick(click_button)

screen.mainloop()
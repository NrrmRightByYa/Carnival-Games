import random
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

def main_menu():
    pen.clear()

    # Draw Menu Title
    pen.setpos(0, 150)  
    pen.write("Carnival Games:", font=font, align="Center")
    pen.setpos(0, 110)
    pen.write("Throwing for Fun", font=font, align="Center")

    # Create Menu Buttons
    pen.setpos(-100, 50)
    create_button("lime", "Choose Game")
    pen.setpos(-100, -50)
    create_button("yellow", "Shop")

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

    # Return to main menu after clown game button
    if not on_menu:
        if x > -150 and x < 150:
            if y > -200 and y < -150:
                if ball_count <= 0:
                    ball_display.clear()
                    instructions.clear()
                    main_menu()
                    on_menu = True

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

def draw_clown(size, mode=""):
    pen.setheading(90)
    pen.down()

    color1 = "gold"
    color2 = "red"

    if mode.lower() == "clear":
        color1 = "white"
        color2 = "white"

    # Draw body
    pen.pencolor(color1)
    pen.forward(size*2/3)

    # Draw head
    pen.pencolor(color2)
    pen.forward(size/2)
    for _ in range(2):
        pen.right(90)
        pen.forward(size/2)

    # Draw rest of body
    pen.pencolor(color1)
    pen.forward(size*2/3)
    pen.up()

def draw_accuracy(size):
    pen.setheading(270)
    pen.down()
    pen.pencolor("black")

    pen.begin_fill()
    for _ in range(2):
        pen.forward(50)
        pen.left(90)
        pen.forward(size/2)
        pen.left(90)
    pen.end_fill()

    pen.up()

def stop_arrow():
    global vertical_stopped, bar_stopped, ball_count

    vertical_stopped = True
    bar_stopped = True

def draw_throwbar():
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

def clown_game():
    global vertical_stopped, bar_stopped, ball_count, ball_display, instructions

    pen.clear()

    score = 0

    clown_status = [
        [1, 1, 1],
        [1, 1, 1, 1], 
        [1, 1, 1, 1, 1]
        ]
    
    increment = -0.1
    x = -150
    y = 200

    ball_count = 20
    ball_display = trtl.Turtle()
    ball_display.hideturtle()
    ball_display.up()

    vertical_arrow = trtl.Turtle()
    vertical_arrow.shapesize(2)
    vertical_arrow.up()
    vertical_arrow.setpos(-160, 200)

    bar_arrow = trtl.Turtle()
    bar_arrow.shapesize(2)
    bar_arrow.up()
    bar_arrow.setpos(-150, -140)
    bar_arrow.setheading(270)

    instructions = trtl.Turtle()
    instructions.hideturtle()
    instructions.up()
    instructions.speed(0)

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

    pen.up()

    draw_throwbar()

    # Write score and ball count
    ball_display.setpos(-180, 208)
    ball_display.write(f"Score: {score}", font=font, align="Center")

    ball_display.setpos(155, 208)
    ball_display.write(f"Balls left: {ball_count}", font=font, align="Center")

    # Write instruction text
    instructions.setpos(0, -240)
    instructions.write("Press Spacebar to Stop", font=font, align="Center")
    
    # Draw clowns
    # Top row
    if clown_status[0][0]:
        pen.setpos(-105, 100)
        draw_clown(80)
    if clown_status[0][1]:
        pen.setpos(-20, 100)
        draw_clown(80)
    if clown_status[0][2]:
        pen.setpos(65, 100)
        draw_clown(80)

    # Middle row
    if clown_status[1][0]:
        pen.setpos(-118, 0)
        draw_clown(70)
    if clown_status[1][1]:
        pen.setpos(-51, 0)
        draw_clown(70)
    if clown_status[1][2]:
        pen.setpos(16, 0)
        draw_clown(70)
    if clown_status[1][3]:
        pen.setpos(83, 0)
        draw_clown(70)

    # Bottom row
    if clown_status[2][0]:
        pen.setpos(-125, -100)
        draw_clown(60)
    if clown_status[2][1]:
        pen.setpos(-70, -100)
        draw_clown(60)
    if clown_status[2][2]:
        pen.setpos(-15, -100)
        draw_clown(60)
    if clown_status[2][3]:
        pen.setpos(40, -100)
        draw_clown(60)
    if clown_status[2][4]:
        pen.setpos(95, -100)
        draw_clown(60)

        screen.update()

    while ball_count > 0:

        # Make vertical arrow move up and down
        vertical_stopped = False
        while not vertical_stopped:
            y += increment
            vertical_arrow.setpos(-160, y)
            if y < -100:
                increment = 0.1
            elif y > 200:
                increment = -0.1
            screen.update()

        pen.fillcolor("lime")
        # Draw corresponding accuracies for throwing bar
        if vertical_arrow.ycor() > 100:
            # Top row
            if clown_status[0][0]:
                pen.setpos(-105, -150)
                draw_accuracy(80)
            if clown_status[0][1]:
                pen.setpos(-20, -150)
                draw_accuracy(80)
            if clown_status[0][2]:
                pen.setpos(65, -150)
                draw_accuracy(80)
        elif vertical_arrow.ycor() > 0:
            # Middle row
            if clown_status[1][0]:
                pen.setpos(-118, -150)
                draw_accuracy(70)
            if clown_status[1][1]:
                pen.setpos(-51, -150)
                draw_accuracy(70)
            if clown_status[1][2]:
                pen.setpos(16, -150)
                draw_accuracy(70)
            if clown_status[1][3]:
                pen.setpos(83, -150)
                draw_accuracy(70)
        elif vertical_arrow.ycor() > -100:
            # Bottom row
            if clown_status[2][0]:
                pen.setpos(-125, -150)
                draw_accuracy(60)
            if clown_status[2][1]:
                pen.setpos(-70, -150)
                draw_accuracy(60)
            if clown_status[2][2]:
                pen.setpos(-15, -150)
                draw_accuracy(60)
            if clown_status[2][3]:
                pen.setpos(40, -150)
                draw_accuracy(60)
            if clown_status[2][4]:
                pen.setpos(95, -150)
                draw_accuracy(60)

        # Make bar arrow move right and left
        bar_stopped = False
        while not bar_stopped:
            x += increment
            bar_arrow.setpos(x, -140)
            if x < -150:
                increment = 0.1
            elif x > 150:
                increment = -0.1
            screen.update() 

        # Check top row clown hit
        if vertical_arrow.ycor() > 100:
            if bar_arrow.xcor() >= -105 and bar_arrow.xcor() <= -65:
                pen.setpos(-105, 100)
                draw_clown(80, mode="clear")
                if clown_status[0][0]:
                    score += 1
                    clown_status[0][0] = 0
            elif bar_arrow.xcor() >= -20 and bar_arrow.xcor() <= 20:
                pen.setpos(-20, 100)
                draw_clown(80, mode="clear")
                if clown_status[0][1]:
                    score += 1
                    clown_status[0][1] = 0
            elif bar_arrow.xcor() >= 65 and bar_arrow.xcor() <= 105:
                pen.setpos(65, 100)
                draw_clown(80, mode="clear")
                if clown_status[0][2]:
                    score += 1
                    clown_status[0][2] = 0

        # Check middle row clown hit
        elif vertical_arrow.ycor() > 0:
            if bar_arrow.xcor() >= -118 and bar_arrow.xcor() <= -83:
                pen.setpos(-118, 0)
                draw_clown(70, mode="clear")
                if clown_status[1][0]:
                    score += 1
                    clown_status[1][0] = 0
            if bar_arrow.xcor() >= -51 and bar_arrow.xcor() <= -16:
                pen.setpos(-51, 0)
                draw_clown(70, mode="clear")
                if clown_status[1][1]:
                    score += 1
                    clown_status[1][1] = 0
            if bar_arrow.xcor() >= 16 and bar_arrow.xcor() <= 51:
                pen.setpos(16, 0)
                draw_clown(70, mode="clear")
                if clown_status[1][2]:
                    score += 1
                    clown_status[1][2] = 0
            if bar_arrow.xcor() >= 83 and bar_arrow.xcor() <= 118:
                pen.setpos(83, 0)
                draw_clown(70, mode="clear")
                if clown_status[1][3]:
                    score += 1
                    clown_status[1][3] = 0

        # Check bottom row clown hit
        elif vertical_arrow.ycor() > -100:
            if bar_arrow.xcor() >= -125 and bar_arrow.xcor() <= -95:
                pen.setpos(-125, -100)
                draw_clown(60, mode="clear")
                if clown_status[2][0]:
                    score += 1
                    clown_status[2][0] = 0
            if bar_arrow.xcor() >= -70 and bar_arrow.xcor() <= -40:
                pen.setpos(-70, -100)
                draw_clown(60, mode="clear")
                if clown_status[2][1]:
                    score += 1
                    clown_status[2][1] = 0
            if bar_arrow.xcor() >= -15 and bar_arrow.xcor() <= 15:
                pen.setpos(-15, -100)
                draw_clown(60, mode="clear")
                if clown_status[2][2]:
                    score += 1
                    clown_status[2][2] = 0
            if bar_arrow.xcor() >= 40 and bar_arrow.xcor() <= 70:
                pen.setpos(40, -100)
                draw_clown(60, mode="clear")
                if clown_status[2][3]:
                    score += 1
                    clown_status[2][3] = 0
            if bar_arrow.xcor() >= 95 and bar_arrow.xcor() <= 125:
                pen.setpos(95, -100)
                draw_clown(60, mode="clear")
                if clown_status[2][4]:
                    score += 1
                    clown_status[2][4] = 0

        # Decrement ball count
        ball_count -= 1

        # Rewrite ball count
        ball_display.clear()
        ball_display.setpos(155, 208)
        ball_display.write(f"Balls left: {ball_count}", font=font, align="Center")

        # Rewrite score
        ball_display.setpos(-180, 208)
        ball_display.write(f"Score: {score}", font=font, align="Center")

        # Respawn random clown after 3 balls
        '''clown_dead = not any(clown_status)
        if not clown_dead:
            if ball_count % 3 == 2:
                for row in clown_status:
                    for clown in row:
                        if clown == 0:
                            clown_status[clown_status.index(row)][row.index(0)] = 1
                            break
                    break'''

        # Redraw throwing bar
        draw_throwbar()

    vertical_arrow.hideturtle()
    bar_arrow.hideturtle()

    instructions.clear()
    instructions.setpos(0, -190)
    instructions.write("Main Menu", font=font, align="Center")

main_menu()

screen.onclick(click_button)
screen.onkey(stop_arrow, "space")
screen.listen()

screen.mainloop()
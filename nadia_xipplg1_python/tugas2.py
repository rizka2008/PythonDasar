import turtle

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.goto(x2, y2)
        turtle.goto(x3, y3)
        turtle.goto(x1, y1)
    turtle.end_fill()

def draw_trapezium(x1, y1, x2, y2, x3, y3, x4, y4, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x1, y1)
    turtle.end_fill()

def draw_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.goto(x1, y1)
    turtle.end_fill()

# Set up the screen size
turtle.setup(800, 600)
turtle.speed(1)

# Gambar persegi panjang (merah)
draw_rectangle(-100, 100, 150, 80, "red")

# Gambar segitiga (kuning)
draw_triangle(50, 100, 100, 200, 150, 100, "yellow")

# Gambar trapesium (hijau)
draw_trapezium(-150, -100, -50, -100, -30, 0, -170, 0, "green")

# Gambar jajar genjang (biru)
draw_parallelogram(50, -100, 150, -100, 100, 0, 0, 0, "blue")

# Gambar belah ketupat (ungu)
draw_parallelogram(-100, -200, 0, -300, 100, -200, 0, -100, "purple")

# Tutup jendela saat selesai
turtle.done()
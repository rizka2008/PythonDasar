import turtle as tt

def draw_rectangle(color, width, height):
    tt.begin_fill()
    tt.fillcolor(color)
    for _ in range(2):
        tt.forward(width)
        tt.left(90)
        tt.forward(height)
        tt.left(90)
    tt.end_fill()

def draw_indonesia_flag():
    tt.speed(1)
    tt.bgcolor('black')
    tt.penup()
    tt.goto(-100, 50)  # Posisi awal bendera
    tt.pendown()

    # Gambar latar belakang putih
    draw_rectangle("white", 200, 100)

    # Gambar merah bagian atas
    tt.penup()
    tt.goto(-100, 50)
    tt.pendown()
    draw_rectangle("red", 200, 20)

    # Tandai garis tengah bendera
    tt.penup()
    tt.goto(0, 50)
    tt.pendown()
    tt.color("white")
    tt.goto(0, -50)
    tt.penup()

    tt.hideturtle()
    tt.done()

# Panggil fungsi untuk menggambar bendera Indonesia
draw_indonesia_flag()
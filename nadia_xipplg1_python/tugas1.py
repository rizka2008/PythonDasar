import turtle as tt

# Fungsi untuk menggambar persegi panjang
def drawRectangle(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    for _ in range(2):
        tt.forward(100)  # Panjang
        tt.left(90)  # Sudut kanan
        tt.forward(50)  # Lebar
        tt.left(90)

# Fungsi untuk menggambar segitiga
def drawTriangle(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    for _ in range(3):
        tt.forward(100)
        tt.left(120)

# Fungsi untuk menggambar trapesium
def drawTrapezium(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.forward(100)
    tt.left(45)
    tt.forward(50)
    tt.left(135)
    tt.forward(100)
    tt.left(45)
    tt.forward(50)

# Fungsi untuk menggambar jajar genjang
def drawParallelogram(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.forward(100)
    tt.left(60)
    tt.forward(50)
    tt.left(120)
    tt.forward(100)
    tt.left(60)
    tt.forward(50)

# Fungsi untuk menggambar belah ketupat
def drawDiamond(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.setheading(45)  # Mengatur sudut
    tt.forward(70)
    tt.left(90)
    tt.forward(70)
    tt.left(90)
    tt.forward(70)
    tt.left(90)
    tt.forward(70)
    tt.left(90)

# Inisialisasi layar
tt.setup(800, 600)

# Menggambar berbagai bangun datar di tempat yang berbeda
drawRectangle(-200, 100)
drawTriangle(-50, 100)
drawTrapezium(100, 100)
drawParallelogram(-200, -50)
drawDiamond(-50, -50)

# Menutup jendela saat mengklik layar
tt.exitonclick()
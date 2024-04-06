bg=0
def setup():
    size(600,600)
def draw():
    global bg
    background(bg)
    fill(255,0,400)
    rect(450,120,100,50)
def mouseClicked():
    global bg
    if mouseX>450 and mouseX<550 and mouseY>120 and mouseY<170:
        bg=252

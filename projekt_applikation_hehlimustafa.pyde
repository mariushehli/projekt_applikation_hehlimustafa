#Karte als Hintegrundbild----------------------------------------------------
def setup():
    size(862, 500)
    photo = loadImage("IMG_1522.jpg")
    image(photo, 0, 0)
    photo.resize(862, 500)
    image(photo, 0, 0)
#Textfeld------------------------------------------------------------------
    rect(10,380,840,100)
    
#Text----------------------------------------------------------------------
def draw():
    fill(0, 0, 0)
    textSize(16)
    textAlign(CENTER)
    text("Start: Fatima lebt in Afghanistan. Sie will kein Kopftuch tragen.\nDazu betreibt sie ein Krankenhaus nur für Mädchen.\nDeshalb muss sie aus Afghanistan fliehen.\nWelches der beiden Fluchmittel soll sie benutzen? Pfeil Links: Auto; Pfeil recht: Bus", 431, 400)
    fill(255, 255, 255)
    
#Funktion Entscheidung Pfeil links/rechts
    if keyCode == LEFT:
        line(700, 400, 525, 350)
        rect(10,380,840,100)
    if keyCode == RIGHT:
        line(700, 400, 525, 350)
        rect(10,380,840,100)
        
#Text2-------------------------------------------------------------------
    fill(0, 0, 0)
    textSize(16)
    textAlign(CENTER)
    text("Georgien oder Türkei?", 431, 400)
    fill(255, 255, 255)
    
#Entscheidung2
    if keyCode == LEFT:
        line(525, 350, 400, 300)
    if keyCode == RIGHT:
        line(525, 350, 500, 250)

   
        

def setup():
    size(862, 500)
    photo = loadImage("IMG_1522.jpg")
    image(photo, 0, 0)
    photo.resize(862, 500)
    image(photo, 0, 0)
    
def draw():
    textSize(32)
    textAlign(CENTER)
    text("Start: Fatima lebt in Afghanistan. Sie will kein Kopftuch tragen. Dazu betreibt sie ein Krankenhaus nur für Mädchen. Deshalb muss sie aus Afghanistan fliehen. Welches der beiden Fluchmittel soll sie benutzen?", 431, 450)
    fill(0, 0, 0)

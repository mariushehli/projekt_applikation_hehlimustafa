def setup():
    size(862, 500)
    photo = loadImage("IMG_1522.jpg")
    image(photo, 0, 0)
    photo.resize(862, 500)
    image(photo, 0, 0)
    rect(10,380,840,100)
    
def draw():
    fill(0, 0, 0)
    textSize(18)
    textAlign(CENTER)
    text("Start: Fatima lebt in Afghanistan. Sie will kein Kopftuch tragen.\nDazu betreibt sie ein Krankenhaus nur für Mädchen.\nDeshalb muss sie aus Afghanistan fliehen.\nWelches der beiden Fluchmittel soll sie benutzen?", 431, 400)
    fill(255, 255, 255)
    

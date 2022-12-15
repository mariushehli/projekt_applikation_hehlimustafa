#Karte als Hintegrundbild----------------------------------------------------
def setup():
    size(862, 500)
    photo = loadImage("IMG_1522.jpg")
    image(photo, 0, 0)
    photo.resize(862, 500)
    image(photo, 0, 0)
    global step 
    step = 0
#Textfeld------------------------------------------------------------------
   
    
#Text----------------------------------------------------------------------
def draw():
    print(mouseX, mouseY)
    global step
    if step == 0:
        # Textfeld für ersten Schritt zeichnen (Text soll text für Anfang des Spiels sein)
        rect(10,380,840,100)
        fill(0, 0, 0)
        textSize(16)
        textAlign(CENTER)
        text("step: " + str(step) + " " + getTextForStep() , 431, 400)
        fill(255, 255, 255)
        
# wird aufgerufen, wenn eine Taste gedrückt wird
def keyPressed():
    # Schritt setzen (jeder Knoten in eurem Spiel hat eine "ID", das ist der step)
    global step
    lastStep = step
    if keyCode == LEFT:
        if step == 0:
            step = 1
        elif step == 1: #wenn im Iran mit Bus
            step = 3    #dann mit Pfeiltaste links direkt nach Türkei
        elif step == 2: #wenn im Iran mit Auto
            step = 3 #dann mit Pfeiltaste links nach Türkei 
        elif step == 3: #wenn direkt in Türkei
            step = 5 #dann mit Pfeiltaste links nach Rumänien
        elif step == 4: #wenn über Georgien in Türkei
            step = 5 #dann nach Rumänien
        elif step == 5: #wenn in Rumänien
            step = 7 #dann mit Pfeiltaste links über Serbien nach Kroatien
        elif step == 6: #wenn in Griechenland
            step = 9 #dann über Italien in die Schweiz
        elif step == 7: #wenn in Kroatien
            step = 10 #dann über Österreich in die Schweiz
    if keyCode == RIGHT:
        if step == 0: #wenn von Start
            step = 2 #dann mit Pfeiltaste rechts nach Iran mit Auto
        elif step == 1: #wenn im Iran mit Bus
            step = 4 #dann mit Pfeil rechts über Georgien nach Türkei
        elif step == 2: #wenn im Iran mit Auto
            step = 4 #dann mit Pfeil rechts über Georgien nach Türkei
        elif step == 3: #wenn direkt in Türkei
            step = 6 #dann mit Pfeiltaste rechts nach Griechenland
        elif step == 4: #wenn über Georgien nach Türkei
            step = 6 #dann nach Griechenland
        elif step == 5: #wenn in Rumänien
            step = 7 #dann über Ungarn nach Kroatien
        elif step == 6: #wenn in Griechenland
            step = 7 #dann über Balkanroute nach Kroatien
        elif step == 7: #wenn in Kroatien
            step = 10 #dann über Österreich in die Schweiz 
        
    # Textfeld neu zeichnen und mit aktualisierten Text entsprechend des steps füllen (Text kann nicht entfernt werden, muss immer überzeichnet werden)
    rect(10,380,840,100)
    fill(0, 0, 0)
    textSize(16)
    textAlign(CENTER)
    # für den step (Knoten) der entspr. Text schreiben mit getTextForStep()
    text("step: " + str(step) + " " + getTextForStep() , 431, 400)
    fill(255, 255, 255)
    # linie hinzufügen für entspr. step
    drawLineForStep(lastStep)
        
# Für jeden Knoten (step) einen Text zurückgeben
def getTextForStep():
    global step
    if step == 0:
        return "START"
    if step == 1:
        return "STEP 1"
    # und so weiter
    return ""
     
# für jeden Knoten (step) eine Linie zeichnen
# z.B. wenn die erste Entscheidung = RECHTS ist, dann wäre das der Step 1, dann müsst ihr also die linie dafür zeichnen
# vmtl. müsst ihr noch eine variable lastStep haben, damit ihr entscheiden könnt, von wo nach wo die linie geht
def drawLineForStep(lastStep):
    global step
    if step == 1:
        line(700, 400, 525, 350)
    elif step == 2:
        line(700, 400, 525, 350)
    elif step == 3:
        if lastStep == 1:
            line(525, 350, 400, 300)
        elif lastStep == 2:
            line(525, 350, 400, 300)
    elif step == 4:
        if lastStep == 1:
            line(525, 350, 500, 240) 
            line(500, 240, 400, 300)
        elif lastStep == 2:
            line(525, 350, 500, 240) 
            line(500, 240, 400, 300)
    elif step == 5:
        if lastStep == 3:
            line(400, 300, 300, 180)
        elif lastStep == 4:
            line(400, 300, 300, 180)
    elif step == 6:
        if lastStep == 3:
            line(400, 300, 210, 280)
        elif lastStep == 4:
            line(400, 300, 210, 280)
    elif step == 7:
        if lastStep == 6:
            line(210, 280, 100, 170)
        elif lastStep == 5:
            line(300, 180, 150, 210)
            line(150, 210, 100, 170)
    elif step == 9:
        if lastStep == 6:
            line(210, 280, 130, 270)
            line(130, 270, 25, 135)
    elif step == 10:
        if lastStep == 7:
            line(100, 170, 25, 135)

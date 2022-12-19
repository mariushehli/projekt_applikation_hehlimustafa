#Karte als Hintegrundbild----------------------------------------------------------------------------
def setup():
    size(862, 500)
    photo = loadImage("IMG_1522.jpg")
    image(photo, 0, 0)
    photo.resize(862, 500)
    image(photo, 0, 0)
    global step 
    step = 0
#Textfeld----------------------------------------------------------------------------------------------
def draw():
    print(mouseX, mouseY)
    global step
    if step == 0:
        #Textfeld für Startschritt zeichnen (Schritt 0/Aufrufen des Programms)
        rect(0,380,862,200)
        fill(0, 0, 0)
        textSize(16)
        textAlign(CENTER)
        text("Schritt: " + str(step) + " " + getTextForStep() , 431, 400)
        fill(255, 255, 255)
    
#Schritte werden aufgerufen, wenn eine Taste gedrückt wird (links oder rechts)-------------------------
def keyPressed():
    #Schritt setzen (jeder Knoten hat einen Step)---
    global step
    lastStep = step
    #Entscheidungen linke Pfeiltaste---
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
    #Entscheidungen rechte Pfeiltaste---
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
            step = 8 #dann über Ungarn nach Kroatien
        elif step == 6: #wenn in Griechenland
            step = 7 #dann über Balkanroute nach Kroatien
        elif step == 7: #wenn in Kroatien über Balkanroute
            step = 10 #dann über Österreich in die Schweiz 
        elif step == 8: #wenn in Kroatien über Ungarn
            step = 10 #dann über Österreich in die Schweiz
        
    # Textfeld neu zeichnen und mit aktualisierten Text entsprechend des Schritts füllen (Überschreibung)----
    rect(0,380,862,200)
    fill(0, 0, 0)
    textSize(16)
    textAlign(CENTER)
    #Für den Schritt (Knoten) den entspr. Text schreiben
    text("Schritt: " + str(step) + " " + getTextForStep() , 431, 400)
    fill(255, 255, 255)
    #Linie hinzufügen für entspr. step
    drawLineForStep(lastStep)
        
#Für jeden Knoten (step) einen Text zurückgeben----------------------------------------------------------------
def getTextForStep():
    global step
    if step == 0:
        return "START\nFatima lebt in Afghanistan. Sie will kein Kopftuch tragen. Dazu betreibt sie ein Krankenhaus nur fuer Maedchen.\nDeshalb muss sie aus Afghanistan fliehen. Welches der beiden Fluchmittel soll sie benutzen?\nPfeil Links: Auto; Pfeil rechts: Bus"
    if step == 1:
        return "Puh, Glueck gehabt! Ein Freund hat dich in seinem Auto mitgenommen. Ihr seid an der Grenze zwar kontrolliert worden,\njedoch hat niemand Verdacht geschoepft. Nun stellt sich dir eine zweite Frage:\nWillst du weiter in die Tuerkei, ein muslimisches Land, oder ueber Georgien in die Ukraine?\nPfeil Links: Tuerkei; Pfeil Rechts: Ukraine"
    if step == 2:
        return "Puh, Glueck gehabt! Du bist in einen Bus gestiegen, der an der Grenze zum Iran kontrolliert wurde.\n Du hast dich aber kooperativ verhalten und die Grenzer haben keinen Verdacht geschoepft. Nun stellt sich die zweite Frage:\nWillst du weiter in die Tuerkei, ein muslimisches Land, oder ueber Georgien in die Ukraine?\n Pfeil Links: Tuerkei; Pfeil Rechts: Ukraine"
    if step == 3: 
        return "Du hast es direkt mithilfe eines progressiven Taxifahrers nach Istanbul geschafft. Als du jedoch ausgestiegen bist, haben\nihn Polizisten verhaftet und wegen Beihlife zur Flucht eingesperrt. Du konntest fliehen. Du stehst nun vor einer wichtigen Frage:\nNimmst du den Weg ueber das Schwarze Meer nach Rumaenien oder gehst du zu Fuss nach Griechenland?\nPfeil Links: Rumaenien; Pfeil Rechts: Griechenland"
    if step == 4:
        return "Ach du Schande! Gerade, als du in Georgien angekommen bist, hat dich die Meldung vom Krieg in der Ukraine erreicht.\n Du musst umkehren und in die Tuerkei zurueck. Dein Fussweg betrug rund drei Wochen und du bist voellig fertig.\nDu stehst nun vor einer wichtigen Frage: Nimmst du den Weg ueber das Schwarze Meer nach Rumaenien\noder gehst du zu Fuss nach Griechenland? Pfeil Links: Rumaenien; Pfeil Rechts: Griechenland"
    if step == 5:
        return "Du hast einem Schlepper 2000 Euro fuer die Ueberfahrt nach Rumaenien bezahlt.\nDas Boot versank fast und du hast ueberlebt, leider aber nicht alle deine Mitstreiter:innen. Jetzt musst du dich entscheiden:\nGehst du ueber Ungarn nach Kroatien oder ueber Serbien?\nPfeil links: Serbien; Pfeil Rechts: Ungarn"
    if step == 6:
        return "Du hast es nach Griechenland geschafft. Nun musst du dich erneut fragen:\nWaehlst du den Weg uebers Meer nach Italien oder absolvierst du zu Fuss den Weg ueber die Balkanroute nach Kroatien?\n Pfeil links: Italien; Pfeil rechts: Balkanroute"
    if step == 7:
        return "Du hast es nach Kroatien geschafft. An den Grenzen wurdest du immer wieder zurueckgedraengt,\nkonntest dich aber schlussendlich immer durchschleichen.\nNun steht dir der Weg in die Schweiz via Zug offen! Druecke dafuer die eine der Pfeiltasten."
    if step == 8:
        return "Du hast es nach Kroatien geschafft. Die Ungarische Polizei hat dich eingesperrt,\ndich aber nach zwei Tagen wieder freigelassen. Druecke die rechte Pfeiltaste um den Zug zu nehmen."
    if step == 9:
        return "Du hast es im Zug bis in die Schweiz geschafft. Endlich bist du angekommen!"
    if step == 10:
        return "Du hast es im Zug bis in die Schweiz geschafft. Endlich bist du angekommen!"
        
#Für jeden Schritt (Knoten) eine Linie zeichnen
#Bspw. wenn die erste Entscheidung = RECHTS ist, dann ist das der Schritt 1------------------------------------------------
def drawLineForStep(lastStep):
    global step
    if step == 1:
        line(700, 370, 525, 350)
    elif step == 2:
        line(700, 370, 525, 350)
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
    elif step == 8:
        if lastStep == 5:
            line(300, 180, 170, 140)
            line(170, 140, 100, 170)
    elif step == 9:
        if lastStep == 6:
            line(210, 280, 130, 270)
            line(130, 270, 25, 135)
    elif step == 10:
        if lastStep == 7:
            line(100, 170, 25, 135)
        if lastStep == 8:
            line(100, 170, 25, 135)
            
        

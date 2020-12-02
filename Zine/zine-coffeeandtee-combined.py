# INSTALL THE TYPEFACE 'MIGHTY MONO' BEFORE RUNNING THIS

# IMPORT LIBRARY
from random import randrange
import datetime
from datetime import date


#################################
# DEFINE BROWN COLOUR
c, m, y, k, a = 0, 50, 70, 60, 1


#################################
###### PAGE: COVER (COFFEE & TEE)

# DRAW NEW PAGE
newPage('A5')

# DRAW WALLPAPER
cmykFill(c/255, m/255, y/255, k/255, 0.2)
rect(0, 0, width(), height())

# DEFINE LAYER SPECS
inch = 72
w = 5.8*inch
h = 8.3*inch
layerSize = h * 0.5
numLayers = 100
dist = 1.5

# DEFINE FRAME NUMBERS
numFrames = 1

# LOOP FRAMES, ROTATE
for frame in range(numFrames):
    phase = 2 * pi * frame / numFrames 
    startAngle = 360 - (135 * sin(phase))
    #startAngle = 135 * sin(phase)
    endAngle = 135 * cos(phase + pi * .5)
    frameDuration(1/20)
    translate(w/2, h/4 - h/3)

# LOOP LAYERS IN A FRAME
    for i in range(numLayers + 1):
        f = i / numLayers
        
        with savedState():
            translate(0, i * dist * 1.5)
            rotate(startAngle + f * (endAngle - startAngle))
            
            # STYLE THE TITLE TEXT
            cmykFill(c/255, m/255, y/255, k/255, 0.3)    
            cmykStroke(c/255, m/255, y/255, k/255, 0.8)
            # INSERT IMAGE
            #scale(.5)
            im = ImageObject('caphesuada-A5.png')
            im.sepiaTone(.5)
            image(im, (-im.size()[0]/2, -im.size()[1]/2), .1)
            
            # FILL THE TOP LAYER OF TITLE TEXT
            if i == numLayers:
                cmykFill(0, 0, 0, 0, 1)
                #cmykFill(c/255, m/255, y/255, k/255, 1)
            font('Mighty Mono Bold')
            fontSize(w/6)
            translate(0, w/6)
            textBox("Coffee" + "\n" + "&"+ "\n" + "Tee", (-layerSize/2, -layerSize/2, layerSize, layerSize), align="center")
            
            
#################################    
###### PAGE: COFFEE-ADDICT

# DRAW NEW PAGE
newPage('A5')

# DRAW BACKGROUND
cmykFill(c/255, m/255, y/255, k/255, 0.2)
rect(0, 0, width(), height())

# CREATE SPIRAL
for angle in range(180, 360, 1):
    translate(width()/2, height()/2)
    for i in range(50):
        cmykFill(c/255, m/255, y/255, k/255, 0.7)
        font('Mighty Mono Regular')
        fontSize(80)
        text('a coffee-addict', (0, 0))
        scale(.95)
        rotate(angle/15)


#################################
###### PAGE: COFEE MENU

# DRAW NEW PAGE
newPage('A5')

# DEFINE PAGE & CARD SIZE
inch = 72
margin = 0.25*inch
fullWidth = 5.8*inch
fullHeight = 8.3*inch
dimensions = (fullWidth, fullHeight)
cardWidth = dimensions[0]-margin
cardHeight = dimensions[1]-margin

# DEFINE FUNCTION: DRAW CARD
def drawCard(cardWidth, cardHeight):
    cmykFill(0, 0, 0, 0)
    rect(margin, margin, cardWidth - margin, cardHeight - margin)

# DEFINE FUNCTION: WRITE TITLE
def writeTitle():
    font('Mighty Mono Bold')
    fontSize(cardWidth/23)
    textBox('What does Tee wanna drink?', (margin*3, margin, cardWidth-margin, cardHeight-margin*2.6))

# DEFINE FUNCTION: WRITE ANSWER
def writeMenu():
    # QUESTIONS
    font('Mighty Mono Light')
    fontSize(cardWidth/36)
    lineHeight(cardWidth/36 + 5)
    textBox('Step 1. Choose coffee type', (margin*3, margin, cardWidth-margin, cardHeight-margin*4.5))
    textBox('Step 2. Choose hot/iced', (margin*3, margin, cardWidth-margin, cardHeight-margin*21))
    textBox('Step 3. Choose sugar level', (margin*3, margin, cardWidth-margin, cardHeight-margin*24.25))
    textBox('Too many options, can\'t decide?\nUse the randomiser! → → →', (margin, margin, cardWidth-margin*3, cardHeight-margin*28.75), align="right")
    # OPTIONS
    font('Mighty Mono Regular')
    fontSize(cardWidth/30)
    lineHeight(cardWidth/30 + 5)
    textBox('□ Latte\n□ Flat White\n□ Long Black\n□ Cappucino\n□ Expresso\n□ Macchiato\n□ Mocha\n□ Piccolo\n□ Double Ristretto\n□ Magic\n□ Affogato\n□ Dalgona Coffee\n□ Cà Phê Sữa\n□ Coffee Milk with Boba', (margin*3, margin, cardWidth-margin, cardHeight-margin*5.5))
    textBox('□ Hot       □ Iced', (margin*3, margin, cardWidth-margin, cardHeight-margin*22))
    textBox('□ Normal    □ Less    □ Half\n□ Little    □ No', (margin*3, margin, cardWidth-margin, cardHeight-margin*25.25))
    
# DRAW CURVE BACKGROUND
cmykFill(c/255, m/255, y/255, k/255, random())
rect(0, 0, width(), height())
baseColor = [c/255, m/255, y/255, k/255]
bandHeight = fullHeight
for row in range(30):
    cmykFill(*baseColor)
    thisColor = baseColor.copy()
    thisColor[randrange(-2, 1)] = random()
    cmykFill(*thisColor)
    myPath = BezierPath()
    myPath.moveTo((0, 0))
    myPath.lineTo((width(), 0))
    myPath.lineTo((width(), bandHeight))
    myPath.curveTo(
        (0, bandHeight),
        (width()/2, randrange(-50, 10)),
        (0, bandHeight)        
        )
    myPath.closePath()
    drawPath(myPath)
    bandHeight -= cardHeight/30

# DRAW CARD
cmykFill(0, 0, 0, 0)
drawCard(cardWidth, cardHeight)

# WRITE TEXT
cmykFill(0, random(), random(), 0.5)
writeTitle()
writeMenu()


#################################
###### PAGE: COFFEE RANDOMISER

# DRAW NEW PAGE
newPage('A5')

# DEFINE PAGE & CARD SIZE
inch = 72
margin = 0.25*inch
fullWidth = 5.8*inch
fullHeight = 8.3*inch
dimensions = (fullWidth, fullHeight/3)
cardWidth = dimensions[0]-margin
cardHeight = dimensions[1]-margin

# DEFINE VARIABLES
temperature= ['Hot', 'Iced']
coffee= ['Latte', 'Flat White', 'Long Black', 'Cappucino', 'Expresso', 'Macchiato', 'Mocha', 'Piccolo', 'Double Ristretto', 'Magic', 'Affogato', 'Dalgona Coffee', 'Cà Phê Sữa', 'Coffee Milk with Boba']
sugar = ['Normal', 'Less', 'Half', 'Little', 'No']
#drink = choice(temperature) + "\n" + choice(coffee) + "\n" + choice(sugar) + " " + "Sugar"

# DEFINE FUNCTION: DRAW CARD
def drawCard(cardWidth, cardHeight):
    cmykFill(0, 0, 0, 0)
    rect(margin, margin, cardWidth - margin, cardHeight - margin)

# DEFINE FUNCTION: WRITE DATE AND TIME
def writeTime():
    font('Mighty Mono Light')
    fontSize(cardWidth/36)
    now = datetime.datetime.now()
    textBox('Date' + " " + now.strftime("%d-%m-%Y") + "   " + 'Time' + " " + now.strftime("%H:%M"), (margin, margin, cardWidth-margin*2, cardHeight-margin*8.5), align="right")

# DEFINE FUNCTION: WRITE QUESTION
def writeQuestion():
    font('Mighty Mono Light')
    fontSize(cardWidth/32)
    textBox('What coffee should Tee drink today?', (margin*2, margin, cardWidth-margin*2, cardHeight-margin*2))

# DEFINE FUNCTION: WRITE ANSWER
def writeAnswer():
    font('Mighty Mono Bold')
    fontSize(cardWidth/18)
    lineHeight(cardWidth/18 + 5)
    textBox(drink, (margin*2, margin, cardWidth-margin, cardHeight-margin*4))

rows = 3
cols = 1

for row in range(rows):
    for col in range(cols):
        # DRAW BACKGROUND FOR EACH BOX
        cmykFill(c/255, m/255, y/255, k/255, random())
        rect(0, 0, width(), height())
        baseColor = [c/255, m/255, y/255, k/255]
        bandHeight = cardHeight
        for row in range(10):
            cmykFill(*baseColor)
            thisColor = baseColor.copy()
            thisColor[randrange(-2, 1)] = random()
            cmykFill(*thisColor)
            myPath = BezierPath()
            myPath.moveTo((0, 0))
            myPath.lineTo((width(), 0))
            myPath.lineTo((width(), bandHeight))
            myPath.curveTo(
                (0, bandHeight),
                (width()/2, randrange(-10, 0)),
                (0, bandHeight)        
                )
            myPath.closePath()
            drawPath(myPath)
            bandHeight -= cardHeight/10

        cmykFill(0, 0, 0, 0)
        #rect(0, 0, width(), height())
        # DRAW CARDS, WRITE TIME & QUESTION
        drawCard(cardWidth, cardHeight)
        cmykFill(0, random(), random(), 0.5)
        writeTime()
        writeQuestion()
        
        # CHOOSE & WRITE A RANDOM ANSWER
        with savedState():
            #drink = choice(coffee) + " \n" + choice(temperature) + " • " + choice(sugar) + " " + "Sugar" 
            drink = choice(temperature) + " " + choice(coffee) + " " + "\n" + choice(sugar) + " " + "Sugar" 
            writeAnswer()
        
    translate(0, dimensions[1])         
              
                
#################################    
###### PAGE: CA PHE PHIN

# DRAW NEW PAGE
newPage('A5')
margin = 30
        
# IMPORT IMAGE
im = ImageObject('caphesuada-A5.png')
w, h = im.size()

# DRAW BACKGROUND
cmykFill(c/255, m/255, y/255, k/255, 0.3)
rect(0, 0, width(), height())

# CREATE EFFECT FOR IMAGE
with savedState():
    im.zoomBlur(center=(width()/2, height()/2), amount=15)
    translate(width()/2, height()/2)
    scale(.6)
    image(im, (-im.size()[0]/2, -im.size()[1]/2))

# WRITE CAPTION
cmykFill(c/255, m/255, y/255, 0.5, 1)
font('Mighty Mono Light')
fontSize(width()/36)
lineHeight(width()/36 + 5)
textBox('This is when Tee has too much Vietnamese coffee\n(cà phê sữa đá) or when Drawbot keeps crashing.', (margin, margin, width()-margin*2, height()/12), align="center")   


#################################
###### PAGE: COFFEE SPILL PATTERN

# DRAW NEW PAGE
newPage('A5')

# DRAW BACKGROUND
cmykFill(c/255, m/255, y/255, k/255, 0.3)
rect(0, 0, width(), height())

# DEFINE POSITION OF STARTING POINT
x = 0
y = 0

#DEFINE HOW MANY ROWS AND COLUMNS
rows = 20   
cols = 20

# DEFINE WIDTH AND HEIGHT OF EACH UNIT OF THE GRID
gridWidth = 200
gridHeight = 150

# SET DIAMETER MIN/MAX VALUE
diamMin = 5
diamMax = 50

# CREATE LOOP & DRAW THE DOTS
for row in range(rows):
    for col in range(cols):
        diam = randrange(diamMin, diamMax)
        if random() > .5:
            blendMode("multiply")
            cmykFill(c/255, m/255, y/255, k/255, 0.5)
            oval(x, y, diam, diam)
        else:
            blendMode("multiply")
            cmykFill(c/255, m/255, y/255, k/255, 0.8)
            oval(x, y, diam/2, diam/2)
        x += diam
        y += randrange(-10,100)

saveImage('thy-ha-zine-coffeeandtee.pdf')
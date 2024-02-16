e=0
ee=0
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter): 
    testX = cx
    testY = cy
    if cx < rx:
        testX = rx
    elif cx > rx+rw:
        testX = rx+rw
    if cy < ry:
        testY = ry
    elif cy > ry+rh:
        testY = ry+rh
    distance = dist(cx,cy,testX,testY)
    if distance <= diameter/2:
        return True
    else:
        return False
def setup():
    size(800, 800)

def draw():
    global e,ee
    background(123,234,0)
    if collideRectCircle(0,200, 600, 100, e, ee, 10):
        fill(255,0,0)
    elif collideRectCircle(200,400, 600, 100, e, ee, 10):
        fill(255,0,0)
    elif collideRectCircle(0,600, 600, 100, e, ee, 10):
        fill(255,0,0)
    else:
        fill(255)
   
    rect(0,200, 600, 100)
    rect(200,400, 600, 100)
    rect(0,600, 600, 100)
    ellipse(e, ee, 10, 10)
    if keyPressed:
        if key == 'w':
            ee=ee-1
        if key == 's':
            ee=ee+1
        if key == 'a':
            e=e-1
        if key == 'd':
            e=e+1

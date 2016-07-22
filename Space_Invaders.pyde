
aliens = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1] , [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
bulletList = []
varY = 50
varX = 50
bulletX = 50
bulletY = 565
playerX = 250
bulletFired = False


counter = 0
def setup():
    size(700, 600)
    background(0)
    
def draw():
    global varX, varY, aliens, playerX, bulletY, bulletX, bulletFired, counter
    background(0)
    rect(playerX, 565, 30, 30)
    
    # Draws the T-Swiftians
    for i in range(len(aliens)):
        for j in range(len(aliens[i])):
            #ellipse(varX + i * 55, varY, 40, 40)
            ellipse(varX + i * 45, varY + j *60, 30, 30)
            #varY = varY + .01
    
    
    
    
    # Makes the Player move LEFT                
    if keyPressed == True:
        if keyCode == 37:
            playerX = playerX - 10

    
    # Makes the Player move RIGHT                     
    if keyPressed:
        if keyCode == 39:
            playerX = playerX + 10 
            
                # Makes the Player Shoot A bullet
        if keyCode == 0:
        
            if bulletFired == False:
                bulletX = playerX
                bulletFired = True

    if bulletFired == True:
        rect(bulletX, bulletY, 10, 10)
        bulletY = bulletY - 8
        if bulletY < 100:
            bulletFired = False 
            bulletY = 565
            
    #if bulletY >= varX and varY:
        
        
              
        
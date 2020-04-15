# Crown Geen Bowling
#!/usr/bin/env python
# by Thos Tibbetts  2019
#                                  unfinnished

import random, pygame, sys, time,math
from pygame.locals import*

FPS = 30   ##15
WINDOWWIDTH = 1280   ##width
WINDOWHEIGHT = 900   ##height
HALF_WINDOWWIDTH=int(WINDOWWIDTH/2)
HALF_WINDOWHEIGHT=int(WINDOWHEIGHT/2)
#             R    G    B    
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 142,   0)  # B/G col
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
YELLOW    = (255, 255,   0)
PPUPLE    = (255, 209, 255)
PBLUE     = (156, 255, 255)
PYELLOW   = (255, 255, 169)
BLUE      = (  0,   0, 255)
BGCOLOR = BLACK

pygame.init()
scoreR=0
scoreB=0
ends=0
bowlx = 0
bowly = 0
jack =0
red = 0
blue = 0

FPSCLOCK = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('ReBowl.png')) 
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
BIGFONT=pygame.font.Font('freesansbold.ttf', 36)
pygame.display.set_caption('**Crown Green Bowls**')
titleFont = pygame.font.Font('freesansbold.ttf', 100)
BlueB_SURF=pygame.image.load('BlBowl.png').convert()
RedB_SURF=pygame.image.load('ReBowl.png').convert()
backDrop_SURF=pygame.image.load('bowlGreen.png').convert()
backDropTwo_SURF = pygame.image.load('bowlGreenTwo.png').convert()
Ted_SURF=pygame.image.load('tedBowl.png').convert()
Jack_SURF=pygame.image.load('jack.png').convert()
Start_SURF=pygame.image.load('BowlStart.png').convert()
Score_SURF=pygame.image.load('scores.png').convert()
patch_SURF=pygame.image.load('grePatch.png').convert()
hitObj = pygame.mixer.Sound('bowlHit.wav')
hitBBObj = pygame.mixer.Sound('bowlHitNew.wav')
rulesPic=pygame.image.load('instructGreen.png').convert()
def finnish():
    pygame.quit()
    sys.exit()
def checkForQuit():
    for event in pygame.event.get(QUIT): 
        finnish()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            finnish()
        pygame.event.post(event)

def redWin():
    startKeyFont=pygame.font.Font('freesansbold.ttf', 56)
    startKeySurf=startKeyFont.render('*RED IS THE WINNER*', True, RED)
    startKeyRect = startKeySurf.get_rect()
    startKeyRect.midtop =(WINDOWWIDTH /2, 400)
    DISPLAYSURF.blit(startKeySurf, startKeyRect)
    pygame.display.update()     
    pygame.time.wait(9000)

def blueWin():
    waitKeyFont=pygame.font.Font('freesansbold.ttf', 56)
    waitKeySurf=waitKeyFont.render('*BLUE IS THE WINNER*', True, BLUE)
    waitKeyRect = waitKeySurf.get_rect()
    waitKeyRect.midtop =(WINDOWWIDTH /2, 400)
    DISPLAYSURF.blit(waitKeySurf, waitKeyRect)
    pygame.display.update()     
    pygame.time.wait(9000)    
        
def scores():
    global jack, red , blue, ends, jackObj, jackCopy ,scoreR, scoreB
    DISPLAYSURF.blit(Score_SURF, (5, 5))     
    scoreRSurf=BIGFONT.render(';  ' + str(scoreR), True, RED)###ok
    scoreRRect=scoreRSurf.get_rect()
    scoreRRect.topleft=(WINDOWWIDTH-1110, 250)
    DISPLAYSURF.blit(scoreRSurf, scoreRRect)
    scoreBSurf=BIGFONT.render(';  ' + str(scoreB), True, BLUE)###ok
    scoreBRect=scoreBSurf.get_rect()
    scoreBRect.topleft=(WINDOWWIDTH-1110, 326)
    DISPLAYSURF.blit(scoreBSurf, scoreBRect)
    endsSurf=BIGFONT.render(':  ' + str(ends), True, GREEN)###ok
    endsRect=endsSurf.get_rect()
    endsRect.topleft=(WINDOWWIDTH-1110, 406)
    DISPLAYSURF.blit(endsSurf, endsRect)     
    
RATE=300
LEGNTH=0
END = 0
green = 0
HITS =0
ball = 0 
jackObjRect= 0
leRi=0
jposx = 0
jposy = 0
bposx = 0
bposy = 0
rposx = 0
rposy = 0
btposx = 0
rHja = 0  
bHja = 0
#def getPath(currentBounce,Rate, legnth):##
   # return int(math.sin((math.pi/float(Rate))* currentBounce)*legnth)##
def getPath(speed,Rate, legnth):##
    return int(math.sin((math.pi/float(Rate))* speed)*legnth)##

BOWLSIZE = 21            
image = pygame.image.load('jack.png').convert()            
jackObj = {'surface':image,'size':BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}
jackObj['rect'] = pygame.Rect ((jackObj['x'] ,
                                jackObj['y'] - getPath(jackObj['speed'], RATE, LEGNTH),##
                                jackObj['size'], jackObj['size']))         
jackObjRect = jackObj['rect']


class bowlHitJ(pygame.sprite.Sprite):      # ballObj = redObj / jackObj / blueObj
    def __init__(self,ball, posx, posy):  # ball ,image  = jack_SURF, RedB_SURF ,BlueB_SURF   
        pygame.sprite.Sprite.__init__(self)
        self.image = ball  #  jack  blue  red
        #print ('  x  ',   posx )  #test
        #print (' y '  ,  posy) 
        global ends, red, jack, blue,jackCopy , redObjrect
        global leRi, jposx, jposy, rposx, rposy,bHja, rHja
        rbjimg = ball#Jack_SURF
        move = 0
        redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h
        blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h        
        rbjx = posx
        rbjy = posy
        direction = 'up'        
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))
            move += 1
            if direction == 'up':                
                rbjx += leRi  ##leRi#  -4 left / right 4
                rbjy -= 6 
            DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
            jposx = rbjx
            jposy = rbjy
            #print ('  x  ',   rbjx ) # test
            #print (' y '  ,  rbjy)
            jack_RECT = pygame.Rect(jposx, jposy, 22, 22) #x and y , size x  size  y  A            
            pygame.display.update()
            if rHja > 2:                # red hit jack more than 2
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))                
                rposx
                rposy
                bposx
                bposy                                                                        
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok                
                gameStart()
                
            if bHja > 2:                      # blue Hit jack more than 2
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))                
                rposx
                rposy
                bposx
                bposy                                                                        
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok                                 
                gameStart()
                
            if move ==6: # 8 
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
                jackCopy = DISPLAYSURF.copy()
                jposx = rbjx
                jposy = rbjy                
                pygame.display.flip()
                gameStart()
                
            if jack_RECT.colliderect(redObjRect):#  jack hit red one 
                hitBBObj.play(20, 0 ,0)
                rHja += 1
                rposx
                rposy
                bposx
                bposy                                                                        
                DISPLAYSURF.blit(patch_SURF, (rposx, rposy))                
                END = 540  # 540
                ENDR = 1000
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitR(RedB_SURF, rposx, rposy)
                
            if jack_RECT.colliderect(blueObjRect):#  jack hit blue one
                hitBBObj.play(20, 0 ,0)
                bHja += 1 
                rposx
                rposy
                bposx
                bposy                                                                                        
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))              
                END = 540  # 540
                ENDR = 1000
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitB(BlueB_SURF, bposx, bposy)                
            FPSCLOCK.tick(FPS)

class bowlHitRtwo(pygame.sprite.Sprite):   #red bowl two  
    def __init__(self,ball, posx, posy):  # ball ,image  = jack_SURF,/ RedB_SURF ,/BlueB_SURF   
        pygame.sprite.Sprite.__init__(self)
        self.image = ball  #  jack  blue  red
        #print (' x  / b h 1 pos  ',   posx )  #  test
        #print (' y  / b h 1 pos'  ,  posy) 
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect
        global leRi, bposx, bposy, rposx, rposy
        rbjimg = ball#Jack_SURF
        move = 0
        rbjx = posx
        rbjy = posy
        direction = 'up'        
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))
            move += 1            
            if direction == 'up':                
                rbjx += leRi  ##leRi#  -4 left / right 4
                rbjy -= 6 
            DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
            posx = rbjx
            posy = rbjy
            
            pygame.display.update()                                
            if move ==6: 
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
                jackCopy = DISPLAYSURF.copy()
                rtposx = rbjx
                rtposy = rbjy
                #print ('rtposx boHit 2',     rtposx)  #test
                #print ('rtposy boHit 2'  ,   rtposy)                
                pygame.display.flip()
                gameStart()                
            FPSCLOCK.tick(FPS)             

class bowlHitR(pygame.sprite.Sprite):   #red bowl one  
    def __init__(self,ball, posx, posy):  # ball ,image  = jack_SURF,/ RedB_SURF ,/BlueB_SURF   
        pygame.sprite.Sprite.__init__(self)
        self.image = ball  #  jack  blue  red
        #print (' x  / new pos  ',   posx )  #  tyest
        #print (' y  / new pos'  ,  posy) 
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect
        global leRi, bposx, bposy, rposx, rposy, red_RECT, jackObjRect
        rbjimg = ball#Jack_SURF         
        move = 0
        rbjx = posx
        rbjy = posy
        direction = 'up'        
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))
            move += 1            
            if direction == 'up':                
                rbjx +=leRi  ##leRi#  -4 left / right 4
                rbjy -= 6 
            DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
            rposx = rbjx
            rposy = rbjy
            red_RECT = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  A
            jackObjRect = pygame.Rect(jposx, jposy, 22, 22) #x and y , size x  size  y  A             
            pygame.display.update()                                
            if move ==6: 
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
                jackCopy = DISPLAYSURF.copy()
                rposx = rbjx
                rposy = rbjy
                #print ('rposx boHit',     rposx)
                #print ('rposy boHit'  ,   rposy)     #test           
                pygame.display.flip()
                gameStart()
                
            if red_RECT.colliderect(jackObjRect):#  red hit jack 
                hitBBObj.play(20, 0 ,0)
                jposx
                jposy
                rposx
                rposy                                                                        
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitJ(Jack_SURF, jposx, jposy)
                
            if red_RECT.colliderect(blueObjRect):#  red hit blue one ok
                hitBBObj.play(20, 0 ,0)
                rposx
                rposy
                bposx
                bposy                                                                                        
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))              
                END = 540  # 540
                ENDR = 1000
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitB(BlueB_SURF, bposx, bposy) 
                
            FPSCLOCK.tick(FPS)

class bowlHitBtwo(pygame.sprite.Sprite):   #red bowl two  
    def __init__(self,ball, posx, posy):  # ball ,image  = jack_SURF,/ RedB_SURF ,/BlueB_SURF   
        pygame.sprite.Sprite.__init__(self)
        self.image = ball  #  jack  blue  red
        #print (' x  / r h 1 pos  ',   posx )
        #print (' y  / r h 1 pos'  ,  posy)   # test
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect
        global leRi, bposx, bposy, rposx, rposy, btposx, btposy
        rbjimg = ball#Jack_SURF
        move = 0
        rbjx = posx
        rbjy = posy
        direction = 'up'        
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))
            move += 1            
            if direction == 'up':                
                rbjx += leRi  ##leRi#  -4 left / right 4
                rbjy -= 6 
            DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
            posx = rbjx
            posy = rbjy
            
            pygame.display.update()                                
            if move ==6: 
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
                jackCopy = DISPLAYSURF.copy()
                btposx = rbjx
                btposy = rbjy
                #print ('rtposx boHit 2',     rtposx)
                #print ('rtposy boHit 2'  ,   rtposy)     #test           
                pygame.display.flip()
                gameStart()                
            FPSCLOCK.tick(FPS)             

class bowlHitB(pygame.sprite.Sprite):  
    def __init__(self,ball, posx, posy):  # ball ,image  = jack_SURF, RedB_SURF ,BlueB_SURF   
        pygame.sprite.Sprite.__init__(self)
        self.image = ball  #  jack  blue  red
        #print ('  x  ',   posx )
        #print (' y '  ,  posy) # test
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect
        global leRi, bposx, bposy, LeRi
        rbjimg = ball#Jack_SURF
        move = 0
        rbjx = posx
        rbjy = posy
        direction = 'up'        
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))
            move += 1            
            if direction == 'up':                
                rbjx += leRi  ##leRi#  -4 left / right 4
                rbjy -= 6
            DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
            bposx = rbjx
            bposy = rbjy
            blue_RECT = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  A
            jackObjRect = pygame.Rect(jposx, jposy, 22, 22) #x and y , size x  size  y  A             
            pygame.display.update()                                
            if move ==6: 
                DISPLAYSURF.blit(rbjimg,(rbjx, rbjy))
                jackCopy = DISPLAYSURF.copy()
                bposx = rbjx
                bposy = rbjy
                #print ('bposx boHit',     rbjx)
                #print ('bposy boHit'  ,   rbjy)        #test        
                pygame.display.flip()
                gameStart()
                
            if blue_RECT.colliderect(jackObjRect):#  blue hit jack ok 
                hitBBObj.play(20, 0 ,0)
                jposx
                jposy                                                                       
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitJ(Jack_SURF, jposx, jposy)
                
            if blue_RECT.colliderect(redObjRect):#  blue hit red one ok
                hitBBObj.play(20, 0 ,0)
                bposx
                bposy                                                                                        
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))              
                END = 540  # 540
                ENDR = 1000
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitR(RedB_SURF, rposx, rposy) 
                
            FPSCLOCK.tick(FPS)

BOWLSIZE = 22
image = pygame.image.load('ReBowl.png').convert()
redObj = {'surface':image,'size':BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}  
redObj['rect'] = pygame.Rect ((redObj['x'] ,
                                redObj['y'] - getPath(redObj['speed'], RATE, LEGNTH),
                                redObj['size'], redObj['size']))
redTObjRect = redObj['rect'] 

class blueBowlTwo(pygame.sprite.Sprite):   # blue two
    def __init__(self,bowlx, bowly, ark):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('BlBowl.png').convert()
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect , ball
        global hitBBObj, hitObj,bposx, bposy, btposx, btposy, rtposx, rtposy
        self.BOWLSIZE = 22
        RATE=300
        hitBBObj = 0        
        speed = 'speed'
        speed = 0
        blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h
        jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h
        redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h
        tredObjRect = pygame.Rect(rtposx, rtposy, 22, 22) #x and y , size x  size  y  h        

        tblueObj = {'surface':self.image,'size':self.BOWLSIZE,'x':bowlx, 'y':bowly, 'speed': 1}    
        while True:
            hitBBObj = pygame.mixer.Sound('bowlHitNew.wav')            
            DISPLAYSURF.blit(jackCopy , (0, 0))                              
            tblueObj['rect'] = pygame.Rect ((tblueObj['x'] ,
                                            tblueObj['y'] - getPath(tblueObj['speed'],RATE, LEGNTH),
                                            tblueObj['size'], tblueObj['size']))
            tblueObj['speed'] += 1  # speed 
            tblueObj['x'] -= ark #2    #  -  left / + right
            tblueTObjRect = tblueObj['rect'] 
            DISPLAYSURF.blit(tblueObj['surface'], tblueObj['rect'])
            btposx = tblueObj['rect'] [0]  
            btposy = tblueObj['rect'] [1]  
               
            tredObjRect = pygame.Rect(rtposx, rtposy, 22, 22) #x and y , size x  size  y  h             
            checkForQuit()                                
            if tblueObj['rect'].colliderect(jackObjRect):#   blue two / hit jack   
                hitBBObj.play(20, 0 ,0)               
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))                                     
                END = 540 
                ENDR = 1000                                                             
                jackCopy = DISPLAYSURF.copy() #ok#
                pygame.display.flip()                 
                bowlHitJ(Jack_SURF, jposx, jposy)
                
            if tblueObj['rect'].colliderect(redObjRect):#  blue two hit red one 
                hitBBObj.play(20, 0 ,0)
                rposx
                rposy                
                redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h                
                #print ('new pos  ',  rposx)  #ok
                #print ('new pos '  ,  rposy)  #ok                 
                DISPLAYSURF.blit(patch_SURF, (rposx, rposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitR(RedB_SURF, rposx, rposy)
                
            if tblueObj['rect'].colliderect(tredObjRect):#blue2 hit red2 = red2 hit blue2
                hitBBObj.play(20, 0 ,0)
                #print ('rt pos hit ',  rtposx)  #ok
                #print ('rt pos hit'  ,  rtposy)  #ok
                rtposx
                rtposy                
                tredObjRect = pygame.Rect(rtposx, rtposy, 22, 22) #x and y , size x  size  y  h                               
                DISPLAYSURF.blit(patch_SURF, (rtposx, rtposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitRtwo(RedB_SURF, rtposx, rtposy)
                
            if tblueObj['rect'].colliderect(blueObjRect):#  bluetwo hit blue one
                hitBBObj.play(20, 0 ,0)
                #print ('rt pos hit ',  rtposx)  #ok
                #print ('rt pos hit'  ,  rtposy)  #ok
                bposx
                bposy                
                blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h                
                
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitRtwo(BlueB_SURF, bposx, bposy)                
                
            if tblueObj['x'] > ENDR:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()             
            if tblueObj['x'] < END:            
                jackCopy = DISPLAYSURF.copy()              
                gameStart()        
            pygame.display.flip()                                
            FPSCLOCK.tick(FPS)            

BOWLSIZE = 22
image = pygame.image.load('ReBowl.png').convert()
redObj = {'surface':image,'size':BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}  
redObj['rect'] = pygame.Rect ((redObj['x'] ,
                                redObj['y'] - getPath(redObj['speed'],RATE, LEGNTH),
                                redObj['size'], redObj['size']))
redObjRect = redObj['rect']

class blueBowl(pygame.sprite.Sprite):   # blue one
    def __init__(self,bowlx, bowly, ark):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('BlBowl.png').convert()
        global ends, red, jack, blue,jackCopy ,ENDR, END, blueObjRect, redObjRect , ball
        global hitBBObj, hitObj,bposx, bposy, bHja
        self.BOWLSIZE = 22
        RATE=300
        hitBBObj = 0        
        speed = 'speed'
        speed = 0
        blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h
        jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h
        redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h                
        #print ('new pos  ',   rposx)  #ok
       # print ('new pos '  ,  rposy)  #ok                          
        #print ( 'blue  pos 1   x   ',  bposx)
        #print (' blue  pos 1   y  ' ,  bposy ) 
        
        blueObj = {'surface':self.image,'size':self.BOWLSIZE,'x':bowlx, 'y':bowly, 'speed': 1}    
        while True:
            hitBBObj = pygame.mixer.Sound('bowlHitNew.wav')            
            DISPLAYSURF.blit(jackCopy , (0, 0))                              
            blueObj['rect'] = pygame.Rect ((blueObj['x'] ,
                                            blueObj['y'] - getPath(blueObj['speed'],RATE, LEGNTH),
                                            blueObj['size'], blueObj['size']))
            blueObj['speed'] += 1  # speed 
            blueObj['x'] -= ark #2    #  -  left / + right
            blueObjRect = blueObj['rect']
            DISPLAYSURF.blit(blueObj['surface'], blueObj['rect'])
            bposx = blueObj['rect'] [0]
            bposy = blueObj['rect'] [1]
            #print ('  x  ',  bposx)  #ok
            #print (' y '  ,  bposy)  #ok            
            checkForQuit()                                
            if blueObj['rect'].colliderect(jackObjRect):#   
                hitBBObj.play(20, 0 ,0)
                bHja += 1                                   # blue hit jack
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))                                   
                END = 540 
                ENDR = 1000                                                             
                jackCopy = DISPLAYSURF.copy() #
                pygame.display.flip()                 
                bowlHitJ(Jack_SURF, jposx, jposy)
                
            if blueObj['rect'].colliderect(redObjRect):#  
                hitBBObj.play(20, 0 ,0)
                rposx
                rposy                
                redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h                
                #print ('new pos  ',  rposx)  #ok
                #print ('new pos '  ,  rposy)  #ok                 
                DISPLAYSURF.blit(patch_SURF, (rposx, rposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitR(RedB_SURF, rposx, rposy)
                
            if blueObj['x'] > ENDR:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()             
            if blueObj['x'] < END:            
                jackCopy = DISPLAYSURF.copy()              
                gameStart()        
            pygame.display.flip()                                
            FPSCLOCK.tick(FPS)
            
BOWLSIZE = 22            
image = pygame.image.load('BlBowl.png').convert()            
tblueObj = {'surface':image,'size':BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}
tblueObj['rect'] = pygame.Rect ((tblueObj['x'] ,
                                tblueObj['y'] - getPath(tblueObj['speed'],RATE, LEGNTH),
                                tblueObj['size'], tblueObj['size']))         
tblueObjRect = tblueObj['rect'] 
                
class redBowlTwo(pygame.sprite.Sprite):   #  red two
    def __init__(self,bowlx, bowly, ark):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load('ReBowl.png').convert()
        global ends,jack, red, blue,jackCopy, END, ENDR, blueObjRect, redObjRect
        global hitBBObj, hitObj,rposx, rposy ,bposx, bposy,leRi, rtposx, rtposy       
        self.BOWLSIZE = 22
        hitObjB = 0        
        RATE=300
        #currentBounce = 0
        speed = 'speed'
        speed = 0
        redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h         
        jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h
        #print ( '11j pos 1  jor x   ',  jposx)
        #print ('11 j pos 1  jor y  ' ,  jposy )
        blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h

        tblueObjRect = pygame.Rect(btposx, btposy, 22, 22) #x and y , size x  size  y  h        
        tredObj = {'surface':self.image,'size':self.BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}    
        while True:
            hitObjB = pygame.mixer.Sound('bowlHitNew.wav')            
            DISPLAYSURF.blit(jackCopy , (0, 0))              
            tredObj['rect'] = pygame.Rect ((tredObj['x'] ,
                                            tredObj['y'] - getPath(tredObj['speed'],RATE, LEGNTH),
                                            tredObj['size'], tredObj['size']))
            tredObj['speed'] += 1  # +=1
            tredObj['x'] -= ark #2    #  -  left / + right
            tredObjRect = tredObj['rect']
            DISPLAYSURF.blit(tredObj['surface'], tredObj['rect'])
            rtposx = tredObj['rect'] [0]  # ??
            rtposy = tredObj['rect'] [1]  #??
            #print ('rt  pos  ',  rtposx)  #ok
            #print ('rt pos '  ,  rtposy)  #ok
            
            checkForQuit()
            if tredObj['rect'].colliderect(jackObjRect):     #red two / hit jack         
                hitObj.play(20, 0 ,0)
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))
                END = 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitJ(Jack_SURF, jposx, jposy)
                
            if tredObj['rect'].colliderect(blueObjRect):# red  two / hit blue one
                hitObj.play(20, 0 ,0)
                blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h                
                #print ('new pos  ',  bposx)  #ok
                #print ('new pos '  ,  bposy)  #ok                 
                bposx
                bposy
                
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))                
                END = 650 #540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy()                     
                pygame.display.flip()
                bowlHitB(BlueB_SURF, bposx, bposy)#
                
            if tredObj['rect'].colliderect(tblueObjRect):#red 2 hit blue 2= blue 2 hit red 2
                hitBBObj.play(20, 0 ,0)
                #print ('rt pos hit ',  rtposx)  #ok
                #print ('rt pos hit'  ,  rtposy)  #ok
                btposx
                btposy                
                tblueObjRect = pygame.Rect(btposx, btposy, 22, 22) #x and y , size x  size  y  h                                
                DISPLAYSURF.blit(patch_SURF, (btposx, btposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitBtwo(BlueB_SURF, btposx, btposy)
               
            if tredObj['rect'].colliderect(redObjRect):#  red hit red two
                hitBBObj.play(20, 0 ,0)
                #print ('rt pos hit ',  rtposx)  #ok
                #print ('rt pos hit'  ,  rtposy)  #ok
                rposx
                rposy                
                redObjRect = pygame.Rect(rposx, rposy, 22, 22) #x and y , size x  size  y  h                
                
                DISPLAYSURF.blit(patch_SURF, (rposx, rposy))                
                END = 540  # 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitRtwo(RedB_SURF, rposx, rposy) 
                                
            if tredObj['x'] > ENDR:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()             
            if tredObj['x'] < END:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()        
            pygame.display.flip()                                    
            FPSCLOCK.tick(FPS)              
            
BOWLSIZE = 22            
image = pygame.image.load('BlBowl.png').convert()            
blueObj = {'surface':image,'size':BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}
blueObj['rect'] = pygame.Rect ((blueObj['x'] ,
                                blueObj['y'] - getPath(blueObj['speed'],RATE, LEGNTH),
                                blueObj['size'], blueObj['size']))         
blueObjRect = blueObj['rect']
                
class redBowl(pygame.sprite.Sprite):   #  red one
    def __init__(self,bowlx, bowly, ark):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load('ReBowl.png').convert()
        global ends,jack, red, blue,jackCopy, END, ENDR, blueObjRect, redObjRect
        global hitBBObj, hitObj,rposx, rposy ,bposx, bposy,leRi,rHja, bHja       
        self.BOWLSIZE = 22
        hitObjB = 0        
        RATE=300
        speed = 'speed'
        speed = 0
        jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h
        #print ( '11j pos 1  jor x   ',  jposx)
        #print ('11 j pos 1  jor y  ' ,  jposy )
        blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h
        #print ('new pos  ',  bposx)  #ok
        #print ('new pos '  ,  bposy)  #ok         
        redObj = {'surface':self.image,'size':self.BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}    
        while True:
            hitObjB = pygame.mixer.Sound('bowlHitNew.wav')            
            DISPLAYSURF.blit(jackCopy , (0, 0))              
            redObj['rect'] = pygame.Rect ((redObj['x'] ,
                                            redObj['y'] - getPath(redObj['speed'],RATE, LEGNTH),
                                            redObj['size'], redObj['size']))
            redObj['speed'] += 1  # +=1
            redObj['x'] -= ark #2    #  -  left / + right
            redObjRect = redObj['rect']
            DISPLAYSURF.blit(redObj['surface'], redObj['rect'])
            rposx = redObj['rect'] [0]
            rposy = redObj['rect'] [1]          
            checkForQuit()
            if redObj['rect'].colliderect(jackObjRect):  # hit jack             
                hitObj.play(20, 0 ,0)
                rHja +=1  #   red hit  jack  +1
                DISPLAYSURF.blit(patch_SURF, (jposx, jposy))
                END = 540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy() #ok                     
                pygame.display.flip()#ok
                bowlHitJ(Jack_SURF, jposx, jposy)
                                    
            if redObj['rect'].colliderect(blueObjRect):# hit blue one
                hitObj.play(20, 0 ,0)
                blueObjRect = pygame.Rect(bposx, bposy, 22, 22) #x and y , size x  size  y  h                
                #print ('new pos  ',  bposx)  #ok
                #print ('new pos '  ,  bposy)  #ok                 
                bposx
                bposy
                DISPLAYSURF.blit(patch_SURF, (bposx, bposy))                
                END = 650 #540
                ENDR = 1000                  
                jackCopy = DISPLAYSURF.copy()                     
                pygame.display.flip()
                bowlHitB(BlueB_SURF, bposx, bposy)#                
            if redObj['x'] > ENDR:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()             
            if redObj['x'] < END:
                jackCopy = DISPLAYSURF.copy()              
                gameStart()        
            pygame.display.flip()                                    
            FPSCLOCK.tick(FPS)   

class playJack(pygame.sprite.Sprite):   #(bowlx, bowly, ark):  ##left or right
    def __init__(self,bowlx, bowly, ark):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('jack.png').convert()        
        global ends, jack, red , blue, greenCopy, jackObj,jackCopy,END, ENDR, ball
        global jackObjRect,jposx, jposy
        ends += 1    
        self.BOWLSIZE = 21
        RATE=300##
        speed = 'speed'
        speed=0
        jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h         
        jackCopy = DISPLAYSURF.copy()    
        jackObj = {'surface':self.image,'size':self.BOWLSIZE,'x':bowlx, 'y': bowly, 'speed': 1}    
        while True:
            DISPLAYSURF.blit(jackCopy , (0, 0))                        
            jackObj['rect'] = pygame.Rect ((jackObj['x'] ,
                                            jackObj['y'] - getPath(jackObj['speed'],RATE, LEGNTH),##
                                            jackObj['size'], jackObj['size']))
            jackObj['speed'] += 1  # +=1
            jackObj['x'] -=  ark #2    #  -  left / + right
            jackObj_Y = jackObj['rect']
            jackObjRect = jackObj['rect']        
            DISPLAYSURF.blit(jackObj['surface'], jackObj['rect'])
            jposx = jackObj['rect'] [0]
            jposy = jackObj['rect'] [1]          
            checkForQuit()
            if jackObj['x'] < END:
                jackObjRect = pygame.Rect(jposx, jposy, 21, 21) #x and y , size x  size  y  h               
                jackCopy = DISPLAYSURF.copy()            
                gameStart()          
            if jackObj['x'] > ENDR:
                jackCopy = DISPLAYSURF.copy()            
                gameStart() 
            pygame.display.flip()                                
            FPSCLOCK.tick(FPS)
    
def markers():  # start of game
    global jack, red , blue, ends, END, ENDR, jackCopy , leRi , LEGNTH
    END = 0
    ENDR =0
    scores()      
    while True:       
        DISPLAYSURF.blit(Score_SURF, (5, 5))                        
        scoreRSurf=BIGFONT.render(';  ' + str(scoreR), True, RED)
        scoreRRect=scoreRSurf.get_rect()
        scoreRRect.topleft=(WINDOWWIDTH-1110, 250)
        DISPLAYSURF.blit(scoreRSurf, scoreRRect)
        scoreBSurf=BIGFONT.render(';  ' + str(scoreB), True, BLUE)
        scoreBRect=scoreBSurf.get_rect()
        scoreBRect.topleft=(WINDOWWIDTH-1110, 326)
        DISPLAYSURF.blit(scoreBSurf, scoreBRect)
        endsSurf=BIGFONT.render(':  ' + str(ends), True, GREEN)
        endsRect=endsSurf.get_rect()
        endsRect.topleft=(WINDOWWIDTH-1110, 406)
        DISPLAYSURF.blit(endsSurf, endsRect)
                              
        aTRAN_RECT = pygame.Rect(310, 5, 129, 179) #x and y , size x  size  y  A
        bTRAN_RECT = pygame.Rect(440, 5, 119, 179)                                                     
        cTRAN_RECT = pygame.Rect(550, 5, 129, 179)                                       
        dTRAN_RECT = pygame.Rect(685, 5, 109, 179)                                                    
        eTRAN_RECT = pygame.Rect(790, 5, 118, 179)   
        fTRAN_RECT = pygame.Rect(910, 5, 109, 179)                                                       
        gTRAN_RECT = pygame.Rect(1020, 5, 119, 179)  
        hTRAN_RECT = pygame.Rect(1140, 5, 99, 179) 
        
        aaTRAN_RECT = pygame.Rect(310, 180, 129, 230) 
        abTRAN_RECT = pygame.Rect(440, 180, 119, 230)                                                      
        acTRAN_RECT = pygame.Rect(550, 180, 129, 230)                                       
        adTRAN_RECT = pygame.Rect(685, 180, 109, 230)                                                    
        aeTRAN_RECT = pygame.Rect(790, 180, 118, 230)  
        afTRAN_RECT = pygame.Rect(910, 180, 109, 230)                                                      
        agTRAN_RECT = pygame.Rect(1020, 180, 119, 230) 
        ahTRAN_RECT = pygame.Rect(1140, 180, 99, 230)
                    
        markFont=pygame.font.Font('freesansbold.ttf', 24)
        markSurf=markFont.render('*Pick a marker for your bowl*', True, BLUE)
        markRect = markSurf.get_rect()
        markRect.midtop = (WINDOWWIDTH /2, 400)
        DISPLAYSURF.blit(markSurf, markRect)
        
        #pygame.draw.rect(DISPLAYSURF,BLUE, eTRAN_RECT)####  blue rect on    / test del
        #pygame.draw.rect(DISPLAYSURF,WHITE, fTRAN_RECT)####  blue rect on   / test del
        
        #pygame.draw.rect(DISPLAYSURF,WHITE, aeTRAN_RECT)####  blue rect on    / test del
        #pygame.draw.rect(DISPLAYSURF,BLUE, afTRAN_RECT)####  blue rect on   / test del
        
        pygame.display.update()
        checkForQuit()        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and eTRAN_RECT.collidepoint(event. pos) :  #e   done
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    END = random.randint(650, 750)
                    #END = 580  # test
                    ENDR = 1000                    
                    jack += 1                   
                    leRi =-3                               
                    jackCopy = DISPLAYSURF.copy()                     
                    playJack(950, 800, 2)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                    
                    #END = 600  # test
                    END = random.randint(650, 750)
                    ENDR = 1000                    
                    red += 1
                    leRi =-1                  
                    redBowl(950, 800, 2)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                     
                    END = random.randint(650, 750)
                    #END = 580  # test
                    ENDR = 1000                    
                    red += 1
                    leRi = -2                   
                    redBowlTwo(950, 800, 2)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    END = random.randint(650, 750)
                    #END = 580  # test
                    ENDR = 1000                    
                    blue += 1
                    leRi = -5                  
                    blueBowl(950, 800, 2)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    END = random.randint(650, 750)
                    #END = 580  #  test
                    ENDR = 1000                   
                    blue += 1
                    leRi = -4 
                    blueBowlTwo(950, 800, 2)
            if event.type == MOUSEBUTTONUP and aTRAN_RECT.collidepoint(event. pos) :  #a  done  
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END = random.randint(320, 360)
                    ENDR=1000
                    leRi = -4                    
                    playJack(870, 800,4)                    
                if red == 1:
                    LEGNTH = random.randint(600, 830)                 
                    red += 1
                    END = random.randint(320, 360)
                    ENDR=1000
                    leRi = -2
                    redBowl(870, 800,4)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                   
                    red += 1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -5
                    redBowlTwo(870, 800, 4)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -3
                    blueBowl(870, 800, 4)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    blue += 1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -4
                    blueBowlTwo(870, 800, 4)
            if event.type == MOUSEBUTTONUP and bTRAN_RECT.collidepoint(event. pos) : #b  done   
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END = random.randint(390, 440) 
                    ENDR=1000
                    leRi = -4                    
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(870, 800, 3.5)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                  
                    red += 1
                    END = random.randint(390, 440)  
                    ENDR=1000
                    leRi = -2                    
                    redBowl(870, 800,3.5)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                    
                    red += 1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -4                   
                    redBowlTwo(870, 800, 3.5)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -5                    
                    blueBowl(870, 800, 3.5)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    blue += 1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -2                    
                    blueBowlTwo(870, 800, 3.5)
            if event.type == MOUSEBUTTONUP and cTRAN_RECT.collidepoint(event. pos) :   #c done  
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    jack  += 1
                    END = random.randint(450, 540)
                    ENDR=1000
                    leRi = -2                     
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(870, 800, 3)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                   
                    red += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -3                    
                    redBowl(870, 800,3)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                     
                    red += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -5                    
                    redBowlTwo(870, 800, 3)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -4                    
                    blueBowl(870, 800, 3)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    blue += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -3                   
                    blueBowlTwo(870, 800, 3)
            if event.type == MOUSEBUTTONUP and dTRAN_RECT.collidepoint(event. pos) :   # d done   
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END = random.randint(510, 610) 
                    ENDR=1000
                    leRi = -4                     
                    jackCopy = DISPLAYSURF.copy()                   
                    playJack(870, 800, 2.5)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                     
                    red += 1
                    END = random.randint(510, 610)  
                    ENDR=1000
                    leRi = -2                    
                    redBowl(870, 800,2.5)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                    
                    red += 1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -4                   
                    redBowlTwo(870, 800, 2.5)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -3                    
                    blueBowl(870, 800, 2.5)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                   
                    blue += 1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -5                    
                    blueBowlTwo(870, 800, 2.5)  
            if event.type == MOUSEBUTTONUP and fTRAN_RECT.collidepoint(event. pos) : #f   done
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                
                    jack  += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1070)
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(800, 800, -2)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                   
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1070)
                    jackCopy = DISPLAYSURF.copy()                    
                    redBowl(800, 800,-1.5)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                   
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1070)                     
                    redBowlTwo(800, 800, -1.5)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1070)                     
                    blueBowl(800, 800, -1.5)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    blue += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1070)                     
                    blueBowlTwo(800, 800, -1.5)  
            if event.type == MOUSEBUTTONUP and gTRAN_RECT.collidepoint(event. pos) : #g done
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END == 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1050, 1150)
                    jackCopy = DISPLAYSURF.copy()                   
                    playJack(870, 800, -2)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                    
                    red += 1
                    END == 100
                    leRi = random.randint(2, 5)                                        
                    ENDR = random.randint(1050, 1150)  
                    redBowl(870, 800,-2)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                    
                    red += 1
                    END == 100
                    leRi = random.randint(2, 5)                                       
                    ENDR = random.randint(1050, 1150)                      
                    redBowlTwo(870, 800, -2)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                    
                    blue +=1
                    END == 100
                    leRi = random.randint(2, 5)                                        
                    ENDR = random.randint(1050, 1150)                      
                    blueBowl(870, 800, -2)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                      
                    blue += 1
                    END == 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1050, 1150)                      
                    blueBowlTwo(870, 800, -2)
            if event.type == MOUSEBUTTONUP and hTRAN_RECT.collidepoint(event. pos) :      
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END = 100
                    leRi = random.randint(2, 5)                                         
                    ENDR = random.randint(1080, 1270)                     
                    playJack(870, 800,-2.5)                               
                if red == 1:
                    LEGNTH = random.randint(600, 830)                     
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1260)                     
                    redBowl(870, 800,-2.2)
                if red == 3:
                    LEGNTH = random.randint(600, 830)                   
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1260)                    
                    redBowlTwo(870, 800, -2.2)                   
                if blue == 1:
                    LEGNTH = random.randint(600, 830)                   
                    blue +=1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1260)                    
                    blueBowl(870, 800, -2.2)
                if blue == 3:
                    LEGNTH = random.randint(600, 830)                    
                    blue += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1260)                     
                    blueBowlTwo(870, 800, -2.2)                 
                    
            if event.type == MOUSEBUTTONUP and aeTRAN_RECT.collidepoint(event. pos) :  
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    END = random.randint(600, 700)
                    #END = 580
                    ENDR = 1000                    
                    jack += 1                   
                    leRi =-3                               
                    jackCopy = DISPLAYSURF.copy()                     
                    playJack(870, 800, 2)                              
                if red == 1:
                    LEGNTH = random.randint(530, 650)                     
                    #END = 600
                    END = random.randint(600, 700)
                    ENDR = 1000                    
                    red += 1
                    leRi =-3 #-1                  
                    redBowl(870, 800, 2)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                    
                    END = random.randint(600, 700)
                    #END = 580
                    ENDR = 1000                    
                    red += 1
                    leRi = -3 #-2                   
                    redBowlTwo(870, 800, 2)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                    
                    END = random.randint(600, 700)
                    #END = 580
                    ENDR = 1000                    
                    blue += 1
                    leRi = -3 #-5                  
                    blueBowl(870, 800, 2)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                     
                    END = random.randint(600, 700)
                    #END = 580
                    ENDR = 1000                   
                    blue += 1
                    leRi = -3 #-4
                    blueBowlTwo(870, 800, 2)
            if event.type == MOUSEBUTTONUP and aaTRAN_RECT.collidepoint(event. pos) :   
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    jack  += 1
                    END = random.randint(320, 360)
                    ENDR=1000
                    leRi = -4                    
                    playJack(870, 800,4)                    
                if red == 1:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END = random.randint(320, 360)
                    ENDR=1000
                    leRi = -2
                    redBowl(870, 800,4)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -5
                    redBowlTwo(870, 800, 4)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                     
                    blue +=1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -3
                    blueBowl(870, 800, 4)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                      
                    blue += 1
                    END = random.randint(350, 360)
                    ENDR=1000
                    leRi = -4
                    blueBowlTwo(870, 800, 4)
            if event.type == MOUSEBUTTONUP and abTRAN_RECT.collidepoint(event. pos) :   
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    jack  += 1
                    END = random.randint(390, 440) 
                    ENDR=1000
                    leRi = -4                    
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(870, 800, 3.5)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = random.randint(390, 440)  
                    ENDR=1000
                    leRi = -2                    
                    redBowl(870, 800,3.5)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -4                   
                    redBowlTwo(870, 800, 3.5)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                     
                    blue +=1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -5                    
                    blueBowl(870, 800, 3.5)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                      
                    blue += 1
                    END = random.randint(390, 440)
                    ENDR=1000
                    leRi = -2                    
                    blueBowlTwo(870, 800, 3.5)
            if event.type == MOUSEBUTTONUP and acTRAN_RECT.collidepoint(event. pos) :   #c done  
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    jack  += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -2                     
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(870, 800, 3)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -3                    
                    redBowl(870, 800,3)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -5                    
                    redBowlTwo(870, 800, 3)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                      
                    blue +=1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -4                    
                    blueBowl(870, 800, 3)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                      
                    blue += 1
                    END = random.randint(450, 550)
                    ENDR=1000
                    leRi = -3                   
                    blueBowlTwo(870, 800, 3)
            if event.type == MOUSEBUTTONUP and adTRAN_RECT.collidepoint(event. pos) :     
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                 
                    jack  += 1
                    END = random.randint(510, 610) 
                    ENDR=1000
                    leRi = -4                     
                    jackCopy = DISPLAYSURF.copy()                   
                    playJack(870, 800, 2.5)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END = random.randint(510, 610)  
                    ENDR=1000
                    leRi = -2                    
                    redBowl(870, 800,2.5)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -4                   
                    redBowlTwo(870, 800, 2.5)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                     
                    blue +=1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -3                    
                    blueBowl(870, 800, 2.5)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                      
                    blue += 1
                    END = random.randint(510, 610)
                    ENDR=1000
                    leRi = -5                    
                    blueBowlTwo(870, 800, 2.5)  
            if event.type == MOUSEBUTTONUP and afTRAN_RECT.collidepoint(event. pos) : 
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                  
                    jack  += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1020)
                    jackCopy = DISPLAYSURF.copy()                    
                    playJack(800, 800, -1.5)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1020)
                    jackCopy = DISPLAYSURF.copy()                    
                    redBowl(800, 800,-1.5)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1020)                     
                    redBowlTwo(800, 800, -1.5)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                      
                    blue +=1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1020)                     
                    blueBowl(800, 800, -1.5)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                     
                    blue += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(980, 1020)                     
                    blueBowlTwo(800, 800, -1.5)  
            if event.type == MOUSEBUTTONUP and agTRAN_RECT.collidepoint(event. pos) :
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END == 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1050, 1150)
                    jackCopy = DISPLAYSURF.copy()                   
                    playJack(870, 800, -2)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END == 100
                    leRi = random.randint(2, 5)                                        
                    ENDR = random.randint(1050, 1150)  
                    redBowl(870, 800,-2)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                      
                    red += 1
                    END == 100
                    leRi = random.randint(2, 5)                                       
                    ENDR = random.randint(1050, 1150)                      
                    redBowlTwo(870, 800, -2)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                      
                    blue +=1
                    END == 100
                    leRi = random.randint(2, 5)                                        
                    ENDR = random.randint(1050, 1150)                      
                    blueBowl(870, 800, -2)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                      
                    blue += 1
                    END == 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1050, 1150)                      
                    blueBowlTwo(870, 800, -2)
            if event.type == MOUSEBUTTONUP and ahTRAN_RECT.collidepoint(event. pos) :      
                if jack == 1:
                    LEGNTH = random.randint(530, 830)                   
                    jack  += 1
                    END = 100
                    leRi = random.randint(2, 5)                                         
                    ENDR = random.randint(1080, 1270)                     
                    playJack(870, 800,-2.2)                               
                if red == 1:
                    LEGNTH = random.randint(530, 650)                     
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1270)                     
                    redBowl(870, 800,-2.2)
                if red == 3:
                    LEGNTH = random.randint(530, 650)                   
                    red += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1270)                    
                    redBowlTwo(870, 800, -2.2)                   
                if blue == 1:
                    LEGNTH = random.randint(530, 650)                     
                    blue +=1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1270)                    
                    blueBowl(870, 800, -2.2)
                if blue == 3:
                    LEGNTH = random.randint(530, 650)                     
                    blue += 1
                    END = 100
                    leRi = random.randint(2, 5)                     
                    ENDR = random.randint(1080, 1270)                     
                    blueBowlTwo(870, 800, -2.2)                                  
def newEnd():
   
    while True:
        global jack, red, blue, backDrop, green, backDropTwo, jackCopy
        global jposx, jposy, rposx, rposy, bposx, bposy, btposx, btposy
        global rtposx, rtposy, rHja, bHja
        green += 1
        jack = 0
        red = 0
        blue = 0
        jposx = 0
        jposy = 0
        bposx = 0
        bposy = 0
        rposx = 0
        rposy = 0
        btposx = 0
        btposy = 0
        rtposx = 0
        rtposy = 0
        rHja = 0
        bHja = 0
        if green %2 == 0:
            DISPLAYSURF.blit(backDrop_SURF, (5, 3))            
            jackCopy = DISPLAYSURF.copy()             
            pygame.display.update()            
            gameStart()
        else:
            DISPLAYSURF.blit(backDropTwo_SURF, (310, 3))             
            jackCopy = DISPLAYSURF.copy()             
            pygame.display.update()            
            gameStart()            
               
def gameStart():

    global bposx, bposy, rposx, rposy, jposx, jposy
        
    global jack, red , blue, ends, jackObj, jackCopy ,scoreR, scoreB, ENDR, END
    global hitBBObj, hitObj, jackObjRect, redObjRect, blueObjRect, ball 
    posx = 0
    posy = 0
    DISPLAYSURF.blit(Start_SURF, (800, 750))
    pygame.mixer.Sound.stop(hitObj) 
    pygame.mixer.Sound.stop(hitBBObj)     
    scores()
    while True:
       
        rPlus_RECT = pygame.Rect(6, 230, 40, 40) #x and y , size x  size  y  A
        rMinus_RECT = pygame.Rect(6, 270, 40, 40) #x and y , size x  size  y  B                                                      
        bPlus_RECT = pygame.Rect(6, 310, 40, 40) #x and y , size x  size  y  C
        bMinus_RECT = pygame.Rect(6, 355, 40, 40) #x and y , size x  size  y  C       
        newend_RECT = pygame.Rect(40, 540, 200, 40) #x and y , size x  size  y  A        
        jack_RECT = pygame.Rect(110, 600, 60, 60) #x and y , size x  size  y  A
        red_RECT = pygame.Rect(190, 740, 60, 60) #x and y , size x  size  y  B                                                      
        blue_RECT = pygame.Rect(60, 740, 60, 60) #x and y , size x  size  y  C           
        DISPLAYSURF.blit(Score_SURF, (5, 5))        
       
        scoreRSurf=BIGFONT.render(';  ' + str(scoreR), True, RED)###ok
        scoreRRect=scoreRSurf.get_rect()
        scoreRRect.topleft=(WINDOWWIDTH-1110, 250)
        DISPLAYSURF.blit(scoreRSurf, scoreRRect)
        scoreBSurf=BIGFONT.render(';  ' + str(scoreB), True, BLUE)###ok
        scoreBRect=scoreBSurf.get_rect()
        scoreBRect.topleft=(WINDOWWIDTH-1110, 326)
        DISPLAYSURF.blit(scoreBSurf, scoreBRect)
        endsSurf=BIGFONT.render(':  ' + str(ends), True, GREEN)###ok
        endsRect=endsSurf.get_rect()
        endsRect.topleft=(WINDOWWIDTH-1110, 406)
        DISPLAYSURF.blit(endsSurf, endsRect)        
        checkForQuit()        
        pygame.display.update()        
        for event in pygame.event.get():            
            if event.type == MOUSEBUTTONUP and rPlus_RECT.collidepoint(event. pos) :      
                scoreR +=1
            if event.type == MOUSEBUTTONUP and rMinus_RECT.collidepoint(event. pos) :
                scoreR -=1
            if event.type == MOUSEBUTTONUP and bPlus_RECT.collidepoint(event. pos) :   
                scoreB +=1
            if event.type == MOUSEBUTTONUP and bMinus_RECT.collidepoint(event. pos) :       
                scoreB -=1        
            if event.type == MOUSEBUTTONUP and newend_RECT.collidepoint(event. pos) :        
                newEnd()     
            if event.type == MOUSEBUTTONUP and jack_RECT.collidepoint(event. pos) :
                if jack  < 1:
                    jack += 1
                    markers()
                if jack >2 :           
                    gameStart()                            
            if event.type == MOUSEBUTTONUP and red_RECT.collidepoint(event. pos):
                if red <3:
                    red += 1
                    markers()
                if red > 3:
                    gameStart()                
            if event.type == MOUSEBUTTONUP and blue_RECT.collidepoint(event. pos):
                if blue < 3:
                    blue += 1
                    markers()
                if blue > 3:
                    gameStart()
            if scoreR == 21:
                redWin()
                scoreR = 0
                main()
            if scoreB == 21:
                blueWin()
                scoreB = 0
                main()   
                    
def rules():
    while True:
        DISPLAYSURF.blit(rulesPic , (10, 0))
        but_RECT = pygame.Rect(660, 650, 250, 120) #x and y , size x  size  y  A        
        wFont=pygame.font.Font('freesansbold.ttf', 18)
        wSurf=wFont.render('Players toss to go first & who plays red or blue', True, BLUE)
        wRect = wSurf.get_rect()
        wRect.topleft =(340, 250)
        DISPLAYSURF.blit(wSurf, wRect)        
        wKeyFont=pygame.font.Font('freesansbold.ttf', 18)
        wKeySurf=wKeyFont.render('Play order,Jack,/red,blue,red,blue,or Jack, /blue,red,blue,red,click on bowls on Left to play', True, BLUE)
        wKeyRect = wKeySurf.get_rect()
        wKeyRect.topleft =(340, 280)
        DISPLAYSURF.blit(wKeySurf, wKeyRect)        
        weyFont=pygame.font.Font('freesansbold.ttf', 18)
        weySurf=weyFont.render('click on jack,pick a mark on the top edge of green and click on it to send the jack', True, BLUE)
        weyRect = weySurf.get_rect()
        weyRect.topleft =(340, 310)
        DISPLAYSURF.blit(weySurf, weyRect)        
        weFont=pygame.font.Font('freesansbold.ttf', 18)
        weSurf=weFont.render('click on red or blue bowl and click left or right of the same mark to get the bowl near the jack', True, BLUE)
        weRect = weSurf.get_rect()
        weRect.topleft =(340, 340)
        DISPLAYSURF.blit(weSurf, weRect)        
        aFont=pygame.font.Font('freesansbold.ttf', 18)
        aSurf=aFont.render("If jack go's of the green ,click NEW END to start again & the other player takes the jack ",True, BLUE)
        aRect = aSurf.get_rect()
        aRect.topleft =(340, 370)
        DISPLAYSURF.blit(aSurf, aRect)                   
        bFont=pygame.font.Font('freesansbold.ttf', 18)
        bSurf=bFont.render("one point for each bowl nearest the jack ,no score for bowls off the green ",True, BLUE)
        bRect = bSurf.get_rect()
        bRect.topleft =(340, 400)
        DISPLAYSURF.blit(bSurf, bRect)
        
        bFont=pygame.font.Font('freesansbold.ttf', 18)
        bSurf=bFont.render("when 4 bowls have been sent add your score with the + & - buttons no the LEFT and click NEW END  ",True, BLUE)
        bRect = bSurf.get_rect()
        bRect.topleft =(340, 430)
        DISPLAYSURF.blit(bSurf, bRect)

        DISPLAYSURF.blit(BASICFONT.render(" First player with 21 points wins.",1, BLUE), (340, 460))
        checkForQuit()         
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and but_RECT.collidepoint(event. pos) :
                newEnd()
       

def main():  
    global bowlRimg, bowlBimg, jackimg, backDrop_SURF ,bowlx, bowly, jackCopy
    bowlRimg=pygame.image.load('ReBowl.png')
    bowlBimg=pygame.image.load('BlBowl.png')
    jackimg=pygame.image.load('jack.png')       
    backDrop_SURF=pygame.image.load('bowlGreen.png').convert()
    DISPLAYSURF.blit(backDrop_SURF, (5, 5))
    while True:
        rules()
        pygame.display.update()
        pygame.time.wait(1000)
        checkForQuit()        
    FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
        

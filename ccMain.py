#===============================================================
#Cookie clicker - made in Pygame!
#===============================================================

#imports
import pygame
from pygame.sprite import Sprite
import os
import tkinter as tk
from tkinter.font import Font

#colors
pastelGreen = (153,255,153)
pastelYellow = (153,153,255)
darkBlue = (73, 96, 117)
lightBlue = (194, 241, 219)
black = (0, 0, 0)
white = (255, 255, 255)
lightOrange = (243, 192, 128)
black2 = (85, 90, 96)

#setup
pygame.init()
clock = pygame.time.Clock()
timeCounter = 0
window = pygame.display.set_mode((950, 600))
window.fill(lightOrange)
pygame.display.set_caption("Cookie Clicker!")
cookies = pygame.sprite.Group()
CPS = 0

#images
chocolateChipCookieImage = pygame.image.load(os.path.join("images", "ChocolateChipCookie.png"))
cookieGoblinImage = pygame.image.load(os.path.join("images", "cookieGoblin.png"))

# ==========================================
#               PYGAME CODE
#============================================
class cookie(Sprite):

    def __init__(self, x, y, cookieImage, var, cookieValue):
        super().__init__()
        self.x = x
        self.y = y
        self.image = cookieImage
        self.var = var
        self.cookieValue = cookieValue

        self.cookieCount = 0
        self.cookieCounter()

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.coverUpRect = self.rect
        self.coverUpRect[3] += 1
        # creating a formatted version of the cookieCount to be displayed
        self.Font = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 80)



    def cookieCounter(self):
        #if the path exists, open it and set self.CookieCount to the saved value.
        if os.path.exists("ccUserInfo.txt"):
            file = (open("ccUserInfo.txt", "r"))
            self.info = file.read()
            self.info = self.info.split("\n")
            self.info = [line.replace("COOKIES - ", "") for line in self.info]
            self.info = [line.replace("CPS - ", "") for line in self.info]
            self.info = [line.replace("GOBLINS - ", "") for line in self.info]
            self.info = [line.replace("GOBLIN_PRICE - ", "") for line in self.info]
            try:
                self.info.remove("")
                self.cookieCount = int(self.info[0])
            except:
                pass
            file.close()

        else:
            newFile = open("ccUserInfo.txt", "w+")
            newFile.write("COOKIES - " + self.cookieCount + "\n")
            newFile.close()

    def update(self):
        window.fill(lightOrange)
        window.blit(self.image, self.rect)
        self.commaCookieCount = "{:,}".format(int(self.cookieCount))
        self.cookieCountDisplay = self.Font.render(self.commaCookieCount, True, black2)
        self.text_rect = self.cookieCountDisplay.get_rect(center=(475, 50))
        window.blit(self.cookieCountDisplay, self.text_rect)


#class to create text
class createText:
    def __init__(self, msg, color, fontsize, pos):
        self.msg = msg
        self.color = color
        self.pos = pos
        self.fontsize = fontsize

        Font = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", self.fontsize)
        self.text = Font.render(self.msg, True, self.color)
        self.text_rect = self.text.get_rect(center=(self.pos))
        window.blit(self.text, self.text_rect)
        pygame.display.update()

#class to create rectangles
class rectangle:
    def __init__(self, color, rectInfo, borderWidth = None): #rectInfo = (x, y, width, height)
        self.color = color
        self.rectInfo = rectInfo
        self.borderWidth = borderWidth
        if self.borderWidth == None:
            pygame.draw.rect(window, self.color, (self.rectInfo))
            pygame.display.update()
        else:
            pygame.draw.rect(window, self.color, (self.rectInfo), self.borderWidth)
            pygame.display.update()


#structures menu class
class structureMenu:
    def __init__(self):
        self.unlocked = 1
        self.visible = False
        self.menuRectFill = pygame.Rect((25,20), (350, 470))
        self.menuRectOutline = pygame.Rect((25,20), (350, 470))

        #=============
        #COOKIE GOBLIN
        #=============
        self.goblinsOwned = 0
        self.goblinPrice = 15
        self.goblinCPS = 1
        try:
            self.goblinsOwned = firstCookie.info[2]
            self.goblinsOwned = int(self.goblinsOwned)
            self.goblinPrice = firstCookie.info[3]
            self.goblinPrice = int(self.goblinPrice)
        except:
            pass
        self.cookieGoblinImage = cookieGoblinImage
        self.cookieGoblinImage = pygame.transform.scale(self.cookieGoblinImage, (64, 64))
        self.goblinRect = cookieGoblinImage.get_rect(center = (290, 273))
        self.goblinOutline = pygame.Rect((25,20), (350, 100))
        #text setup
        self.goblinTitleFont = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 26)
        self.goblinDescFont = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 19)
        self.goblinOwnedFont = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 24)
        self.goblinTitle = self.goblinTitleFont.render("COOKIE GOBLIN - 1 CPS", True, black2)
        self.goblinTitleRect = self.goblinTitle.get_rect(center=((235, 45)))
        self.goblinDesc = self.goblinDescFont.render("Groans, moans, and bakes cookies!", True, black2)
        self.goblinDescRect = self.goblinDesc.get_rect(center=((235, 70)))
        self.buyGoblinOutline = pygame.Rect((201, 80), (170, 37))


    def update(self):
        if self.visible == True:
            pygame.draw.rect(window, lightOrange, self.menuRectFill)
            pygame.draw.rect(window, black2, self.menuRectOutline, 5)
            #updating goblin values
            self.goblinsOwnedText = self.goblinOwnedFont.render(str(self.goblinsOwned) + " Goblins Owned", True, black2)
            self.goblinsOwnedRect = self.goblinsOwnedText.get_rect(center=((115, 100)))
            self.buyGoblinText = self.goblinOwnedFont.render("BUY: " + str(self.goblinPrice) + " cookies", True, black2)
            self.buyGoblinRect = self.buyGoblinText.get_rect(center =((285, 100)))

        else:
            pass
        if self.unlocked == 1 and self.visible == True:
            pygame.draw.rect(window, black2, self.goblinOutline, 5)
            pygame.draw.rect(window, black2, self.buyGoblinOutline, 5)
            window.blit(self.cookieGoblinImage, self.goblinRect)
            window.blit(self.goblinTitle, self.goblinTitleRect)
            window.blit(self.goblinDesc, self.goblinDescRect)
            window.blit(self.goblinsOwnedText, self.goblinsOwnedRect)
            window.blit(self.buyGoblinText, self.buyGoblinRect)
#cookies
firstCookie = cookie(475, 300, chocolateChipCookieImage, 9, 1)
cookies.add(firstCookie)

#text 1 - NEEDS to be here so the rectangles can use their text_rect variables
structureText = createText("STRUCTURES", black2, 65, (200, 565))
upgradeText = createText("UPGRADES", black2, 65, (795, 565))

#constant rectangles
structureOutline = rectangle(black2, structureText.text_rect, 10)
structureFilled  = rectangle(lightOrange, structureText.text_rect)
upgradeOutline   = rectangle(black2, upgradeText.text_rect, 10)
upgradeFilled    = rectangle(lightOrange, upgradeText.text_rect)

#text 2
structureText = createText("STRUCTURES", black2, 65, (200, 565))
upgradeText = createText("UPGRADES", black2, 65, (795, 565))

#structure menu
structMenu = structureMenu()

#CPS
CPS = 0
try:
    CPS = firstCookie.info[1]
    CPS = int(CPS)
except:
    pass
#pygame mainloop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            newFile = open("ccUserInfo.txt", "w")
            newFile.write("COOKIES - " + str(firstCookie.cookieCount) + "\n")
            newFile.write("CPS - " + str(CPS) + "\n")
            newFile.write("GOBLINS - " + str(structMenu.goblinsOwned) + "\n")
            newFile.write("GOBLIN_PRICE - " + str(structMenu.goblinPrice) + "\n")
            newFile.close()
            run = False

        #if the cookie is clicked
        if event.type == pygame.MOUSEBUTTONUP and firstCookie.rect.collidepoint(pygame.mouse.get_pos()):
            firstCookie.cookieCount += firstCookie.cookieValue

        #if the structures 'button' is clicked
        if event.type == pygame.MOUSEBUTTONUP and structureOutline.rectInfo.collidepoint(pygame.mouse.get_pos()):
            if structMenu.visible == False:
                structMenu.visible = True
            else:
                structMenu.visible = False
        #if someone hits the buy button for the goblin
        if event.type == pygame.MOUSEBUTTONUP and structMenu.visible == True and structMenu.buyGoblinOutline.collidepoint(pygame.mouse.get_pos()) and firstCookie.cookieCount >= int(structMenu.goblinPrice):
            structMenu.goblinsOwned += 1
            firstCookie.cookieCount -= int(structMenu.goblinPrice)
            CPS += int(structMenu.goblinCPS)
            structMenu.goblinPrice += structMenu.goblinPrice // 33

    if firstCookie.var > 0 and firstCookie.var <= 10:
        pygame.time.delay(100)
        firstCookie.rect[1] += 1
        firstCookie.var -= 1
        firstCookie.update()
        structMenu.update()

    elif firstCookie.var <= 0 and firstCookie.var > -10:
        pygame.time.delay(100)
        firstCookie.rect[1] -= 1
        firstCookie.var -= 1
        firstCookie.update()
        structMenu.update()

    else:
        pygame.time.delay(100)
        firstCookie.var = 10
        structMenu.update()

    timeCounter += clock.tick()
    print(timeCounter)
    if timeCounter >= 1000:
        firstCookie.cookieCount += CPS
        timeCounter = 0
    pygame.display.update((0, 0, 950, 500))

pygame.quit()
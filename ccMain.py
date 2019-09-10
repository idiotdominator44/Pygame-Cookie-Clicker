# ===============================================================
# Cookie clicker - made in Pygame!
# ===============================================================

# imports
import pygame
from pygame.sprite import Sprite
import os

# colors
pastelGreen = (153, 255, 153)
pastelYellow = (153, 153, 255)
darkBlue = (73, 96, 117)
lightBlue = (194, 241, 219)
black = (0, 0, 0)
white = (255, 255, 255)
lightOrange = (243, 192, 128)
black2 = (85, 90, 96)

# setup
pygame.init()
clock = pygame.time.Clock()
timeCounter = 0
window = pygame.display.set_mode((950, 600))
window.fill(lightOrange)
pygame.display.set_caption("Ye Olde Cookie Clicker!")
CPS = 0

# images
chocolateChipCookieImage = pygame.image.load(os.path.join("images", "ChocolateChipCookie.png"))
cookieGoblinImage = pygame.image.load(os.path.join("images", "cookieGoblin.png"))
goblinTribeImage = pygame.image.load(os.path.join("images", "goblinTribe.png"))
cursor1Image = pygame.image.load(os.path.join("images", "cookieCursor1.png"))
cursor2Image = pygame.image.load(os.path.join("images", "cookieCursor2.png"))
cursor3Image = pygame.image.load(os.path.join("images", "cookieCursor3.png"))
cursor4Image = pygame.image.load(os.path.join("images", "cookieCursor4.png"))
cursor5Image = pygame.image.load(os.path.join("images", "cookieCursor5.png"))
cursor6Image = pygame.image.load(os.path.join("images", "cookieCursor6.png"))

# loading information
if os.path.exists("ccUserInfo.txt"):
    with open("ccUserInfo.txt", "r") as file:
        info = file.read()
        info = info.split("\n")
        info = [line.replace("COOKIES - ", "") for line in info]
        info = [line.replace("OVERALL_CPS - ", "") for line in info]
        info = [line.replace("GOBLINS - ", "") for line in info]
        info = [line.replace("GOBLIN_PRICE - ", "") for line in info]
        info = [line.replace("GOBLIN_CPS - ", "") for line in info]
        info = [line.replace("CURSOR_PRICE - ", "") for line in info]
        info = [line.replace("CURSOR_LEVEL - ", "") for line in info]
        info = [line.replace("CURSOR_POWER - ", "") for line in info]
        info = [line.replace("UNLOCKED_STRUCTURES - ", "") for line in info]
        cookieCount = int(info[0])
        CPS = int(info[1])
        goblinsOwned = int(info[2])
        goblinPrice = int(info[3])
        goblinCPS = int(info[4])
        cursorUpgradePrice = int(info[5])
        cursorLevel = int(info[6])
        cursorPower = int(info[7])
        unlocked = int(info[8])
else:
    cookieCount = 0
    CPS = 0
    goblinsOwned = 0
    goblinPrice = 15
    goblinCPS = 1
    cursorUpgradePrice = 500
    cursorLevel = 1
    cursorPower = 1
    unlocked = 0


class Cookie(Sprite):

    def __init__(self, x, y, var):
        super().__init__()
        self.x = x
        self.y = y
        self.var = var
        self.Font = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 80)
        self.cookieCount = cookieCount
        self.rect = chocolateChipCookieImage.get_rect(center=(self.x, self.y))

    def draw(self):
        window.fill(lightOrange)
        window.blit(chocolateChipCookieImage, self.rect)
        commaCookieCount = "{:,}".format(int(cookieCount))
        cookieCountDisplay = self.Font.render(commaCookieCount, True, black2)
        text_rect = cookieCountDisplay.get_rect(center=(475, 50))
        window.blit(cookieCountDisplay, text_rect)
        CPSText = self.Font.render(str(CPS) + " cookies per second", True, black2)
        CPSTextRect = CPSText.get_rect(center=(475, 130))
        window.blit(CPSText, CPSTextRect)


class CreateText:
    def __init__(self, msg, color, font_size, pos):
        self.msg = msg
        self.color = color
        self.pos = pos
        self.fontSize = font_size
        Font = pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", self.fontSize)
        self.text = Font.render(self.msg, True, self.color)
        text_rect = self.text.get_rect(center=self.pos)
        window.blit(self.text, text_rect)
        pygame.display.update()


# class to create rectangles
class Rectangle:
    def __init__(self, color, rectInfo, borderWidth=None):  # rectInfo = (x, y, width, height)
        self.color = color
        self.rectInfo = rectInfo
        self.borderWidth = borderWidth
        if self.borderWidth == None:
            pygame.draw.rect(window, self.color, (self.rectInfo))
            pygame.display.update()
        else:
            pygame.draw.rect(window, self.color, (self.rectInfo), self.borderWidth)
            pygame.display.update()


class UpgradeMenu:
    def __init__(self):
        self.unlocked = 1
        self.visible = False
        self.menuRectFill = pygame.Rect((555, 20), (350, 470))
        self.menuRectOutline = pygame.Rect((555, 20), (350, 470))
        # POINTER UPGRADE
        self.cursor1Image = cursor1Image
        self.cursor2Image = cursor2Image
        self.cursor3Image = cursor3Image
        self.cursor4Image = cursor4Image
        self.cursor5Image = cursor5Image
        self.cursor6Image = cursor6Image
        self.cursor1Image = pygame.transform.scale(self.cursor1Image, (64, 64))
        self.cursor2Image = pygame.transform.scale(self.cursor2Image, (64, 64))
        self.cursor3Image = pygame.transform.scale(self.cursor3Image, (64, 64))
        self.cursor4Image = pygame.transform.scale(self.cursor4Image, (64, 64))
        self.cursor5Image = pygame.transform.scale(self.cursor5Image, (64, 64))
        self.cursor6Image = pygame.transform.scale(self.cursor6Image, (64, 64))
        self.cursorRect = cursor1Image.get_rect(center=(835, 280))
        self.cursorOutline = pygame.Rect((575, 20), (350, 100))
        self.upgradeFonts = {'upgradeButtonFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 65),
                             'cursorTitleFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 23),
                             'cursorDescFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 22),
                             'cursorLevelFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 24),
                             'cursorPowerFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 22),
                             'upgradeCursorFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 30)}
        self.upgradeButtonText = self.upgradeFonts['upgradeButtonFont'].render("UPGRADES", True, black2)
        self.cursorTitle = self.upgradeFonts['cursorTitleFont'].render("CLICKING HAND", True, black2)
        self.cursorDesc = self.upgradeFonts['cursorDescFont'].render("Double your clicking power!", True, black2)
        self.cursorTitleRect = self.cursorTitle.get_rect(center=(725, 40))
        self.cursorDescRect = self.cursorDesc.get_rect(center=(770, 65))
        self.upgradeButtonRect = self.upgradeButtonText.get_rect(center=(787, 565))
        self.menuRectFill = pygame.Rect((575, 20), (350, 470))
        self.menuRectOutline = pygame.Rect((575, 20), (350, 470))

    def draw(self):
        window.blit(self.upgradeButtonText, self.upgradeButtonRect)
        pygame.draw.rect(window, black2, self.upgradeButtonRect, 5)
        # drawing cursor
        self.cursorLevelText = self.upgradeFonts['cursorLevelFont'].render("Current Level: " + str(cursorLevel),
                                                                           True, black2)
        self.cursorLevelRect = self.cursorLevelText.get_rect(center=(655, 105))
        self.cursorPowerText = self.upgradeFonts['cursorPowerFont'].render("- " + str(cursorPower) + " POWER",
                                                                           True, black2)
        self.cursorPowerRect = self.cursorPowerText.get_rect(center=(845, 40))
        self.upgradeCursorButton = self.upgradeFonts['upgradeCursorFont'].render("BUY: " + str(cursorUpgradePrice),
                                                                                 True, black2)
        self.upgradeCursorRect = self.upgradeCursorButton.get_rect(midright=(915, 102))

        if self.visible:
            pygame.draw.rect(window, lightOrange, self.menuRectFill)
            pygame.draw.rect(window, black2, self.menuRectOutline, 5)
            pygame.draw.rect(window, black2, self.cursorOutline, 5)
            window.blit(self.cursorLevelText, self.cursorLevelRect)
            window.blit(self.cursorTitle, self.cursorTitleRect)
            window.blit(self.cursorDesc, self.cursorDescRect)
            window.blit(self.cursorPowerText, self.cursorPowerRect)
            window.blit(self.upgradeCursorButton, self.upgradeCursorRect)

            if cursorLevel == 1:
                window.blit(self.cursor1Image, self.cursorRect)
            elif cursorLevel == 2:
                window.blit(self.cursor2Image, self.cursorRect)
            elif cursorLevel == 3:
                window.blit(self.cursor3Image, self.cursorRect)
            elif cursorLevel == 4:
                window.blit(self.cursor4Image, self.cursorRect)
            elif cursorLevel == 5:
                window.blit(self.cursor5Image, self.cursorRect)
            elif cursorLevel >= 6:
                window.blit(self.cursor6Image, self.cursorRect)


# noinspection PyAttributeOutsideInit
class StructureMenu:
    def __init__(self):
        self.unlocked = unlocked
        self.visible = False
        # structure outlines
        self.outline1 = pygame.Rect((25, 20), (350, 100))
        self.outline2 = pygame.Rect((25, 120), (350, 100))
        self.outline3 = pygame.Rect((25, 220), (350, 100))
        self.outline4 = pygame.Rect((25, 320), (350, 100))

        self.structureFonts = {'structButtonFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 65),
                               'titleFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 26),
                               'descFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 20),
                               'ownedFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 24),
                               'lockedStructureFont': pygame.font.Font(r"C:\WINDOWS\FONTS\ALKHEMIKAL.TTF", 65)}
        self.structureButtonText = self.structureFonts['structButtonFont'].render("STRUCTURES", True, black2)

        # COOKIE GOBLIN
        self.cookieGoblinImage = cookieGoblinImage
        self.cookieGoblinImage = pygame.transform.scale(self.cookieGoblinImage, (64, 64))
        self.goblinRect = cookieGoblinImage.get_rect(center=(290, 273))
        self.goblinTitle = self.structureFonts['titleFont'].render("COOKIE GOBLIN - " + str(goblinCPS)
                                                                   + " CPS", True, black2)
        self.goblinDesc = self.structureFonts['descFont'].render("Groans, moans, and bakes cookies!", True,
                                                                 black2)
        self.structureButtonRect = self.structureButtonText.get_rect(center=(200, 565))
        self.goblinTitleRect = self.goblinTitle.get_rect(center=(235, 45))
        self.goblinDescRect = self.goblinDesc.get_rect(center=(235, 66))

        # GOBLIN TRIBE
        self.goblinTribeImage = goblinTribeImage
        self.goblinTribeImage = pygame.transform.scale(self.goblinTribeImage, (64, 64))
        self.tribeImageRect = goblinTribeImage.get_rect(center=(290, 373))
        # self.tribeOutline = pygame.Rect((25, 150), (350, 100))
        # self.tribeTitle = self.structureFonts['titleFont'].render("GOBLIN TRIBE - " + str(goblinCPS)
        #                                                           + " CPS", True, black2)
        # self.tribeDesc = self.structureFonts['descFont'].render("They live in tipis and perform cookie rituals!", True,
        #                                                          black2)
        # self.structureButtonRect = self.structureButtonText.get_rect(center=(200, 565))
        # self.goblinTitleRect = self.goblinTitle.get_rect(center=(235, 45))
        # self.goblinDescRect = self.goblinDesc.get_rect(center=(235, 66))

        # surrounding rectangle, outline ????? texts
        self.menuRectFill = pygame.Rect((25, 20), (350, 500))
        self.menuRectOutline = pygame.Rect((25, 20), (350, 500))
        self.lockedText = self.structureFonts['lockedStructureFont'].render("???", True, black2)
        self.lockedTextRect1 = self.lockedText.get_rect(center=(200, 173))
        self.lockedTextRect2 = self.lockedText.get_rect(center=(200, 273))
        self.lockedTextRect3 = self.lockedText.get_rect(center=(200, 373))
        self.lockedTextRect4 = self.lockedText.get_rect(center=(200, 473))

    def draw(self):
        window.blit(self.structureButtonText, self.structureButtonRect)
        pygame.draw.rect(window, black2, self.structureButtonRect, 5)
        self.buyGoblinText = self.structureFonts['ownedFont'].render(
            "BUY: " + str(goblinPrice), True, black2)
        self.buyGoblinRect = self.buyGoblinText.get_rect(midright=(370, 105))
        if self.visible:
            pygame.draw.rect(window, lightOrange, self.menuRectFill)
            pygame.draw.rect(window, black2, self.menuRectOutline, 5)
            pygame.draw.rect(window, black2, self.outline1, 5)
            pygame.draw.rect(window, black2, self.outline2, 5)
            pygame.draw.rect(window, black2, self.outline3, 5)
            pygame.draw.rect(window, black2, self.outline4, 5)
            # drawing cookie goblin values
            self.goblinsOwnedText = self.structureFonts['ownedFont'].render(
                str(goblinsOwned) + " Goblins Owned", True, black2)
            self.goblinsOwnedRect = self.goblinsOwnedText.get_rect(center=(115, 105))
        if self.unlocked == 1 and self.visible:
            window.blit(self.cookieGoblinImage, self.goblinRect)
            window.blit(self.goblinTitle, self.goblinTitleRect)
            window.blit(self.goblinDesc, self.goblinDescRect)
            window.blit(self.goblinsOwnedText, self.goblinsOwnedRect)
            window.blit(self.buyGoblinText, self.buyGoblinRect)
            window.blit(self.lockedText, self.lockedTextRect1)
            window.blit(self.lockedText, self.lockedTextRect2)
            window.blit(self.lockedText, self.lockedTextRect3)
            window.blit(self.lockedText, self.lockedTextRect4)
        elif self.unlocked == 2 and self.visible:
            window.blit(self.cookieGoblinImage, self.goblinRect)
            window.blit(self.goblinTitle, self.goblinTitleRect)
            window.blit(self.goblinDesc, self.goblinDescRect)
            window.blit(self.goblinsOwnedText, self.goblinsOwnedRect)
            window.blit(self.buyGoblinText, self.buyGoblinRect)
            window.blit(self.goblinTribeImage, self.tribeImageRect)
            window.blit(self.lockedText, self.lockedTextRect2)
            window.blit(self.lockedText, self.lockedTextRect3)
            window.blit(self.lockedText, self.lockedTextRect4)


chocolateChipCookie = Cookie(475, 300, 9)
structureMenu = StructureMenu()
upgradeMenu = UpgradeMenu()


def updateAll():
    chocolateChipCookie.draw()
    structureMenu.draw()
    upgradeMenu.draw()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            newFile = open("ccUserInfo.txt", "w")
            newFile.write("COOKIES - " + str(cookieCount) + "\n")
            newFile.write("OVERALL_CPS - " + str(CPS) + "\n")
            newFile.write("GOBLINS - " + str(goblinsOwned) + "\n")
            newFile.write("GOBLIN_PRICE - " + str(goblinPrice) + "\n")
            newFile.write("GOBLIN_CPS - " + str(goblinCPS) + "\n")
            newFile.write("CURSOR_PRICE - " + str(cursorUpgradePrice) + "\n")
            newFile.write("CURSOR_LEVEL - " + str(cursorLevel) + "\n")
            newFile.write("CURSOR_POWER - " + str(cursorPower) + "\n")
            newFile.write("UNLOCKED_STRUCTURES - " + str(structureMenu.unlocked) + "\n")
            newFile.close()
            run = False

        # if the cookie is clicked
        if event.type == pygame.MOUSEBUTTONUP and chocolateChipCookie.rect.collidepoint(pygame.mouse.get_pos()):
            cookieCount += cursorPower

        # if the structures 'button' is clicked
        if event.type == pygame.MOUSEBUTTONUP and structureMenu.structureButtonRect.collidepoint(
                pygame.mouse.get_pos()):
            if not structureMenu.visible:
                structureMenu.visible = True
            else:
                structureMenu.visible = False

        # if the upgrades 'button' is clicked
        if event.type == pygame.MOUSEBUTTONUP and upgradeMenu.upgradeButtonRect.collidepoint(pygame.mouse.get_pos()):
            if not upgradeMenu.visible:
                upgradeMenu.visible = True
            else:
                upgradeMenu.visible = False

        # if someone hits the buy button for the goblin
        if event.type == pygame.MOUSEBUTTONUP and structureMenu.visible and structureMenu.buyGoblinRect.collidepoint(
                pygame.mouse.get_pos()) and cookieCount >= int(goblinPrice):
            goblinsOwned += 1
            cookieCount -= int(goblinPrice)
            CPS += int(goblinCPS)
            goblinPrice = round(15 * (1.135 ** goblinsOwned))
            if goblinsOwned == 3:
                structureMenu.unlocked += 1
        # if someone hits the buy button for the cursor upgrade
        if event.type == pygame.MOUSEBUTTONUP and upgradeMenu.visible and upgradeMenu.upgradeCursorRect.collidepoint(
                pygame.mouse.get_pos()) and cookieCount >= int(cursorUpgradePrice):
            cursorLevel += 1
            cursorPower *= 2
            cookieCount -= int(cursorUpgradePrice)
            cursorUpgradePrice = (cursorPower * 450)

    if 0 < chocolateChipCookie.var <= 10:
        pygame.time.delay(100)
        chocolateChipCookie.rect[1] += 1
        chocolateChipCookie.var -= 1
        updateAll()
    elif 0 >= chocolateChipCookie.var > -10:
        pygame.time.delay(100)
        chocolateChipCookie.rect[1] -= 1
        chocolateChipCookie.var -= 1
        updateAll()
    else:
        pygame.time.delay(100)
        chocolateChipCookie.var = 10
        updateAll()

    timeCounter += clock.tick()
    if timeCounter >= 1000:
        cookieCount += CPS
        timeCounter = 0
    pygame.display.update()

pygame.quit()
exit()

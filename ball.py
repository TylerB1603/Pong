import pygame

class Ball():
  def __init__(self, x, y, xVel, yVel, width, height, color):
    self.x = x
    self.y = y
    self.xVel = xVel
    self.yVel = yVel
    self.width = width
    self.height = height
    self.color = color
    self.rect = (x, y, width, height)
    self.gameOver = False

  def draw(self, win):
    pygame.draw.rect(win, self.color, self.rect)

  def move(self, y1, y2):
    keys = pygame.key.get_pressed()
    if self.y < 0 or self.y > 480:
      self.yVel = -self.yVel
    if 10 < self.x < 20 and y1 - 20 <= self.y <= y1 + 120:
      self.xVel = -1.1 * self.xVel
      self.yVel = 2 * self.yVel
    elif 480 < self.x < 490 and y2 - 20 <= self.y <= y2 + 120:
      self.xVel = -1.1 * self.xVel
      self.yVel = 2 * self.yVel
    elif self.x < 0 or self.x > 480:
      self.x = 240
      self.y = 240
    if self.xVel == 0:
      self.xVel += 2
    if self.yVel == 0:
      self.yVel += 2
    self.x += self.xVel
    self.y += self.yVel
    self.update()

  def update(self):
    self.rect = (self.x, self.y, self.width, self.height)
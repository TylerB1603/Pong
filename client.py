import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player, player2, ball):
  win.fill((0, 0, 0))
  player.draw(win)
  player2.draw(win)
  ball.draw(win)
  pygame.display.update()

def main():
  global player
  run = True
  n = Network()
  pAndb = n.getP()
  if pAndb[1] == "0":
    p = pAndb[0][0]
    player = 1
  elif pAndb[1] == "1":
    p2 = pAndb[0][0]
    player = 2
  else:
    print(pAndb[1])
  b = pAndb[0][1]
  clock = pygame.time.Clock()
  while run:
    clock.tick(60)
    if player == 1:
      p2 = n.send([p, b])[0]
    elif player == 2:
      p = n.send([p2, b])[0]
    if (p2 != "1" and player == 1) or (p != "1" and player == 2):
      if player == 1:
        p.move()
      elif player == 2:
        p2.move()
      b.move(p.y, p2.y)
      redrawWindow(win, p, p2, b)
    else:
      print("2 players are required to play")
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()

main()
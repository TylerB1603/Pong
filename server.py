import socket, pickle, random
from _thread import *
from player import Player
from ball import Ball

server = "192.168.0.163"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

ballXspeed = ((-1)^random.randint(0,1)) * random.randint(1,3)
ballYspeed = ((-1)^random.randint(0,1)) * random.randint(1,3)

players = [[Player(10, 200, 10, 100, (255, 255, 255)), Ball(240, 240, ballXspeed, ballYspeed, 20, 20, (255, 255, 255))], [Player(480, 200, 10, 100, (255, 255, 255)), Ball(240, 240, ballXspeed, ballYspeed, 20, 20, (255, 255, 255))]]

def threaded_client(conn, player):
  global playerCount
  conn.send(pickle.dumps([players[playerCount], str(playerCount)]))
  playerCount += 1
  reply = ""
  while True:
    try:
      data = pickle.loads(conn.recv(2048))
      players[player] = data
      if not data:
        print("Disconnected")
        playerCount -= 1
        break
      else:
        if playerCount >= 2:
          if player == 1:
            reply = players[0]
          else:
            reply = players[1]
        else:
          reply = "1"
        conn.sendall(pickle.dumps(reply))
        print("Sent data")
    except:
      break
  print("Lost connection")
  playerCount -= 1
  conn.close()

currentPlayer = 0
playerCount = 0

while True:
  conn, addr = s.accept()
  print("Connected to:", addr)
  start_new_thread(threaded_client, (conn, currentPlayer))
  currentPlayer += 1
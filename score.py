#!/usr/bin/env python3
from time import sleep

key = [1,1,1]
while(True):
    try:
        players = {}
        playerScore = {}
        a = open("log.txt","r")
        lines = a.read().split('\n')
        lines.pop(0)
        lines.pop()
        a.close()
        for line in lines:
            name = line.split(' ')[0]
            if(not name in players):
                players[name] = []
            players[name].append(line.split(' ')[1])
        for player in players:
            playerScore[player] = 0
            for i in range(3):
                if(key[i] == int(players[player][i])):
                    playerScore[player] += 1
        print(playerScore)
        a = open("/var/www/html/end.html","r")
        web = a.read()
        webLines = web.split("\n")
        buf = "<ol>\n"
        for player in playerScore:
            buf += "<li>" + player + " scored " + str(playerScore[player]) + "</li>" + '\n'
        buf += "\n</ol>\n"
        startln = 0
        endln = 0
        #print(webLines)
        for num in range(len(webLines)):
            if(webLines[num].replace("\t","").replace(" ","") == "<ol>"):
                startln = num
            if(webLines[num].replace("\t","").replace(" ","") == "</ol>"):
                endln = num
        #print(startln, endln)
        #print(webLines[startln],webLines[endln])
        a.close()
        out = ""
        for i in range(len(webLines)):
            if(i == startln):
                out += buf
            elif(i >startln and (i <=endln)):
                continue
            else:
                out += webLines[i] + "\n"
        a = open("/var/www/html/end.html","w")
        a.write(out)
        a.close()

        sleep(1)
    except:
        print("Waiting...")
        sleep(2)

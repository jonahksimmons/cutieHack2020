# cutieHack2020 project, Kwizard
CutieHack project (November 7, 2020)

## Overview
This is a hack-a-thon project done in under 12 hours. We have an AR app combined with something inspired by Kahoot. The teacher brings up a question, and students use their phones to select answers that are displayed around their rooms. The server runs on 2 distinct ports: 80 for the frontend/GET backend, and 8080 (default) for POST backend. This can easily be setup to run over WAN.

## Setup
### Server
The server we used was run by apache2, but it just needs to host the html files. For the server, just host all the html files and q1 to q3 text files (for GET backend). The score.py and server.py projects need to be running as well. 

Note: If your apache service isn't running out of `/var/www/html`, you'll need to edit that line in score.py.

### Phone
The apps in the "Builds" dir are the current builds. At the time of writing, we only have android, but we might support iPhone in the future. 
To setup the phone, simply download the desired build and run. It should automatically connect to the server and start the game.

## Usage
### Server
Run the apache2 service, score.py script, and server.py script. Then navigate to the website (ie. localhost) and direct your students through the questions. The scoreboard will auto-update. To reset, just run 
`echo "" > log.txt` 
or clear the log file.

### Users
Just run the game. The app will auto-connect and send the answer when you tap on the screen.

## Future work
We would like to update the app to allow variable usernames, changable servers, and more devices (iPhones). 

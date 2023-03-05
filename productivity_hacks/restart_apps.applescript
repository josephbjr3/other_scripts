(* 
Here, I'm just restarting apps that commonly ask to restart to update.
View the crontab_instructions.txt to learn how to run this script weekly.
*)
tell application "Visual Studio Code" to quit
delay 2
tell application "Visual Studio Code" to activate

tell application "Discord" to quit
delay 2
tell application "Discord" to activate

tell application "zoom.us" to quit
delay 2
tell application "zoom.us" to activate

tell application "Surfshark" to quit
delay 2
tell application "Surfshark" to activate

tell application "Google Chrome" to quit
delay 2
tell application "Google Chrome" to activate

tell application "System Events"
    tell process "Google Chrome"
        set frontmost to true
        keystroke "," using command down
    end tell
end tell

delay 5

tell application "Google Chrome"
    keystroke "r" using command down
    delay 2
    quit
    delay 2
    activate
end tell

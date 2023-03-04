set restart_apps to {"Visual Studio Code", "Discord", "zoom.us", "Surfshark"}

-- set the restart day and time
set restart_day to 0 -- 0 = Sunday, 1 = Monday, 2 = Tuesday, etc.
set restart_time to "05:00:00" -- format: "HH:mm:ss"

-- calculate the next restart time
set next_restart to current date
set weekday of next_restart to restart_day
set time of next_restart to restart_time
if next_restart ² (current date) then
    set next_restart to next_restart + (7 * days)
end if

repeat
    set current_time to current date
    if current_time ³ next_restart then
        repeat with app_name in restart_apps
            tell application app_name
                if running then
                    quit
                    delay 5
                end if
                activate
            end tell
        end repeat
        
        -- wait a minute to allow apps to fully close
        delay 60
        
        repeat with app_name in restart_apps
            tell application app_name
                activate
            end tell
        end repeat
        
        -- update next restart time
        set next_restart to next_restart + (7 * days)
    end if
    delay 60 -- check every minute
end repeat

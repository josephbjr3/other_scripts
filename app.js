const { exec } = require('child_process');

// Set the apps that need to be restarted
const apps = [
  "Visual Studio Code",
  "Discord",
  "zoom.us",
  "Surfshark",
  "Google Chrome"
];

// Get the current date and time
const now = new Date();

// Calculate the date of the next Sunday at 5 am
const nextSunday = new Date(now.getTime() + (7 - now.getDay()) % 7 * 24 * 60 * 60 * 1000);
nextSunday.setHours(5, 0, 0, 0);

// Calculate the time until the next Sunday at 5 am
const timeUntilNextSunday = nextSunday.getTime() - now.getTime();

// Convert the time to hours and minutes
const hoursUntilNextSunday = Math.floor(timeUntilNextSunday / (60 * 60 * 1000));
const minutesUntilNextSunday = Math.floor((timeUntilNextSunday % (60 * 60 * 1000)) / (60 * 1000));

console.log(`Next restart will be on ${nextSunday} (${hoursUntilNextSunday} hours and ${minutesUntilNextSunday} minutes from now)`);

// Schedule the restart to happen on the next Sunday at 5 am
setTimeout(() => {
  console.log("Restarting apps...");

  // Restart each app
  apps.forEach((app) => {
    exec(`osascript -e 'tell application "${app}" to quit'`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Failed to quit ${app}: ${error.message}`);
        return;
      }
      console.log(`${app} has been quit`);
    });
    setTimeout(() => {
      exec(`open -a "${app}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`Failed to open ${app}: ${error.message}`);
          return;
        }
        console.log(`${app} has been opened`);
      });
    }, 2000); // Wait 2 seconds before reopening the app
  });

}, timeUntilNextSunday);

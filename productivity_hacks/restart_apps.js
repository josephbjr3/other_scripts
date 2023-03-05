/* 
This is the js version of my restart_apps script.
I'm just restarting apps that commonly ask for a restart to update.
I'm still working on this script.
*/


const { exec } = require('child_process');

// Set the apps that need to be restarted
const apps = [
  "Visual Studio Code",
  "Discord",
  "zoom.us",
  "Surfshark",
  "Google Chrome"
];

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

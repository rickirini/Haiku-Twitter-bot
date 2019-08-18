████████╗██╗    ██╗███████╗███████╗██╗  ██╗██╗   ██╗
╚══██╔══╝██║    ██║██╔════╝██╔════╝██║ ██╔╝██║   ██║
   ██║   ██║ █╗ ██║█████╗  █████╗  █████╔╝ ██║   ██║
   ██║   ██║███╗██║██╔══╝  ██╔══╝  ██╔═██╗ ██║   ██║
   ██║   ╚███╔███╔╝███████╗███████╗██║  ██╗╚██████╔╝
   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝


ACCIDENTAL HAIKU TWITTER BOT TWEEKU version 1.0 12/04/2017

AUTHOR NOTES
-------------------
Thank you for using the Tweeku application
This is application is created by students information science Marloes Kuijper,
Rick Kosse and Mike van Lenthe from University of Groningen


REQUIREMENTS
-------------------
- Tweepy library
- Twitter account credentials
- Tweeku files (zip file)
- Tweets (.out format (JSON))


TWEEKU INSTALLATION UNDER MAC OS/X or LINUX
-------------------
- Extract files into one directory (with git clone https://bitbucket.org/MMKuijper/gp-haiku/src/)
- Edit CREDENTIALS.PY with your own twitter key, secrets and token


START AND STOP TWEEKU
-------------------
-  START
  - Open terminal
  - Navigate (CD) to the tweeku directory (where you extracted the zip files)
  - Enter tweeku.py in the terminal
  - Tweeku will start

-  STOP
  - Click on the X button in the right upper corner to stop and close Tweeku


HOURLY TWEET
-------------------
- The hourly tweet depends on which button is clicked (default accidental Tweeku).
  When you click on the hourly tweet button before clicking on a generate button it will hourly tweet an accidental Tweeku. Clicking on a generate button before clicking on the hourly tweet button will set the hourly tweet button to that specific generate function, e.g. first lick on Generate random Tweeku button then on hourly button will automatically hourly tweet a random Tweeku.

- MENTON that when the hourly tweet button is clicked, it will run as a background process (so you can continue with generating your favorite Tweeku's)
  You can stop the function by clicking on the stop button. Closing the Tweeku application will also stop the hourly tweet function.


GENERAL USAGE NOTES
-------------------
- MENTION that if you click on a generate button you will have some wait time depending on how
  many tweet files (.out format) in your tweets directory


CUSTOM USAGE
-------------------
- If you want to use Tweeku with your own collection of tweets:
    - copy or move your own collection (.out format) to the tweets directory
      (located in the directory where you extracted the zip file)

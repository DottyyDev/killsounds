# killsounds
another skywars thingy, it plays custom sounds on various events such as kills, black magic, wins, and most importantly, blasts your ears on an assist

# How to use

I would say its pretty easy, but i have zero clue the talent most of you have, so who knows!

* download it
* unzip it
* make sure you have python installed
* go into values.txt and find a logs folder for minecraft, the one i personally use is the lunar client one, which is found at C:/Users/[your windows user]/.lunarclient/logs/launcher/renderer.log, but i think the normal minecraft logs also work
* go to command line and type in the following command `py -m pip install playsound`, this installs the one python plugin used in this project.
* Now you should be all set to use the project, so go in the folder the project is in, press `shift+right click`, and select `Open PowerShell window here`, once it loads type in the terminal `py main.py` and it shoudl start!
  
# Features
  
* Sound on kill
* Sound on win
* Sound on getting an ender pearl via Black Magic perk
* Alarm sound when getting an assist(so you know you didnt get strength and die form a kill steal)
* A system that keeps two lists that reset every session, God gamers and Bhoppers
# Modding
The code was basically designed to be added to. If you know pyhton well you can figure it out but for all the brainless skywars players that hard focus someone and then get you both killed, heres how you do it
  
On lines 13 and 15, you will see the following two lists:
  
``` py 
listen = ['+1 Ender Pearl! (Black Magic Perk)','You have assisted killing','You won! Want to play again? Click here! ','+1 SkyWars Experience (Kill)'] # What the program should look for in the chat logs

play = ['pearl','assist','win','kill'] # The corresponding sound's name, in the same position on the list
```
The first list, `listen` is what the program listens for in the chat logs, so if i want to add a sound for every time diamondpiercer procks, i would put in `Your diamond piercer perk hit`(theres a name in the full thing so half of the message prevents most missfires)

The second list, `play`, is what the program plays from the `./assets` folder, make sure whenever you add somehting or change a sound, it is the same name as the one you replaced it with OR you went into the code and changed it yourself. The sounds position on the list corresponds with what is triggers from, so the first sound file name on the list triggers whenever the first phrase ont he listener list is found.
  
# Enjoy!

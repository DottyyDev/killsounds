
from playsound import playsound

txt = open('./values.txt')
print('discovered values.txt')
txt = txt.readline()

kills = 0

thefile = open(txt)
print('found the specified logs files')

listen = ['+1 Ender Pearl!','You have assisted killing','SkyWars Experience (Win)','SkyWars Experience (Kill)'] # What the program should look for in the chat logs

play = ['pearl','assist','win','kill'] # The corresponding sound's name, in the same position on the list


thefile.seek(0, 2)
print('entering the loop!')
while True:
    line = thefile.readline()
    for x in listen:
        if x in line:
            if x == 'SkyWars Experience (Kill)':
                if kills < 5:
                    kills += 1
                playsound(str('./assets/kill/'+str(kills)+'.mp3'), False)
            else:
                playsound(str('./assets/'+play[listen.index(x)]+'.mp3'), False)
                break    
    if 'Cages opened! FIGHT!' in line:
        kills = 0

from playsound import playsound

txt = open('./values.txt')
print('discovered values.txt')
txt = txt.readline()

thefile = open(txt)
print('found the specified logs files')

listen = ['+1 Ender Pearl! (Black Magic Perk)','You have assisted killing','You won! Want to play again? Click here! ','+1 SkyWars Experience (Kill)'] # What the program should look for in the chat logs

play = ['pearl','assist','win','kill'] # The corresponding sound's name, in the same position on the list

hoppers = []
gods = []
thefile.seek(0, 2)
print('entering the loop!')
while True:

    line = thefile.readline()
    for x in listen:
        if x in line:
            playsound(str('./assets/'+play[listen.index(x)]+'.mp3'))
            break    
    for x in hoppers:
        if x in line:
            playsound('./assets/hecker.mp3')
            break
    for x in gods:
        if x in line:
            playsound('./assets/god.mp3')
    if '!hopper ' in line:
        hoppers.append(line.split('!hopper ',1)[1])
        print('added to hopper list!')
    if '!god' in line:
        gods.append(line.split('god ',1)[1])
        print('added to god list!')
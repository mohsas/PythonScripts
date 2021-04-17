choices = {1:'Monday', 2:'Tuesday', 3: 'Wednesday',4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
while True:
    try:
        print('Enter integer in[1..7]')
        msg = int(input())
    except ValueError:
        print("Not Valid!")
        continue
    if msg > 7 or msg < 1:
        print("Not Valid!")
        continue
    else:
        result = choices.get(msg)
        print('Your choice ', result)
        break


    

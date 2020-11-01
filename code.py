import string
import random
import webbrowser
print('url scrap by Andrew')

def len_instrument():
    vvod = input('len >>>')
    print(len(vvod))
    input()
    
ma = input('do you want to open len_instrument? y/n')
if ma  == 'y':
    len_instrument()
if ma == 'n':
    pass

url_ready = input('URL e.g. https://bit.ly/ >>>')
url_ready_2 = url_ready

if url_ready == 'https://prnt.sc/':
    print('LIGHTSHOT MODE')
    many = int(input('how many characters in url? >>>'))
    times = int(input('how many times do you want to scrap? >>>'))
    for i in range(times):
        for g in range(many):
            random_letter = 'abcdefghijklmnopqrstuvwxyz'
            m = random.randrange(0,25)
            yu = random_letter[m]
            random_int = random.randint(1,9)
            url_ready = str(url_ready) + str(yu)
        print(url_ready)
        webbrowser.open_new(url_ready)
        url_ready = url_ready_2



many = int(input('how many characters in url? >>>'))
times = int(input('how many times do you want to scrap? >>>'))
for i in range(times):
    for g in range(many):
        random_letter = random.choice(string.ascii_letters)
        random_int = random.randint(1,9)
        url_ready = str(url_ready) + str(random_letter)
    print(url_ready)
    webbrowser.open_new(url_ready)
    url_ready = url_ready_2

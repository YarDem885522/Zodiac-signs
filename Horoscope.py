import random
from time import sleep
ChoLan = input('Choice the language:(English),(Русский),(Беларуская мова): ')
if ChoLan == 'Русский':
    while True:
        a = input('Введи знак зодиака: ')
        b = ['У вас сегодня будет счастье','У вас случится беда','Вы попадете в неприятности','Вы познакомитесь с новыми людьми','На вас упадет кирпич']
        if a == 'Рыба':
            b.pop(1)
            b.pop(1)
            b.pop(2)
            print(random.choices(b))    
            break
        elif a == 'Козерог':
            b.pop(1)
            b.pop(1)
            b.pop(2)
            print(random.choices(b))
            break
        elif a == 'Стрелец':
            print(random.choices(b))
            break
        elif a == 'Рак':
            print(random.choices(b))
            break
        elif a == 'Близнецы':
            print(random.choices(b))
            break
        elif a == 'Овен':
            print(random.choices(b))
            break
        elif a == 'Лев':
            print(random.choices(b))
            break
        elif a == 'Весы':
            print(random.choices(b))
            break
        elif a == 'Скорпион':
            print(random.choices(b))
            break
        elif a == 'Телец':
            print(random.choices(b))
            break
        elif a == 'Водолей':
            print(random.choices(b))
            break
        elif a == 'Дева':
            print(random.choices(b))
            break
        else:
            print('Вы ошиблись')
elif ChoLan == 'English':
    while True:
        a = input('Enter your zodiac sign: ')
        b = ['You will have happiness today','You will have trouble','You will get into trouble','You will meet new people','A brick will fall on you']
        if a == 'Fish':
            b.pop(1)
            b.pop(1)
            b.pop(2)
            print(random.choices(b))    
            break
        elif a == 'Capricorn':
            b.pop(1)
            b.pop(1)
            b.pop(2)
            print(random.choices(b))
            break
        elif a == 'Sagittarius':
            print(random.choices(b))
            break
        elif a == 'Cancer':
            print(random.choices(b))
            break
        elif a == 'Twins':
            print(random.choices(b))
            break
        elif a == 'Aries':
            print(random.choices(b))
            break
        elif a == 'Lion':
            print(random.choices(b))
            break
        elif a == 'Scales':
            print(random.choices(b))
            break
        elif a == 'Scorpion':
            print(random.choices(b))
            break
        elif a == 'Taurus':
            print(random.choices(b))
            break
        elif a == 'Aquarius':
            print(random.choices(b))
            break
        elif a == 'Virgo':
            print(random.choices(b))
            break
        else:
            print('''Y're slip up''')
elif ChoLan == 'Беларуская мова':
                  print('Извините его еще не добавили)')
                  sleep(5)
                  exit()
else:
    print('Sorry, choose the correct option suggested.')

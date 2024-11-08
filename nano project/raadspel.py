import random
def nummer_raadspel():
    naam = input('Wat is je naam? ')
    welkom = 'Welkom bij het nummer raadspel, '
    print(welkom + naam)
    print('Je hebt 3 pogingen om het juiste nummer te raden tussen 1 en 10.')

    random_nummer = random.randrange(1, 11)
    pogingen = 3
    x = 0

    while x < pogingen:
        gok = int(input('Gok een nummer tussen 1 en 10: '))

        if gok < 1 or gok > 10:
            print("Dit nummer is buiten de range. Probeer opnieuw.")
            continue

        if gok == random_nummer:
            print(f'Gefeliciteerd {naam}! Je hebt het juiste nummer geraden.')
            break
        elif gok > random_nummer:
            print('Je hebt te hoog gegokt.')
        else:
            print('Je hebt te laag gegokt.')

        x += 1
        if x == pogingen:
            print(f'Helaas, je hebt verloren. Het juiste nummer was {random_nummer}.')

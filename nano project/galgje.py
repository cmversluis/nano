import random


def laad_woorden_uit_file():
    woorden_per_niveau = {'makkelijk': [], 'gemiddeld': [], 'moeilijk': []}

    try:
        with open("woorden.txt", "r") as file:
            for line in file:
                if ":" in line:
                    level, woorden = line.strip().split(":")
                    woorden_per_niveau[level] = woorden.split(",")
    except FileNotFoundError:
        print("Fout: Het bestand 'woorden.txt' kon niet worden gevonden.")
    except Exception as e:
        print(f"Fout bij het laden van woorden: {e}")

    return woorden_per_niveau


# Function to select a word based on difficulty level
def kies_woord(moeilijkheid):
    woorden_per_niveau = laad_woorden_uit_file()
    return random.choice(woorden_per_niveau.get(moeilijkheid, []))


# Function to determine the number of attempts based on difficulty
def bepaal_pogingen(moeilijkheid):
    if moeilijkheid == 'makkelijk':
        return 10
    elif moeilijkheid == 'gemiddeld':
        return 8
    elif moeilijkheid == 'moeilijk':
        return 6


# Function to save the score
def sla_score_op(naam, woord, pogingen, foutieve_pogingen):
    with open("scores.txt", "a") as file:
        file.write(f"{naam},{woord},{pogingen - foutieve_pogingen},{foutieve_pogingen}\n")


# Function to play the game
def speel_galgje():
    naam = input("Wat is je naam? ")
    print("Kies een moeilijkheidsgraad: makkelijk, gemiddeld, moeilijk")
    moeilijkheid = input().lower()

    if moeilijkheid not in ['makkelijk', 'gemiddeld', 'moeilijk']:
        print("Ongeldige moeilijkheidsgraad gekozen.")
        return

    woord = kies_woord(moeilijkheid)
    if not woord:
        print(f"Geen woorden gevonden voor moeilijkheidsgraad '{moeilijkheid}' in het bestand.")
        return

    pogingen = bepaal_pogingen(moeilijkheid)
    geraden_letters = []
    foutieve_pogingen = 0

    print(f"Welkom, {naam}! Laten we Galgje spelen.")
    print(f"Het woord dat je moet raden heeft {len(woord)} letters en je hebt {pogingen} pogingen.")

    while foutieve_pogingen < pogingen:
        status = ''.join([letter if letter in geraden_letters else '_' for letter in woord])
        print(f"Woord: {status}")
        keuze = input("Wil je een letter raden of het hele woord? Typ 'letter' of 'woord': ").lower()

        if keuze == 'letter':
            letter = input("Raad een letter: ").lower()

            if letter in geraden_letters:
                print("Deze letter heb je al geraden.")
                continue

            geraden_letters.append(letter)

            if letter in woord:
                print(f"Goed gedaan! De letter '{letter}' zit in het woord.")
            else:
                foutieve_pogingen += 1
                print(f"Fout! Je hebt nog {pogingen - foutieve_pogingen} pogingen over.")

        elif keuze == 'woord':
            geraden_woord = input("Wat denk je dat het woord is? ").lower()

            if geraden_woord == woord:
                print(f"Gefeliciteerd, {naam}! Je hebt het woord in één keer goed geraden: {woord}")
                sla_score_op(naam, woord, pogingen, foutieve_pogingen)
                return
            else:
                foutieve_pogingen += 1
                print(
                    f"Fout! '{geraden_woord}' is niet het juiste woord. Je hebt nog {pogingen - foutieve_pogingen} pogingen over.")
        else:
            print("Ongeldige keuze, probeer opnieuw.")

        if set(woord) <= set(geraden_letters):
            print(f"Gefeliciteerd, {naam}! Je hebt het woord geraden: {woord}")
            sla_score_op(naam, woord, pogingen, foutieve_pogingen)
            return

    print(f"Helaas, je hebt verloren. Het woord was: {woord}")
    sla_score_op(naam, woord, pogingen, foutieve_pogingen)




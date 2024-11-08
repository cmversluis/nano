import galgje
import raadspel



def boot_up():
    print("Welkom bij het spelmenu!")
    print("\nMenu:")
    print("1. Speel Galgje")
    print("2. Speel het nummer raadspel")
    print("3. Bekijk de regels")
    print("4. Stop")

    keuze = input("\nMaak een keuze (1, 2, 3, of 4): ")
    return keuze


# Functie om de regels te tonen
def toon_regels():
    print("\nRegels van het spel:")
    print("1. Galgje: Raad het woord door letters of het hele woord te raden.")
    print("2. Nummer raadspel: Raad het juiste nummer tussen 1 en 10. Je hebt 3 pogingen.")
    print("Veel succes!")

def main():
    while True:
        keuze = boot_up()

        if keuze == '1':
            galgje.speel_galgje()
        elif keuze == '2':
            raadspel.nummer_raadspel()
        elif keuze == '3':
            toon_regels()
        elif keuze == '4':
            print("Bedankt voor het spelen! Tot ziens.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")


# Start het spel
main()

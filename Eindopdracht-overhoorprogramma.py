import os

DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '-'
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'

def kies_lijst(lijstnaam):
  global STANDAARD_LIJST
  leeg_scherm()
  print("gedaan! de lijst die je nu hebt geselecteerd is " + lijstnaam + EXTENSIE)
  STANDAARD_LIJST = lijstnaam
  doorgaan = input("druk op ENTER om door te gaan ")
  print(doorgaan)


def leeg_scherm():
  os.system('cls||clear')


def nieuwe_lijst_naam():
  nieuwelijstnaam = STANDAARD_LIJST
  return nieuwelijstnaam


def overhoren(woordenlijst):
  leeg_scherm()
  f = open(STANDAARD_LIJST + EXTENSIE)
  with open(STANDAARD_LIJST + EXTENSIE) as f:
    bestandsdata = f.read().split('\n')
  overhoorstoppen = True
  for item in bestandsdata:
    if overhoorstoppen == True:
      if not item == '':
        woord1, woord2 = item.split(SCHEIDER)
        leeg_scherm()
        print_header()
        print(print_regel("zeg " + STOPPEN + " als je wil stoppen"))
        print(print_regel("wat is de vertaling van " + woord1))
        print_footer()
        inputantwoord = input("")
        if inputantwoord == woord2:
          leeg_scherm()
          print_header()
          print(print_regel("je hebt het goed!"))
          print_footer()
          stop = input("druk op ENTER om door te gaan ")
          print(stop)
        elif inputantwoord == STOPPEN:
          print("hij is gestopt")
          stop = input("druk op ENTER om door te gaan ")
          print(stop)
          overhoorstoppen = False
        elif not inputantwoord == woord2:
          leeg_scherm()
          print_header()
          print(print_regel("jammer je hebt het niet goed..."))
          print(print_regel("het was " + woord2))
          print_footer()
          stop = input("druk op ENTER om door te gaan ")
          print(stop)


def print_afscheid():
  leeg_scherm()
  print_header()
  print(print_regel("tot de volgende keer! "))
  print_footer()


def print_footer():
  print(print_regel(""))
  print("="*SCHERMBREEDTE)


def print_header():
  print("="*SCHERMBREEDTE)
  print(print_regel(""))


def print_menu():
  leeg_scherm()
  print_header()
  print(print_regel("de geselecteerde woordenlijst is: " + STANDAARD_LIJST))
  print(print_regel(NIEUWE_LIJST + " = een nieuwe lijst maken"))
  print(print_regel(KIES_LIJST + " = een andere lijst selecteren"))
  print(print_regel(TOEVOEGEN + " = een woord toevoegen"))
  print(print_regel(OVERHOREN + " = de woordenlijst overhoren"))
  print(print_regel(STOPPEN + " = stoppen"))
  print_footer()


def print_regel(input):
  input_in_haakjes = ("|{:<78}|".format(input))
  return input_in_haakjes


def schrijf_woordenlijst(lijst):
  global STANDAARD_LIJST
  nieuwelijstnaam = input("wat wordt de naam van de nieuwe lijst? ")
  f = open(nieuwelijstnaam + EXTENSIE, "w")

  hoeveel_woorden = int(input("hoeveel woorden met vertalingen moeten in het bestand? "))
  for i in range(hoeveel_woorden):
    hoeveelste = str(i + 1)
    woord_met_vertaling = input("wat is het " + hoeveelste + "e woord met vertaling? (bijvoorbeeld charger-oplader) ")
    f.write(ab + "\n")
  STANDAARD_LIJST = woord_met_vertaling
  f.close()


def voeg_woorden_toe(woordenlijst):
  f = open(STANDAARD_LIJST + EXTENSIE, 'a')

  f.write(woordenlijst)

  f.close()

def main():
  print_menu()

  while (vraag := input("Uw keuze: ")) != STOPPEN:

    if vraag == NIEUWE_LIJST:
      schrijf_woordenlijst(STANDAARD_LIJST)
    elif vraag == KIES_LIJST:
      welke_lijst_selecteren = input("Welke lijst wil je selecteren? ")
      kies_lijst(welke_lijst_selecteren)
    elif vraag == OVERHOREN:
      overhoren(STANDAARD_LIJST)
    elif vraag == TOEVOEGEN:
      hoeveel_toevoegen = int(input("hoeveel woorden wil je toevoegen? "))
      for i in range(hoeveel_toevoegen):
        toevoegwoord = input("welke woorden wil je toevoegen (bijvoorbeeld table-tafel) ")
        toevoegwoord_met_enter = "\n" + toevoegwoord
      voeg_woorden_toe(toevoegwoord_met_enter)
    elif vraag == STOPPEN:
      print_afscheid()
    elif vraag == "r":
      f = open(STANDAARD_LIJST + EXTENSIE, 'w')

      f.write("door-deur\n")
      f.write("trashbin-prullenbak\n")
      f.write("mouse-muis\n")
      f.write("head-hoofd\n")

      f.close()
    else:
      print("wtf heb je nou weer geschreven")
      doorgaan = input("druk op ENTER om door te gaan ")
      print(doorgaan)

    print_menu()


main()

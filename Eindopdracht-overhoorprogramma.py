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
trueornot = True

def kies_lijst(lijstnaam):
  global STANDAARD_LIJST
  leeg_scherm()
  print("gedaan! de lijst die je nu hebt geselecteerd is " + lijstnaam + EXTENSIE)
  STANDAARD_LIJST = lijstnaam
  a = input("druk op ENTER om door te gaan ")
  print(a)
def leeg_scherm():
  os.system('cls||clear')
def nieuwe_lijst_naam():
  c = STANDAARD_LIJST
  return c
def overhoren(woordenlijst):
  leeg_scherm()
  f = open(STANDAARD_LIJST + EXTENSIE)
  with open(STANDAARD_LIJST + EXTENSIE) as f:
    bestandsdata = f.read().split('\n')
  overhoorstoppen = True
  for item in bestandsdata:
    if overhoorstoppen == True:
      if not item == '':
        print("a")
        woord1, woord2 = item.split(SCHEIDER)
        leeg_scherm()
        print_header()
        print(print_regel("zeg " + STOPPEN + " als je wil stoppen"))
        print(print_regel("wat is de vertaling van " + woord1))
        print_footer()
        haha = input("")
        if haha == woord2:
          leeg_scherm()
          print_header()
          print(print_regel("je hebt het goed!"))
          print_footer()
          stop = input("druk op ENTER om door te gaan ")
          print(stop)
        elif haha == STOPPEN:
          print("hij is gestopt")
          stop = input("druk op ENTER om door te gaan ")
          print(stop)
          overhoorstoppen = False
        elif not haha == woord2:
          leeg_scherm()
          print_header()
          print(print_regel("jammer je hebt het niet goed..."))
          print(print_regel("het was " + woord2))
          print_footer()
          stop = input("druk op ENTER om door te gaan ")
          print(stop)
def print_afscheid():
  print("tot de volgende keer! ")
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
  #b = ("|" + input + " "*(SCHERMBREEDTE - (2+len(input))) + "|")
  b = ("|{:<78}|".format(input))
  return b
def schrijf_woordenlijst(lijst):
  global STANDAARD_LIJST
  abv = input("wat wordt de naam van de nieuwe lijst? ")
  f = open(abv + EXTENSIE, "w")

  a = int(input("hoeveel woorden met vertalingen moeten in het bestand? "))
  for i in range(a):
    hoeveelste = str(i + 1)
    ab = input("wat is het " + hoeveelste + "e woord met vertaling? (bijvoorbeeld charger-oplader) ")
    f.write(ab + "\n")
  STANDAARD_LIJST = abv
  f.close()
def voeg_woorden_toe(woordenlijst):
  f = open(STANDAARD_LIJST + EXTENSIE, 'a')

  f.write(woordenlijst)

  f.close()
while trueornot == True:
  print_menu()

  vraag = input("Uw keuze: ")
  if vraag == NIEUWE_LIJST:
    schrijf_woordenlijst(STANDAARD_LIJST)
  elif vraag == KIES_LIJST:
    vraag2 = input("Welke lijst wil je selecteren? ")
    kies_lijst(vraag2)
  elif vraag == OVERHOREN:
    overhoren(STANDAARD_LIJST)
  elif vraag == TOEVOEGEN:
    ab = int(input("hoeveel woorden wil je toevoegen? "))
    for i in range(ab):
      av = input("welke woorden wil je toevoegen (bijvoorbeeld table-tafel) ")
      av2 = "\n" + av
    voeg_woorden_toe(av2)
  elif vraag == STOPPEN:
    print_afscheid()
    trueornot = False
  elif vraag == "r":
    f = open(STANDAARD_LIJST + EXTENSIE, 'w')

    f.write("door-deur\n")
    f.write("trashbin-prullenbak\n")
    f.write("mouse-muis\n")
    f.write("head-hoofd\n")

    f.close()
  else:
    print("wtf heb je nou weer geschreven")
    aa = input("druk op ENTER om door te gaan ")
    print(aa)

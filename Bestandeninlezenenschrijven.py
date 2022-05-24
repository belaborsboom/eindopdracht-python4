def lees_woordenlijst(bestandsnaam):
  scheider = "-"
  woordenlijst = {}
  f = open(bestandsnaam)
  for line in f:
    woord1, woord2 = line.strip('\n').split(scheider)
    woordenlijst[woord1] = woord2
  f.close()
  return woordenlijst
print(lees_woordenlijst("bestand.wrd"))

def bestand_schrijven(bestandsnaam, woordenlijst):
  scheider = "-"
  f = open("nl-en.wrd", 'w')

  for i in range(len(woordenlijst)):
    key = str(list(woordenlijst)[i])
    f.write(key + scheider + woordenlijst[key] + "\n")

  f.close()
woordenlijst = { "koe": "cow", "schaap": "sheep", "varken": "pig" }
bestand_schrijven("nl-en.wrd", woordenlijst)

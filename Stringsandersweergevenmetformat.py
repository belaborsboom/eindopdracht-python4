def de_basis():
  naam = input("Hoe heet je? ")
  print("-"*27)
  print(naam + ", wat leuk!")
  print("{:^21}".format(naam))
  print("Je naam is: {:>15}".format(naam))
  print("-"*27)
de_basis()

SCHERMBREEDTE = 60
MAX_WOORD_LENGTE = 14
def uitlijnen():
  woord = input("geef een woord ")
  print("+" + "-"*(SCHERMBREEDTE - MAX_WOORD_LENGTE - 2 ) + "+")
  print(("| Je gekozen woord:" + "{:>" + str(SCHERMBREEDTE - MAX_WOORD_LENGTE - 20) + "}").format(woord) + "|")
  print("+" + "-"*(SCHERMBREEDTE - MAX_WOORD_LENGTE - 2 ) + "+")
uitlijnen()

woord1 = input("geef een woord")
woord2 = input("geef een woord")
woord3 = input("geef een woord")

def print_regel(regel):
  print(("> {:" + str(SCHERMBREEDTE - MAX_WOORD_LENGTE - 4)+ "} <").format(regel))

print("-"*(SCHERMBREEDTE - MAX_WOORD_LENGTE))
print_regel(("Je eerste woord: {:>" + str(SCHERMBREEDTE - MAX_WOORD_LENGTE - 20) + "}").format(woord1))
print_regel(("Je tweede woord: {:>" + str(SCHERMBREEDTE - MAX_WOORD_LENGTE - 20) + "}").format(woord2))
print_regel(("Je derde woord: {:>" + str(SCHERMBREEDTE - MAX_WOORD_LENGTE - 19) + "}").format(woord3))
print("-"*(SCHERMBREEDTE - MAX_WOORD_LENGTE))

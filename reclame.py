from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
   return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - (prijs * korting):.2f} euro."

def inkomsten_totaal(inkomsten, btw):
   return f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {sum(inkomsten)*btw:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
   return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
   aantal = len(mijn_lijst)
   totaal = 0
   for element in mijn_lijst:
      totaal += element
   gemiddelde = totaal / aantal
   return f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro"

def meervoudig(invoer_lijst):
   return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
   korte_lijst = laag_en_hoog(invoer_lijst_2)
   uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
   return uitvoer
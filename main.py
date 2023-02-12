from Pojistenec import Pojistenec
import time                                                  # Při neplatné volbě a vrácení se do menu zastaví aplikaci na 0.75 vteřiny. Uživatelsky hezčí.

pojistenci = []
"""Seznam pojištěnců."""


def pridej_pojistenec(p):
    """Přidá do databáze nového pojištěnce."""
    jmeno = input("Zadejte křesní jméno: ").rstrip()
    jmeno = jmeno.capitalize()
    prijmeni = input("Zadejte příjmení: ").rstrip()
    prijmeni = prijmeni.capitalize()
    try:                                                       # Čekáme chybu v zadání - ošetřeno.
        vek = int(input("Zadejte věk: "))
    except ValueError:
        a = input("ZADEJTE VĚK V ČÍSLECH! - Přejete si pokračovat v zadávání pojištěnce? Y/N: ")
        if a == ("y" or "Y"):
            return pridej_pojistenec(p)
        elif a == ("n" or "N"):
            return menu()
        else:
            print()
            print("Neplatná volba, vracím se do menu.")
            time.sleep(0.75)
            return menu()
    telefonni_cislo = input("Zadejte telefonní číslo: ").rstrip()
    p.append(Pojistenec(jmeno, prijmeni, vek, telefonni_cislo))
    print()
    print("Pojištěnec úspěšně uložen v databázi.")


def ukaz_pojistenci(p):
    """Vybere všechny pojištěnce zadané v databázi."""
    for pojistenec in p:
        print(pojistenec)
    if len(p) == 0:
        print("Seznam je prázdný.")


def najdi_pojistenec(p):
    """Nejde určitého pojištěnce podle jména a příjmení."""
    jmeno = input("Zadejte jméno hledaného pojištěného: ")
    jmeno = jmeno.capitalize()
    prijmeni = input("Zadejte příjmení hledaného pojištěného: ")
    prijmeni = prijmeni.capitalize()
    for pojistenec in p:
        if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
            return pojistenec
    return None


def menu():
    """Úvodní konzolová obrazovka - interaktivní pro 4 možnosti výběru. Při nesprávném zadání vyhodí hlášku. """
    print("-----------------------------------------")
    print("---------Evidence pojištěných------------")
    print("-----------------------------------------")
    while True:
        print()
        print("1 = Přidat nového pojištěného")
        print("2 = Vypsat všechny pojištěné")
        print("3 = Vyhledat pojištěného")
        print("4 = Konec aplikace")
        volba = input("Zadejte volbu 1-4: ")

        if volba == "1":
            pridej_pojistenec(pojistenci)
        elif volba == "2":
            print()
            ukaz_pojistenci(pojistenci)
        elif volba == "3":
            nalezeny_pojistenec = najdi_pojistenec(pojistenci)
            if nalezeny_pojistenec is not None:
                print()
                print("Hledaný pojištěný:")
                print(nalezeny_pojistenec)
            else:
                print()
                print("Pojištěný nenalezen.")
                input("Pokračujte stisknutím ENTER")

        elif volba == "4":
            print()
            print("Ukončuji aplikaci.")
            return
        else:
            """Při neplatné volbě vyhodí hlášku"""
            print()
            print("Neznámá volba, zadejte prosím platnou volbu.")


menu()

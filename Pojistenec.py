class Pojistenec:
    """Třída pojištěnec - muster pro všechny ostatní pojištěnce."""
    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo

    def __str__(self):
        return self.jmeno + " " + self.prijmeni + ", " + str(self.vek) + " let, " + self.telefonni_cislo
class Mediu:
    def __init__(self, dimensiune):
        self.dimensiune = dimensiune
        self.organisme = []

    def adauga(self, organism):
        self.organisme.append(organism)

    def elimina(self, organism):
        if organism in self.organisme:
            self.organisme.remove(organism)

    def simuleaza(self, pasi):
        for i in range(pasi):
            print(f"Pas {i + 1}")
            for organism in self.organisme:
                organism.actiune(self)
            self.afiseaza()

    def afiseaza(self):
        for organism in self.organisme:
            print(f"{organism.nume} la ({organism.pozitie[0]}, {organism.pozitie[1]}) cu energia {organism.energie}")

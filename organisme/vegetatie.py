from organisme.organism import Organism
import random

class Vegetatie(Organism):
    def __init__(self, nume, energie, pozitie):
        super().__init__(nume, energie, pozitie)

    def actiune(self, mediu):
        if random.random() < 0.3:
            self.energie += 5
        elif self.energie > 10:
            mediu.adauga(Vegetatie(self.nume, 5, self.pozitie))

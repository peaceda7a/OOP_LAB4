from organisme.organism import Organism
from organisme.vegetatie import Vegetatie
import random
from abc import ABC

class Creatura(Organism, ABC):
    def __init__(self, nume, energie, pozitie, viteza, dieta):
        super().__init__(nume, energie, pozitie)
        self.viteza = viteza
        self.dieta = dieta

    def miscare(self, mediu):
        self.pozitie = (
            self.pozitie[0] + random.randint(-self.viteza, self.viteza),
            self.pozitie[1] + random.randint(-self.viteza, self.viteza)
        )

    def hranire(self, mediu):
        pass

class ConsumatorPlante(Creatura):
    def __init__(self, nume, energie, pozitie, viteza):
        super().__init__(nume, energie, pozitie, viteza, "vegetatie")

    def hranire(self, mediu):
        for ent in mediu.organisme:
            if isinstance(ent, Vegetatie) and ent.pozitie == self.pozitie:
                self.energie += ent.energie
                mediu.elimina(ent)
                break

    def actiune(self, mediu):
        self.miscare(mediu)
        self.hranire(mediu)

class ConsumatorCarne(Creatura):
    def __init__(self, nume, energie, pozitie, viteza):
        super().__init__(nume, energie, pozitie, viteza, "carne")

    def hranire(self, mediu):
        for ent in mediu.organisme:
            if isinstance(ent, Creatura) and ent != self and ent.pozitie == self.pozitie:
                self.energie += ent.energie
                mediu.elimina(ent)
                break

    def actiune(self, mediu):
        self.miscare(mediu)
        self.hranire(mediu)

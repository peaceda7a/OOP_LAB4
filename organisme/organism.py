from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, nume, energie, pozitie):
        self.nume = nume
        self.energie = energie
        self.pozitie = pozitie
        self.rata_supravietuire = 0.5

    @abstractmethod
    def actiune(self, mediu):
        pass

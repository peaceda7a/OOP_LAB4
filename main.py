from mediu.mediu import Mediu
from organisme.vegetatie import Vegetatie
from organisme.creatura import ConsumatorPlante, ConsumatorCarne

if __name__ == "__main__":
    mediu = Mediu((10, 10))
    mediu.adauga(Vegetatie("Iarba", 10, (1, 1)))
    mediu.adauga(ConsumatorPlante("Iepure", 20, (1, 1), 2))
    mediu.adauga(ConsumatorCarne("Lup", 30, (2, 2), 3))
    mediu.simuleaza(5)

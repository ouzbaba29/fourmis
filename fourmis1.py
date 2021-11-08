class Salle:
    def __init__(self, nom, taille):
        self.nom = nom
        self.fourmi = 0
        self.taille = taille
        self.connexion = []

    def is_full(self):
        if self.fourmi < self.taille:
            return False
        return True

    def set_connexion(self, salle):
        self.connexion.append(salle)

    def add_fourmi(self):
        self.fourmi += 1

    def remove_fourmi(self):
        self.fourmi -= 1


class Fourmi:

    def __init__(self, nom):
        self.nom = nom
        self.position = None
        self.moved = False

    def move(self, start, end):
        start.remove_fourmi()
        end.add_fourmi()
        self.has_move()
        print(self.nom + " - " + start.nom + " - " + end.nom)

    def has_move(self):
        self.moved = True

    def reinit_move(self):
        self.moved = False


class Fourmilliere:
    def __init__(self, end):
        self.graphe_salles = {}
        self.pos_fourmi = {}
        self.end = end

    def add_fourmi(self, f, S):
        self.pos_fourmi[S].append(f)
        S.add_fourmi()
        f.position = S

    def remove_fourmi(self, f, S):
        del self.pos_fourmi[S][self.pos_fourmi[S].index(f)]
        S.remove_fourmi()
        f.position = None

    def add_salle(self, salle):
        self.graphe_salles[salle] = salle.connexion
        self.pos_fourmi[salle] = list()

    def can_move(self, fourmi):
        if fourmi.moved is False:
            return True
        return False

    def display_chemin(self):
        print("Chemins : ")
        for cle, valeur in self.graphe_salles.items():
            for i in range(len(valeur)):
                print(cle.nom + " - " + valeur[i].nom)
        print("\n")

    def display_fourmi(self):
        print("Position des fourmis : ")
        for cle, valeur in self.pos_fourmi.items():
            for i in range(len(valeur)):
                print(valeur[i].nom + " - " + cle.nom)
        print("\n")

    def solve(self):
        nb_fourmi = len(list(self.pos_fourmi.values())) - 1
        step = 1
        while len(self.pos_fourmi[self.end]) < nb_fourmi:
            print("\nEtape", step, ":")
            self.display_fourmi()
            print("Mouvements : ")
            for cle in self.pos_fourmi.keys():
                for f in self.pos_fourmi[cle]:
                    f.reinit_move()
            for cle in self.graphe_salles.keys():
                for next_room in self.graphe_salles[cle]:
                    for fourmi in self.pos_fourmi[cle]:
                        if next_room.is_full() is False and self.can_move(fourmi) is True:
                            self.remove_fourmi(fourmi, cle)
                            self.add_fourmi(fourmi, next_room)
                            fourmi.move(cle, next_room)
                        elif len(list(self.pos_fourmi[next_room])) > 0 and self.can_move(fourmi) is True:
                            for next_fourmi in self.pos_fourmi[next_room]:
                                if self.can_move(next_fourmi) is True:
                                    self.remove_fourmi(fourmi, cle)
                                    self.add_fourmi(fourmi, next_room)
                                    fourmi.move(cle, next_room)
            step += 1


Sv = Salle('Sv', 10)
S1 = Salle('S1', 1)
S2 = Salle('S2', 1)
S3 = Salle('S3', 2)
S4 = Salle('S4', 1)
S5 = Salle('S5', 2)
Sd = Salle('Sd', 10)

Sv.set_connexion(S1)
Sv.set_connexion(S2)
Sv.set_connexion(S3)
S1.set_connexion(S4)
S3.set_connexion(S5)
S5.set_connexion(Sd)
S2.set_connexion(Sd)
S4.set_connexion(Sd)

F = Fourmilliere(Sd)
F.add_salle(Sv)
F.add_salle(S1)
F.add_salle(S2)
F.add_salle(S3)
F.add_salle(S4)
F.add_salle(S5)
F.add_salle(Sd)

f1 = Fourmi('f1')
F.add_fourmi(f1, Sv)
f2 = Fourmi('f2')
F.add_fourmi(f2, Sv)
f3 = Fourmi('f3')
F.add_fourmi(f3, Sv)
f4 = Fourmi('f4')
F.add_fourmi(f4, Sv)
f5 = Fourmi('f5')
F.add_fourmi(f5, Sv)
f6 = Fourmi('f6')
F.add_fourmi(f6, Sv)

F.solve()

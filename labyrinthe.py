import pyxel
import pprint

class Labyrinthe:
    """"""

    def __init__(self):
        pyxel.init(128, 128)
        self.origine = (1, 1)

        pyxel.load("3.pyxres")

        self.nb_blocs = 21
        self.taille_bloc = 6

        self.matrice = [[[self.origine[0] + (ligne * self.taille_bloc),
                         self.origine[1] + (colonne * self.taille_bloc),
                          0] 
                          for ligne in range(self.nb_blocs)] for colonne in range(self.nb_blocs)]

        for i in range(self.nb_blocs):
            self.matrice[i][i][2] = 1
            if i < (self.nb_blocs - 1):
                self.matrice[i][i+1][2] = 1


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(0)

        for ligne in range(self.nb_blocs):
            for colonne in range(self.nb_blocs):
                bloc = self.matrice[ligne][colonne]
                if bloc[2] == 0:
                    x = bloc[0]
                    y = bloc[1]
                    pyxel.blt(x, y, 0, 225, 40, 6, 6)

lab = Labyrinthe()

# pp = pprint.PrettyPrinter()
# pp.pprint(lab.matrice)

pyxel.run(lab.update, lab.draw)    



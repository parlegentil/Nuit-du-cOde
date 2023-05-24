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
        self.matrice = [[0 for ligne in range(self.nb_blocs)] for colonne in range(self.nb_blocs)]

        for i in range(self.nb_blocs):
            self.matrice[i][i] = 1
            if i < (self.nb_blocs - 1):
                self.matrice[i][i+1] = 1

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(0)
        for ligne in range(self.nb_blocs):
            for colonne in range(self.nb_blocs):
                if self.matrice[ligne][colonne] == 0:
                    x = self.origine[0] + (ligne * self.taille_bloc)
                    y = self.origine[1] + (colonne * self.taille_bloc)
                    pyxel.blt(x, y, 0, 225, 40, 6, 6)

lab = Labyrinthe()
pyxel.run(lab.update, lab.draw)

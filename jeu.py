import pyxel
import labyrinthe
import ennemi
import vaisseau

class Jeu:
    """"""

    directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def __init__(self):
        pyxel.init(128, 128)
        pyxel.mouse(visible=True)
        self.lab = labyrinthe.Labyrinthe()
        # self.vso = vaisseau.Vaisseau()
        self.ennemi = ennemi.Ennemi(self.lab.coords[3][5][0],
                                    self.lab.coords[3][5][1])


    def draw(self):
       self.lab.dessine()
       # self.vaisseau.dessine()
       self.ennemi.mouvement(self.lab.coords)
       self.ennemi.dessine()

    
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            dire = 1
        elif pyxel.btn(pyxel.KEY_LEFT):
            dire = 2
        elif pyxel.btn(pyxel.KEY_UP):
            dire = 4
        elif pyxel.btn(pyxel.KEY_DOWN):
            dire = 3
        else:
            dire = 0

jeu = Jeu()
pyxel.run(jeu.update, jeu.draw)


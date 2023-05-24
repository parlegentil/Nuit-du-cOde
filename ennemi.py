import pyxel

class Ennemi:
    """"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvitesse = 1
        self.yvitesse = 0
        pyxel.load("3.pyxres")


    def mouvement(self, coords):
        if self.x < 31 or self.x > 50:
            self.xvitesse *= -1

        self.x += self.xvitesse
        self.y += self.yvitesse


    def dessine(self):
        pyxel.blt(self.x, self.y, 0, 123, 20, 6, 6)


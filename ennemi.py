import pyxel

class Ennemi:
    """"""

    def __init__(self, x, y, idt):
        self.x = x
        self.y = y
        self.xvitesse = 1
        self.yvitesse = 1
        self.idt = idt
        pyxel.load("3.pyxres")


    def mouvement(self):
        if self.idt == 1:
            if self.x < 31 or self.x > 50:
                self.xvitesse *= -1
            self.x += self.xvitesse

        if self.idt == 3:
            if self.x < 25 or self.x > 50:
                self.xvitesse *= -1
            self.x += self.xvitesse

        if self.idt == 2:
            if self.y < 37 or self.y > 57:
                self.yvitesse *= -1
            self.y += self.yvitesse

        if self.idt == 4:
            if self.y < 102 or self.y > 122:
                self.yvitesse *= -1
            self.y += self.yvitesse


    def dessine(self):
        pyxel.blt(self.x, self.y, 0, 123, 20, 6, 6)


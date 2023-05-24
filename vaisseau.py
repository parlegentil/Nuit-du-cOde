# nuit du code

import pyxel 

class vaisseau:
    def __init__(self, coord, orientation):
        self.coord = coord
        self.orientation = orientation
    
    def mouvement(self, direction, lab):
        if direction

    def sur_ennemi(self):
        pass

    def dessin(self):
        if self.orientation == haut:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, 6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, 6)

        if self.orientation == bas:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, -6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, -6)

        if self.orientation == droite:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, 6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, 6, -3)

        if self.orientation == gauche:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, -6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, -6, -3)

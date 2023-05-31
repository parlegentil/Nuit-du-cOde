import pyxel

class Vaisseau:
    """"""

    def __init__(self, coord):
        self.coord = coord
        self.directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def sur_ennemi(self, ennemis):
        sur_enm = False
        for ennemi in ennemis:
            if (self.coord[0] > ennemi.x 
                and self.coord[0] < ennemi.x + 6
                and self.coord[1] > ennemi.y
                and self.coord[1] < ennemi.y + 6):

                sur_enm = True

            if (self.coord[0] + 6 > ennemi.x 
                and self.coord[0] + 6 < ennemi.x + 6
                and self.coord[1] > ennemi.y
                and self.coord[1] < ennemi.y + 6):

                sur_enm = True

            if (self.coord[0] > ennemi.x 
                and self.coord[0] < ennemi.x + 6
                and self.coord[1] + 6 > ennemi.y
                and self.coord[1] + 6 < ennemi.y + 6):

                sur_enm = True

            if (self.coord[0] + 6 > ennemi.x 
                and self.coord[0] + 6 < ennemi.x + 6
                and self.coord[1] + 6 > ennemi.y
                and self.coord[1] + 6 < ennemi.y + 6):

                sur_enm = True

        return sur_enm

    def pos_dans_lab(self, lab):
        position = (0, 0)
        for i in range(len(lab.coords)):
            for j in range(len(lab.coords[0])):
                if self.coord == lab.coords[i][j]:
                    position = (i, j)
        return position

    #
    def presence_sol(self, dire, lab):

        return lab.murs[self.pos_dans_lab(lab)[0] + self.directions[dire][0]][self.pos_dans_lab(lab)[1] + self.directions[dire][1]] == 1
    

    def mouvement(self, dire, lab):
        

        if not self.presence_sol(dire, lab):
            self.coord = (self.coord[0] + self.directions[dire][0], self.coord[1] + self.directions[dire][1])


    def dessine(self, dire, lab):
        
        self.mouvement(dire, lab)

        if dire == 4:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, 6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, 6)

        if dire == 3:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, -6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, -6)

        if dire == 1:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, 6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, 6, -3)

        if dire == 2:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, -6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, -6, -3)

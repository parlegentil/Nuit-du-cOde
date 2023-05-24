class vaisseau:
    """"""

    def __init__(self, coord):
        self.coord = coord
    
    def sur_ennemi(self):
        pass

    def pos_dans_lab(self, lab):
        position = (0, 0)
        for i in range(lab.coord):
            for j in range(lab.coord[0]):
                if self.coord == self.lab[i][j]:
                    position = (i, j)
        return position


    def presence_mur(self, dir, lab):
        return lab[self.pos_dans_lab()[0] + dir[0]][self.pos_dans_lab()[1] + dir[1]] == 1
    
    def mouvement(self, dir, lab):
        

    

    def dessin(self, dir):
        
        if dir == 4:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, 6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, 6)

        if dir == 3:
            pyxel.blt(self.coord[0], self.coord[1], 0, 2, 1, 3, -6)
            pyxel.blt(self.coord[0] + 3, self.coord[1], 0, 2, 1, -3, -6)

        if dir == 1:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, 6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, 6, -3)

        if dir == 2:
            pyxel.blt(self.coord[0], self.coord[1], 0, 77, 41, -6, 3)
            pyxel.blt(self.coord[0], self.coord[1] + 3, 0, 77, 41, -6, -3)





class Jeu():

    directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        self.lab = Labyrinthe()
        self.vso = vaisseau()

    def draw(self):
        pass
    
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            dir = 1
        elif pyxel.btn(pyxel.KEY_LEFT):
            dir = 2
        elif pyxel.btn(pyxel.KEY_UP):
            dir = 4
        elif pyxel.btn(pyxel.KEY_DOWN):
            dir = 3
        else:
            dir = 0

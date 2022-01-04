
import random
carrésAVérifier = 0
def créer_terrainMiné(terrainMiné):
    global carrésAVérifier
    for rangée in range(0,10):
        listeRangée = []
        for colonne in range(0,10):
            if random.randint(1,100) < 20:
                listeRangée.append(1)
            else:
                listeRangée.append(0)
                carrésAVérifier = carrésAVérifier + 1
        terrainMiné.append(listeRangée)
       
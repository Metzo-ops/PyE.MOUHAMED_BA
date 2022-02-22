from re import S


def moy(fichier):
    Somme = 0
    for line in fichier:
        Somme = Somme + line
        moy1 = Somme/len(fichier)
        print(moy1)
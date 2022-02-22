def func_inv(fichier):
    liste_des_el_ayant_rendu_la_ligne_invalide = []
    liste_non_valide = []
    liste_valide = []

    for ligne in fichier :
        if len(ligne[1]) != 7 or not ligne[1].isalpha() or (not ligne[2].isalpha() or len(ligne[2]) < 2) or (
                not ligne[3].isalpha() or len(ligne[3]) < 3):

            liste_non_valide.append(ligne)
        else:
            liste_valide.append(ligne)
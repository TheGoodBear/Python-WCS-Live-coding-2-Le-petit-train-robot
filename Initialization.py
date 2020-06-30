# coding: utf-8

def ShowTitleAndRules():

    print("Le petit train robot")
    print("--------------------")
    print()
    print("L'objectif du jeu est, en un minimum d'instructions, de programmer un train pour :")
    print("    - qu'il charge toutes les marchandise")
    print("    - qu'il les décharge à l'entrepôt")
    print("    - qu'il revienne à son garage")
    print()
    print("Règles particulières :")
    print("    - lorsque les objectifs ci-dessus sont remplis, la partie est gagnée")
    print("    - si le train tombe en panne d'énergie, la partie est perdue")
    print("    - les instructions doivent être séparées par un espace")
    print()
    print("Instructions comprises par le train :")
    print("    - (A)vancer de n cases (par exemple A5)")
    print("    - (R)eculer de n cases (par exemple R12)")
    print("    - (C)harger des marchandises (seulement sur un emplacement de marchandises et à concurrence de la capacité de charge maximum)")
    print("    - (D)écharger les marchandises (seulement à l'entrepôt)")
    print("    - Recharger en (E)nergie (seulement sur une station de charge, et remet la charge au niveau maximum)")

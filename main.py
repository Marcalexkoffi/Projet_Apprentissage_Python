liste_Livres = []
liste_Livres.append("Alice au pays des merveilles")
liste_Livres.append("Les bases en Java")
liste_Livres.append("Le cauchemard")

print("Bienvenue dans notre bibliothèque numérique 🤗")
choix1 = input("Taper 1 pour afficher le menu ou 0 pour fermer la session :  ")
if(choix1 == "1") :
    print(" ")
    print(" Menu ")
    print(" ")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Quitter")
choix2 = input("Veuillez choisir une option    ")
match choix2 :
    case "1" :
        nvLivre = input("Entrez le nom du livre ")
        liste_Livres.append(nvLivre)
        print("Le livre a été ajouter avec succès, choisir l'option 2 pour voir la liste de Livres")
    case "2" :
        for livre in liste_Livres :
         print(livre)
    case "3" :
      print("Merci de vitre viste, à bientôt")
      exit()
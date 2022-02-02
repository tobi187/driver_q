import logic

# hauptfile


# Einstiegspunkt
def start():
    fragen_liste = logic.fragen_einlesen()

    logic.fragen_stellen(fragen_liste)

    anzahl_richtig = logic.zaehle_richtige_antworten(fragen_liste)

    print("\n")
    print("Herzlichen Glückwunsch, du hast " +
          anzahl_richtig + "von 10 richtig beantwortet")
    print("\n")

    auswertung_anzeigen = input("Auswertung anzeigen? (j,n): ")

    print("\n")
    if auswertung_anzeigen == "j":
        logic.auswertung(fragen_liste)
    # else:
    #     exit()


if __name__ == "__main__":
    start()

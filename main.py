import logic
import questionModel
# hauptfile


# Einstiegspunkt
def start():
    color = questionModel.BColors()
    fragen_liste = questionModel.fragen_liste

    fragen_liste = logic.fragen_stellen(fragen_liste)

    anzahl_richtig = logic.zaehle_richtige_antworten(fragen_liste)

    print("\n")
    if anzahl_richtig < 60:
        print(color.FAIL + "Du hast " + str(anzahl_richtig) + " % von 20 Fragen richtig beantwortet. Das reicht leider nicht" + color.ENDC)
    else:
        print(color.OKCYAN + "Du hast " + str(anzahl_richtig) + " % von 20 Fragen richtig beantwortet. Hezlichen Glückwunsch du hast bestanden" + color.ENDC)
    print("\n")

    auswertung_anzeigen = input("Auswertung anzeigen? (j,n): ")

    print("\n")
    if auswertung_anzeigen.lower() == "j":
        for index, frage in enumerate(fragen_liste):
            logic.auswertung(index, frage)


if __name__ == "__main__":
    start()


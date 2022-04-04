import logic
import questionModel
# hauptfile


# Einstiegspunkt
def start():
    color = questionModel.BColors()

    fragen_liste = questionModel.fragen_liste

    logic.fragen_stellen(fragen_liste)

    anzahl_richtig = logic.zaehle_richtige_antworten(fragen_liste)

    print("\n")
    print(f"Herzlichen Glückwunsch, du hast " +
          anzahl_richtig + f"von 20 richtig beantwortet")
    print("\n")

    auswertung_anzeigen = input("Auswertung anzeigen? (j,n): ")

    print("\n")
    if auswertung_anzeigen.lower() == "j":
        logic.auswertung(fragen_liste)


if __name__ == "__main__":
    start()


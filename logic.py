import questionModel
import os
import random

# DIESE FUNKTION ÖFFNET DAS JSON FILE MIT FRAGEN UND ERSTELLT FÜR
# JEDE FRAGE EIN QUESTIONMODEL UND GIBT EINE LISTE MIT QUESTIONMODEL ZURÜCK


def eingabe_validieren(details: questionModel.Questions):
    antworten = details.user_antworten.split(",")
    for antwort in antworten:
        if antwort.strip() not in details.korrekte_antworten:
            return False
    if len(antworten) == len(details.korrekte_antworten):
        return True
    else:
        return False


# DIESE FUNKTION GIBT FÜR JEDES QUESTIONMODEL IN DER LISTE DIE FRAGE + ANTWORTMGLKEITEN
# IN DER CONSOLE AUS UND FÜGT DEM QUESTIONMODEL DIE ANTWORT VOM USER HINZU
def fragen_stellen(fragen_liste):
    print("Fahrschulfragen")
    colors = questionModel.BColors()

    for fragen_nummer in range(len(fragen_liste)):
        aktuelle_frage: questionModel.Questions = fragen_liste[fragen_nummer]
        # frage + antwortMöglichkeiten in der Konsole ausgeben
        print(colors.UNDERLINE + aktuelle_frage.frage + colors.ENDC)
        
        for buchstabe, mgl in aktuelle_frage.antwort_mgl.items():
            print(f"{buchstabe}: {mgl}")

        print("\n")

        # überprüfung ob antwort = a b c oder d
        while True:
            antworten = input("Wähle die korrekte Antwort: ").replace(" ", "")

            korrekt = True

            antwort_liste = antworten.split(",")
            for antwort in antwort_liste:
                if antwort not in aktuelle_frage.antwort_mgl.keys():
                    korrekt = False
                    
            if korrekt:
                break
            else:
                print("\n")
                print("Bitte wähle eine valide Antwortmöglichkeit (bei mehreren antworten mit komma trennen)")

        # doppelte werte entfernen + sortieren
        formatierte_antworten =  list(set(antwort_liste))
        formatierte_antworten.sort()

        # jetzt user antwort ins model hinzufügen
        fragen_liste[fragen_nummer].user_antworten = formatierte_antworten

        print("\n")

    # fragenliste(mit userantwort hinzugefügt) zurückgeben
    return fragen_liste


# DIESE FUNKTION ÜBERPRÜFT WIEVIELE FRAGEN RICHTIG BEANTWORTET WURDEN
def zaehle_richtige_antworten(fragen_liste):
    # anzahl richtig beantwortete
    counter = 0
    for frage in fragen_liste:
        # wenn antwort richtig ist counter +1
        if frage.korrekte_antworten == frage.user_antworten:
            counter += 1

    # prozent ausrechnen
    richtig_in_prozent = counter / 20 * 100

    # dann counter (anzahl korrekte Antworten) zurückgeben (als str für Konsolenausgabe)
    return int(richtig_in_prozent)


# NOCHMAL ALLE FRAGEN DURCHGEHEN, UND DIE FRAGE + ANTWORTMGL + RICHTIGE ANTOWRT + EIGENE ANTOWRT
# + ERKLÄRUNG (WENN VORHANDEN) AUSGEBEN
def auswertung(index, frage):
    colors = questionModel.BColors()

    print("\n")
    # prüfen ob antorten richtig sind
    if frage.korrekte_antworten == frage.user_antworten:
        print(colors.OKGREEN + "Frage " + str(index + 1) + ": " + frage.frage + " - Richtig" + colors.ENDC)
    else:
        print(colors.FAIL + "Frage " + str(index + 1) + ": " + frage.frage + " - Falsch" + colors.ENDC)

    print("\n")

    # durch antwortmgl gehen
    for ant_mgl in frage.antwort_mgl:
        # wenn mglkeit richtig und von nutzer gewählt
        if ant_mgl in frage.user_antworten and ant_mgl in frage.korrekte_antworten:
            print(colors.OKGREEN + " (✓) " + frage.antwort_mgl[ant_mgl] + colors.ENDC)
        # wenn mglkeit falsch und von nutzer gewählt
        elif ant_mgl in frage.user_antworten:
            print(colors.WARNING + " (X) " + frage.antwort_mgl[ant_mgl] + colors.ENDC)
        # wenn mglkeit richtig aber nicht von nutzer gewählt
        elif ant_mgl in frage.korrekte_antworten:
            print(colors.OKGREEN + " (X) " + frage.antwort_mgl[ant_mgl] + colors.ENDC)
        # wenn mgl falsch und nicht gewählt
        else:
            print(" (X) " + frage.antwort_mgl[ant_mgl])

    # Wenn Erklärung dabei ist dann gib Erklärung auch aus
    if frage.erklaerung != "":
        print(colors.OKBLUE + "Erklärung: " + frage.erklaerung + colors.ENDC)
    print("\n")

    # os.system('pause')  # test on windows


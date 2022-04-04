import questionModel
import json
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
        print("a: " + aktuelle_frage.antwort_mgl[0])
        print("b: " + aktuelle_frage.antwort_mgl[1])
        print("c: " + aktuelle_frage.antwort_mgl[2])

        if len(aktuelle_frage.antwort_mgl) == 3:
            moegliche_antworten = ["a", "b", "c"]
        else:
            moegliche_antworten = ["a", "b", "c", "d"]
            print("d: " + aktuelle_frage.antwort_mgl[3])

        print("\n")

        # überprüfung ob antwort = a b c oder d
        while True:
            antwort = input("Wähle die korrekte Antwort: ").replace(" ", "")

            antwort_liste = antwort.split(",")
            for antwort in antwort_liste:
                if antwort not in moegliche_antworten:
                    print(
                        "Bitte wähle eine valide Antwortmöglichkeit (bei mehreren antworten mit komma trennen)")
                    continue
            break

        # jetzt user antwort ins model hinzufügen
        aktuelle_frage.user_answer = antwort_liste

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
def auswertung(fragen_liste: list[questionModel.Questions]):
    colors = questionModel.BColors()

    print("_______________________________________________________________________________")
    print("\n")

    for frage in fragen_liste:
        print("Frage: " + colors.UNDERLINE + frage.frage + colors.ENDC)
        # Wenn richtig beantwortet
        if frage.korrekte_antworten == frage.user_antworten:
            print(
                f"{colors.OKGREEN}Korrekt brantwortet (Korrekte Antwort: {frage.correct_answer}){colors.ENDC}")
        # wenn falsch beantwortet
        else:
            print(
                f"{colors.FAIL}Leider falsch (Korrekte Antwort: {frage.correct_answer}){colors.ENDC}")
            print("Deine Antwort war: " + frage.user_answer)

        # Wenn Erklärung dabei ist dann gib Erklärung auch aus
        if frage.erklaerung != "":
            print(f"{colors.OKBLUE}Erklärung: {frage.erklaerung}{colors.ENDC}")
        print("\n")

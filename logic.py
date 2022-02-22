import questionModel

# DIESE FUNKTION GIBT FÜR JEDES QUESTIONMODEL IN DER LISTE DIE FRAGE + ANTWORTMGLKEITEN
# IN DER CONSOLE AUS UND FÜGT DEM QUESTIONMODEL DIE ANTWORT VOM USER HINZU
def fragen_stellen(fragen_liste):
    print("Fahrschulfragen")
    colors = questionModel.BColors()

    for aktuelle_frage in fragen_liste:
        print("\n")
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

        #print("\n")

        # überprüfung ob antwort = a b c oder d

        antwort_nicht_valide = True

        antwort_liste = []

        while antwort_nicht_valide:
            antwort = input("Wähle die korrekte Antwort: ").replace(" ", "")

            antwort_liste = antwort.split(",")

            antwort_nicht_valide = False

            for buchstabe in antwort_liste:
                if buchstabe not in moegliche_antworten:
                    print("Bitte wähle eine valide Antwortmöglichkeit (bei mehreren antworten mit komma trennen)")
                    antwort_nicht_valide = True


        # jetzt user antwort ins model hinzufügen
        aktuelle_frage.user_antworten = antwort_liste

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
def auswertung(frage):
    colors = questionModel.BColors()

    antwort_schluessel = {0: "a", 1: "b", 2: "c", 3: "d"}

    print("\n")
    if frage.korrekte_antworten == list(set(frage.user_antworten)):
        print(colors.OKGREEN + "Frage: " + frage.frage + " - Richtig" + colors.ENDC)
    else:
        print(colors.FAIL + "Frage: " + frage.frage + " - Falsch" + colors.ENDC)

    print("\n")

    for ant_index in range(len(frage.antwort_mgl)):
        if antwort_schluessel[ant_index] in frage.user_antworten and antwort_schluessel[ant_index] in frage.korrekte_antworten:
            print(colors.OKGREEN + colors.UNDERLINE + frage.antwort_mgl[ant_index] + colors.ENDC)
        elif antwort_schluessel[ant_index] in frage.user_antworten:
            print(colors.UNDERLINE + frage.antwort_mgl[ant_index] + colors.ENDC)
        elif antwort_schluessel[ant_index] in frage.korrekte_antworten:
            print(colors.OKGREEN + frage.antwort_mgl[ant_index] + colors.ENDC)
        else:
            print(frage.antwort_mgl[ant_index])

    # Wenn Erklärung dabei ist dann gib Erklärung auch aus
    if frage.erklaerung != "":
        print(colors.OKBLUE + "Erklärung: " + frage.erklaerung + colors.ENDC)
    print("\n")

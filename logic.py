import questionModel
import json

moegliche_antworten = ["a", "b", "c", "d"]


def fragen_einlesen():

    # öffne json datei mit fragen im lesemodus
    with open("questions.json", "r") as file:
        # jsonliste lesen und in var fragen speichern
        fragen = json.load(file)["questions"]
        fragen_model_liste = []

        # durch liste loopen
        for frage in fragen:
            frage_model = questionModel.Questions(
                question=frage["question"],
                correct_answer=frage["correct_answer"],
                explanation=frage["explanation"],
                answer_options=frage["answer_options"],
                # später erst setzen
                user_answer=""
            )

            # model zur list hinzufügen
            fragen_model_liste.append(frage_model)

        # fragen model list zurückgeben
        return fragen_model_liste


def frage_stellen(fragen_liste):
    print("Fahrschulfragen")
    print("Test antowrt immer b")

    for fragen_nummer in range(10):
        aktuelle_frage = fragen_liste[fragen_nummer]
        # frage + antwortMöglichkeiten in der Konsole ausgeben
        print(aktuelle_frage.question)
        print("a: " + aktuelle_frage.answer_options[0])
        print("b: " + aktuelle_frage.answer_options[1])
        print("c: " + aktuelle_frage.answer_options[2])
        print("d: " + aktuelle_frage.answer_options[3])
        print("\n")

        antwort = input("Wähle die korrekte Antwort: ")

        # überprüfung ob antwort = a b c oder d
        while True:
            # wenn ja loop abbrechen
            if antwort in moegliche_antworten:
                break
            # wenn nein : nochmal fragen
            else:
                antwort = input("Bitte wähle a, b, c oder d: ")

        aktuelle_frage.user_answer = antwort

    return fragen_liste


def zaehle_richtige_antworten(fragen_liste: list[questionModel]):
    # anzahl richtig beantwortete
    counter = 0
    for frage in fragen_liste:
        # wenn antwort richtig ist counter 1 hoch setzen
        if frage.correct_answer == frage.user_answer:
            counter += 1

    return str(counter)


def auswertung(fragen_liste):
    print("\n")
    print("_______________________________________________________________________________")
    print("\n")
    for frage in fragen_liste:

        if frage.correct_answer == frage.user_answer:
            print("Korrekt brantwortet (Korrekte Antwort: " + frage.correct_answer + ")")
        else:
            print("Leider falsch (Korrekte Antwort: " + frage.correct_answer + ")")
            print("Deine Antwort war: " + frage.user_answer)

        print(frage.question)
        print("a: " + frage.answer_options[0])
        print("b: " + frage.answer_options[1])
        print("c: " + frage.answer_options[2])
        print("d: " + frage.answer_options[3])
        if frage.explanation != "":
            print("Erklärung: " + frage.explanation)
        print("\n")































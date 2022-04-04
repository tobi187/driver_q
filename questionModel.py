# models

class Questions:
    def __init__(self, frage, antwort_mgl, korrekte_antworten, user_antworten, erklaerung):
        self.frage = frage  # frage
        self.antwort_mgl = antwort_mgl  # liste mit 4 Antwortmöglichkeiten
        self.korrekte_antworten = korrekte_antworten  # a,b,c oder d
        self.erklaerung = erklaerung  # entweder leerer text oder Erklärung
        # Erst leer lassen und später die Antwort vom User eintragen
        self.user_antworten = user_antworten  # a,b,c oder d
        # self.speziell = speziell # true, false


# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


fragen_liste = [
    Questions(
        frage="Warum müssen Sie die Geschwindigkeit anpassen, wenn Sie abblenden?",
        antwort_mgl={"a": "Weil ich sonst Personen oder Gegenstände auf der Fahrbahn zu spät sehen würde",
                     "b": "Weil ich sonst nicht mehr innerhalb der Sichtweite anhalten kann",
                     "c": "Weil ich sonst den Gegenverkehr nicht rechtzeitig erkennen kann",
                     "d": "Weil sich damit die Reaktionszeit verkürzt",
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren mit etwa 80 km/h mit Fernlicht. Wann blenden Sie ab?",
        antwort_mgl={"a": "Sobald ich den Gegenverkehr kommen sehe",
                     "b": "Wenn der Gegenverkehr auf meiner Höhe ist",
                     "c": "Wenn der Gegenverkehr sein Fernlicht abblendet",
                     "d": "Sobald ich mich durch den Gegenverkehr geblendet fühle",
        },
        korrekte_antworten=["c", "d"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie beladen ein Fahrzeug. Darf die Ladung vorne hinausragen?",
        antwort_mgl={"a": "Ja, aber nicht mehr als 1/4 der Fahrzeuglänge ",
                     "b": "Nein",
                     "c": "Ja, aber nicht mehr als 1m",
                     "d": "Ja, unbegrenzt",
        },
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Warum müssen Sie Ihr Fahrzeug bei winterlichen Fahrbahnverhältnissen mit Winterreifen ausstatten?",
        antwort_mgl={"a": "Weil das Fahrzeug beim Bremsen auf einer Schneefahrbahn dadurch nicht so leicht ins Schleudern kommt",
                     "b": "Weil die Bodenhaftung auf einer Schneefahrbahn dadurch besser ist",
                     "c": "Weil dadurch der Treibstoffverbrauch reduziert wird",
                     "d": "Weil Schneeketten nur auf Winterreifen montiert werden dürfen",
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Was kann in Kurven zum Schleudern führen? ",
        antwort_mgl={"a": "Defekte Stoßdämpfer",
                     "b": "Zu niedriger oder stark unterschiedlicher Reifendruck",
                     "c": "Zu geringe Beladung ",
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wozu führt das Hören von lauter Musik, vor allem mit extremen Bässen im Auto?",
        antwort_mgl={"a": "Die Aufmerksamkeit des Fahrers wird erheblich beeinträchtigt ",
                     "b": "Blinde erkennen dadurch leichter den Verlauf der Fahrbahn",
                     "c": "In der Nähe solcher Fahrzeuge verlieren Blinde die Orientierung"
        },
        korrekte_antworten=["a", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Mit welchem Verhalten von Kindern müssen Sie an Zebrastreifen rechnen?",
        antwort_mgl={"a": "Sie kehren ohne erkennbaren Grund auf dem Zebrastreifen um und laufen zurück",
                     "b": "Sie schätzen Geschwindigkeiten und Entfernungen herannahender Fahrzeuge immer richtig ein und warten am Fahrbahnrand",
                     "c": "Sie laufen auf den Zebrastreifen, ohne auf den Verkehr zu achten",
        },
        korrekte_antworten=["a", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="In einem Wohngebiet rollt ein Ball vor ihr Fahrzeug. Wie müssen Sie reagieren?",
        antwort_mgl={"a": "Bremsen",
                     "b": "Weiterfahren",
                     "c": "Ausweichen",
        },
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wodurch kann die Fahrtüchtigkeit herabgesetzt werden?",
        antwort_mgl={"a": "Durch Alkohol und andere berauschende Mittel",
                     "b": "Durch Übermüdung",
                     "c": "Durch bestimmte Medikamente"
        },
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wie verhalten Sie sich beim Anfahren vom Fahrbahnrand?",
        antwort_mgl={"a": "Rückwärtigen Verkehr beobachten",
                     "b": "Blinken",
                     "c": "Blick in den Rückspiegel genügt"
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Worauf müssen Sie achten, wenn Sie in eine Tiefgarage fahren?",
        antwort_mgl={"a": "Fußgänger laufen oft auf Fahrwegen",
                     "b": "Meine Reifen können an engen Aus- und Einfahren beschädigt werden",
                     "c": "Meine Augen müssen sich erst an die veränderten Lichtverhältnisse gewöhnen"
        },
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wo ist das Überholen verboten?",
        antwort_mgl={"a": "Wo der Gegenverkehr behindert werden könnte",
                     "b": "Wo die Verkehrslage unklar ist",
                     "c": "In allen Einbahnstraßen"
                     },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wann müssen Sie vor einem Bahnübergang warten?",
        antwort_mgl={"a": "Wenn ein rotes Blinklicht aufleuchtet",
                     "b": "Wenn ein Bahnbediensteter eine weiß - rot - weiße Fahne schwenkt",
                     "c": "Wenn sich die Schranken senken",
        },
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="An welchen Stellen ohne vorfahrtregelnde Verkehrszeichen gilt die Regen „rechts vor links“?",
        antwort_mgl={"a": "Am Ende eines verkehrsberuhigten Bereiches",
                     "b": "Ab Grundstücksausfahren",
                     "c": "An Straßenkreuzungen und -Einmündungen",
        },
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Was können Sie tun, um die Umwelt zu schonen?",
        antwort_mgl={"a": "Fahren mit Vollgas",
                     "b": "Fahren in überfüllte Innenstädte",
                     "c": "Kurzstreckenfahrten"
        },
        korrekte_antworten=[],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren 50 km/h, haben 1 Sekunde Reaktionszeit und führen eine normale Bremsung durch.\nWie lang ist der Anhalteweg nach der Faustregel?",
        antwort_mgl={"a": "20m",
                     "b": "25m",
                     "c": "40m",
                     "d": "50m",
        },
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung="""Der Anhalteweg bei normaler Bremsung setzt sich zusammen aus der Addition von
Reaktionsweg ((Geschwindigkeit: 10) x3) und Bremsweg (Geschwindigkeit: 10) x
(Geschwindigkeit: 10). Anhalteweg = Reaktionsweg + Bremsweg. Das heißt bei einer
Geschwindigkeit von 50 km/h beträgt der Anhalteweg 40 Meter. """
    ),
    Questions(
        frage="Wegen einer technischen Änderungen an Ihrem Fahrzeug ist eine Begutachtung erfolgt. Wozu sind Sie verpflichtet?\nIch muss das Gutachten oder die Bestätigung…",
        antwort_mgl={"a": "mitführen und gegebenenfalls die Zulassungsbescheinigung Teil 1 berichtigen lassen",
                     "b": "dem Fahrzeughersteller übersenden",
                     "c": "an der dafür vorgesehenen Stelle in der Zulassungsbescheinigung Teil 2 einkleben"
        },
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren 100 km/h und haben 1 Sekunde Reaktionszeit. Wie lange ist der Reaktionsweg nach der Faustformel?",
        antwort_mgl={"a": "10m",
                     "b": "20m",
                     "c": "30m",
                     "d": "40m",
        },
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung="Reaktionsweg = (Geschwindigkeit: 10) x 3. Das heißt bei einer Geschwindigkeit\nvon 100 km/hbeträgt der Bremsweg 30 Meter"
    ),
    Questions(
        frage="Auf welchen Straßen gilt die Richtgeschwindigkeit von 130 km/h?",
        antwort_mgl={"a": "Auf Kraftfahrstraßen außerhalb geschlossener Ortschaften mit baulich getrennten Fahrbahnen für jede Richtung",
                     "b": "Auf Kraftfahrstraßen außerhalb geschlossener Ortschaften mit mindestens zwei markierten Fahrstreifen für jede Richtung",
                     "c": "Auf Autobahnen"
        },
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wozu kann eine plötzliche Verschlechterung des Fahrbahnzustandes führen?",
        antwort_mgl={"a": "Zu Schleuder- und Rutschgefahr",
                     "b": "Zu veränderten Reifengeräuschen",
                     "c": "Zu längerem Reaktionsweg"
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    )

]


fragen_liste_liste = [
    Questions(
        frage="Warum müssen Sie die Geschwindigkeit anpassen, wenn Sie abblenden?",
        antwort_mgl={"a": "Weil ich sonst Personen oder Gegenstände auf der Fahrbahn zu spät sehen würde",
                     "b": "Weil ich sonst nicht mehr innerhalb der Sichtweite anhalten kann",
                     "c": "Weil ich sonst den Gegenverkehr nicht rechtzeitig erkennen kann",
                     "d": "Weil sich damit die Reaktionszeit verkürzt"
        },
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren mit etwa 80 km/h mit Fernlicht. Wann blenden Sie ab?",
        antwort_mgl={"a": "Sobald ich den Gegenverkehr kommen sehe",
                     "b": "Wenn der Gegenverkehr auf meiner Höhe ist",
                     "c": "Wenn der Gegenverkehr sein Fernlicht abblendet",
                     "d": "Sobald ich mich durch den Gegenverkehr geblendet fühle"
        },
        korrekte_antworten=["c", "d"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie beladen ein Fahrzeug. Darf die Ladung vorne hinausragen?",
        antwort_mgl={"a": "Ja, aber nicht mehr als 1/4 der Fahrzeuglänge ",
                     "b": "Nein",
                     "c": "Ja, aber nicht mehr als 1m",
                     "d": "Ja, unbegrenzt"
        },
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Warum müssen Sie Ihr Fahrzeug bei winterlichen Fahrbahnverhältnissen mit Winterreifen ausstatten?",
        antwort_mgl=["Weil das Fahrzeug beim Bremsen auf einer Schneefahrbahn dadurch nicht so leicht ins Schleudern kommt",
                     "Weil die Bodenhaftung auf einer Schneefahrbahn dadurch besser ist",
                     "Weil dadurch der Treibstoffverbrauch reduziert wird",
                     "Weil Schneeketten nur auf Winterreifen montiert werden dürfen",
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Was kann in Kurven zum Schleudern führen? ",
        antwort_mgl=["Defekte Stoßdämpfer",
                     "Zu niedriger oder stark unterschiedlicher Reifendruck",
                     "Zu geringe Beladung ",
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wozu führt das Hören von lauter Musik, vor allem mit extremen Bässen im Auto?",
        antwort_mgl=["Die Aufmerksamkeit des Fahrers wird erheblich beeinträchtigt ",
                     "Blinde erkennen dadurch leichter den Verlauf der Fahrbahn",
                     "In der Nähe solcher Fahrzeuge verlieren Blinde die Orientierung"
                     ],
        korrekte_antworten=["a", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Mit welchem Verhalten von Kindern müssen Sie an Zebrastreifen rechnen?",
        antwort_mgl=["Sie kehren ohne erkennbaren Grund auf dem Zebrastreifen um und laufen zurück",
                     "Sie schätzen Geschwindigkeiten und Entfernungen herannahender Fahrzeuge immer richtig ein und warten am Fahrbahnrand",
                     "Sie laufen auf den Zebrastreifen, ohne auf den Verkehr zu achten",
                     ],
        korrekte_antworten=["a", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="In einem Wohngebiet rollt ein Ball vor ihr Fahrzeug. Wie müssen Sie reagieren?",
        antwort_mgl=["Bremsen",
                     "Weiterfahren",
                     "Ausweichen",
                     ],
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wodurch kann die Fahrtüchtigkeit herabgesetzt werden?",
        antwort_mgl=["Durch Alkohol und andere berauschende Mittel",
                     " Durch Übermüdung",
                     "Durch bestimmte Medikamente"
                     ],
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wie verhalten Sie sich beim Anfahren vom Fahrbahnrand?",
        antwort_mgl=["Rückwärtigen Verkehr beobachten",
                     "Blinken",
                     "Blick in den Rückspiegel genügt"
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Worauf müssen Sie achten, wenn Sie in eine Tiefgarage fahren?",
        antwort_mgl=["Fußgänger laufen oft auf Fahrwegen",
                     "Meine Reifen können an engen Aus- und Einfahren beschädigt werden",
                     "Meine Augen müssen sich erst an die veränderten Lichtverhältnisse gewöhnen"
                     ],
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wo ist das Überholen verboten?",
        antwort_mgl=["Wo der Gegenverkehr behindert werden könnte",
                     "Wo die Verkehrslage unklar ist",
                     "In allen Einbahnstraßen"
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wann müssen Sie vor einem Bahnübergang warten?",
        antwort_mgl=["Wenn ein rotes Blinklicht aufleuchtet",
                     "Wenn ein Bahnbediensteter eine weiß - rot - weiße Fahne schwenkt",
                     "Wenn sich die Schranken senken",
                     ],
        korrekte_antworten=["a", "b", "c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="An welchen Stellen ohne vorfahrtregelnde Verkehrszeichen gilt die Regen „rechts vor links“?",
        antwort_mgl=["Am Ende eines verkehrsberuhigten Bereiches",
                     "Ab Grundstücksausfahren",
                     "An Straßenkreuzungen und -Einmündungen",
                     ],
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Was können Sie tun, um die Umwelt zu schonen?",
        antwort_mgl=[" Fahren mit Vollgas",
                     "Fahren in überfüllte Innenstädte",
                     "Kurzstreckenfahrten"
                     ],
        korrekte_antworten=[],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren 50 km/h, haben 1 Sekunde Reaktionszeit und führen eine normale Bremsung durch.\nWie lang ist der Anhalteweg nach der Faustregel?",
        antwort_mgl=["20m",
                     "25m",
                     "40m",
                     "50m",
                     ],
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung="""Der Anhalteweg bei normaler Bremsung setzt sich zusammen aus der Addition von
Reaktionsweg ((Geschwindigkeit: 10) x3) und Bremsweg (Geschwindigkeit: 10) x
(Geschwindigkeit: 10). Anhalteweg = Reaktionsweg + Bremsweg. Das heißt bei einer
Geschwindigkeit von 50 km/h beträgt der Anhalteweg 40 Meter. """
    ),
    Questions(
        frage="Wegen einer technischen Änderungen an Ihrem Fahrzeug ist eine Begutachtung erfolgt. Wozu sind Sie verpflichtet?\nIch muss das Gutachten oder die Bestätigung…",
        antwort_mgl=["mitführen und gegebenenfalls die Zulassungsbescheinigung Teil 1 berichtigen lassen",
                     "dem Fahrzeughersteller übersenden",
                     "an der dafür vorgesehenen Stelle in der Zulassungsbescheinigung Teil 2 einkleben"
                     ],
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren 100 km/h und haben 1 Sekunde Reaktionszeit. Wie lange ist der Reaktionsweg nach der Faustformel?",
        antwort_mgl=["10m",
                     "20m",
                     "30m",
                     "40m",
                     ],
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung="Reaktionsweg = (Geschwindigkeit: 10) x 3. Das heißt bei einer Geschwindigkeit\nvon 100 km/hbeträgt der Bremsweg 30 Meter"
    ),
    Questions(
        frage="Auf welchen Straßen gilt die Richtgeschwindigkeit von 130 km/h?",
        antwort_mgl=["Auf Kraftfahrstraßen außerhalb geschlossener Ortschaften mit baulich getrennten Fahrbahnen für jede Richtung",
                     "Auf Kraftfahrstraßen außerhalb geschlossener Ortschaften mit mindestens zwei markierten Fahrstreifen für jede Richtung",
                     "Auf Autobahnen"
                     ],
        korrekte_antworten=["c"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Wozu kann eine plötzliche Verschlechterung des Fahrbahnzustandes führen?",
        antwort_mgl=["Zu Schleuder- und Rutschgefahr",
                     "Zu veränderten Reifengeräuschen",
                     "Zu längerem Reaktionsweg"
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    )

]
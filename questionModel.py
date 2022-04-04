# models

class Questions:
    def __init__(self, frage, antwort_mgl, korrekte_antworten, user_antworten, erklaerung) -> None:
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
        antwort_mgl=["Weil ich sonst Personen oder Gegenstände auf der Fahrbahn zu spät sehen würde",
                     "Weil ich sonst nicht mehr innerhalb der Sichtweite anhalten kann",
                     "Weil ich sonst den Gegenverkehr nicht rechtzeitig erkennen kann",
                     "Weil sich damit die Reaktionszeit verkürzt",
                     ],
        korrekte_antworten=["a", "b"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie fahren mit etwa 80 km/h mit Fernlicht. Wann blenden Sie ab?",
        antwort_mgl=["Sobald ich den Gegenverkehr kommen sehe",
                     "Wenn der Gegenverkehr auf meiner Höhe ist",
                     "Wenn der Gegenverkehr sein Fernlicht abblendet",
                     "Sobald ich mich durch den Gegenverkehr geblendet fühle",
                     ],
        korrekte_antworten=["c", "d"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Sie beladen ein Fahrzeug. Darf die Ladung vorne hinausragen?",
        antwort_mgl=["Ja, aber nicht mehr als 1/4 der Fahrzeuglänge ",
                     "Nein",
                     "Ja, aber nicht mehr als 1m",
                     "Ja, unbegrenzt",
                     ],
        korrekte_antworten=["a"],
        user_antworten=[],
        erklaerung=""
    ),
    Questions(
        frage="Warum müssen Sie Ihr Fahrzeug bei winterlichen Fahrbahnverhältnissen mit Winterreifen ausstatten?",
        antwort_mgl=["Weil das Fahrzeug beim Bremsen auf einer Schneefahrbahn dadurch nicht so leicht ins Schleudern kommt",
                     "Weil die Bodenhaftung auf einer Schneefahrbahn dadurch besser ist",
                     " Weil dadurch der Treibstoffverbrauch reduziert wird",
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
        antwort_mgl=[" Sie kehren ohne erkennbaren Grund auf dem Zebrastreifen um und laufen zurück",
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
                     " Auf Kraftfahrstraßen außerhalb geschlossener Ortschaften mit mindestens zwei markierten Fahrstreifen für jede Richtung",
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

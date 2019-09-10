import random

# Markierungen für die Türen
KEIN_PREIS = 'k'
PREIS = 'p'
WEGGEWORFENER_TUER = 'w'


def zufaellige(tueren):
    """
    Erzeugt eine zufällige Position für die angegebenen Türen

    :param tueren: Die Türen
    :return: Türposition
    """
    return random.randint(0, len(tueren) - 1)


def tueren_generieren(anzahl_der_tueren):
    """
    Erzeugt die Türen mit einer als Preis gekennzeichneten Tür

    :param anzahl_der_tueren: Anzahl der Türen
    :return: Die Türen
    """
    tueren = [KEIN_PREIS] * anzahl_der_tueren
    tueren[zufaellige(tueren)] = PREIS
    return tueren


def tuer_ablegen(tueren, gewaehlte_tuer):
    """
    Markiert ine Tür als weg in den gegebenen Türen

    :param tueren: Die Tüuren
    :param gewaehlte_tuer: Gewählte Tür
    :return: Die Türen mit einer, die als weg markiert ist
    """
    while True:
        kandidat = zufaellige(tueren)
        if kandidat != gewaehlte_tuer and tueren[kandidat] is KEIN_PREIS:
            tueren[kandidat] = WEGGEWORFENER_TUER
            return tueren


def tuer_wechseln(tueren, gewaehlte_tuer):
    """
    Ändert die gewählte Tür

    :param tueren: Die Türen
    :param gewaehlte_tuer: Die aktuell gewählte Tür
    :return: Neue gewählte Tür
    """
    while True:
        kandidat = zufaellige(tueren)
        if kandidat != gewaehlte_tuer and tueren[kandidat] is not WEGGEWORFENER_TUER:
            return kandidat


def simulieren(anzahl_der_tueren, iterationen, wechsler):
    """
    Führt die Simulation aus

    :param anzahl_der_tueren: Anzahl der Türen
    :param iterationen: Iterationen
    :param wechsler: Flagge: Ist er ein Wechsler oder nicht?
    :return:
    """

    gewinne = 0
    for i in range(iterationen):
        tueren = tueren_generieren(anzahl_der_tueren)
        gewaelte_tuer = zufaellige(tueren)
        tueren = tuer_ablegen(tueren, gewaelte_tuer)

        if wechsler:
            gewaelte_tuer = tuer_wechseln(tueren, gewaelte_tuer)

        if(tueren[gewaelte_tuer] == PREIS):
            gewinne = gewinne + 1

    wer = 'Ändern' if wechsler else 'Nicht ändern'
    print('{} hat {}% der Zeit gewonnen'.format(wer, gewinne * 100 / iterationen))


if __name__ == '__main__':
    simulieren(3, 10000, False)
    simulieren(3, 10000, True)

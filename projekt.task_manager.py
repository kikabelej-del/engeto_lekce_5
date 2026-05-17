"""
Program pro Projekt: Task manager
Umožňuje přidávat, zobrazovat a odstraňovat úkoly uložené v seznamu.
"""

# Seznam pro ukládání úkolů
ukoly = []


def hlavni_menu():
    """Zobrazí hlavní menu programu."""
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu.")


def zobrazit_ukoly():
    """
    Vypíše všechny úkoly v seznamu s jejich indexem.
    Pokud je seznam prázdný, informuje uživatele a vrátí False.
    Využívá enumerate pro automatické číslování od 1.
    """
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return False

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    return True


def pridat_ukol():
    """
    Požádá uživatele o název a popis úkolu.
    Opakuje výzvu, dokud uživatel nezadá neprázdný vstup.
    """
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if nazev:
            break
        print("Neplatná volba, zkuste to znovu.")

    while True:
        popis = input("Zadejte popis úkolu: ").strip()
        if popis:
            break
        print("Neplatná volba, zkuste to znovu.")

    novy_ukol = {"nazev": nazev, "popis": popis}
    ukoly.append(novy_ukol)
    print(f"Úkol '{nazev}' byl úspěšně přidán.")


def odstranit_ukol():
    """
    Zobrazí úkoly a umožní uživateli jeden úkol smazat podle čísla.
    Obsahuje validaci prázdného seznamu, rozsahu a typu vstupu.
    """
    if not zobrazit_ukoly():
        return

    try:
        index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= index <= len(ukoly):
            odstraneny = ukoly.pop(index - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplatná volba, zkuste to znovu.")
    except ValueError:
        print("Neplatná volba, zkuste to znovu.")


# --- Hlavní smyčka ---
def main():
    """Hlavní funkce pro spuštění celého programu."""
    while True:
        hlavni_menu()
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu (zadejte 1-4).")


if __name__ == "__main__":
    main()

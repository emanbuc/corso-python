def lookup_acronym():
    look_up = input("Enter acronym to look for: ").strip().upper()

    found= False
    print(f"Looking for acronym: {look_up}")

    try:
        with open('acronyms.txt') as file:
            for line in file:
                print(f"Checking line: {line.strip()}")
                if look_up in line:
                    found = True
                    print(f"Acronym found: {line.strip()}")
                    break
        if not found:
            print("Acronym not found.")
    except FileNotFoundError:
        print("Acronyms file not found. Please ensure it exists.")




def add_acronym():
    acronym = input("Enter acronym to add: ").strip().upper()
    definition = input("Enter definition to ADD: ").strip()

    with open('acronyms.txt', 'a') as file:
        file.write(f"{acronym} - {definition}\n")
        print(f"Acronym '{acronym}' with definition '{definition}' added.")

add_acronym()
lookup_acronym()
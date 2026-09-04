telefonbok = {
    "Erik":9036570,
    "Jakob":92134700,
    "Odin":94085636,
    "Sindre":46212614,
    "Eilert":46527597
}

def vis_alle():
    print("Telefonbok: ----------")
    for key,value in telefonbok.items():
        print(f"{key}: {value}")
    print("----------------------")

def legg_til(key,val):
    telefonbok[key] = val
    print(f"Lagt til {key} med nummer {val}")

def søk(navn):
    for key in telefonbok:
        if navn.lower() == key.lower():
            print("Person {key} er i ordboken")
    print("Personen er ikke i ordboken")


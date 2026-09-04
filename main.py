run = True

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

def user_exists(key,val):
    for Key,Item in telefonbok.items():
        if Key.lower() == key.lower():
            if Item == int(val):
                return True
    return False

def legg_til(key,val):
    exists = user_exists(key,val)
    if exists:
        print("Denne personen er allerede i ordboken med samme nummer. \n")
        return
    telefonbok[key] = val
    print(f"Lagt til {key} med nummer {val}")

def søk(navn):
    for key in telefonbok:
        if navn.lower() == key.lower():
            print("Person {key} er i ordboken")
    print("Personen er ikke i ordboken \n")

def handleInput(inpt: str):
    inpt = inpt.lower()
    if inpt == "søk":
        usrInput = input("Skriv inn navnet på personen du vil søke etter: ")
        søk(usrInput)
    elif inpt == "vis":
        vis_alle()
    elif inpt == "legg til ny":
        key = input("Skriv inn navnet på personen du vil legge inn: ")
        value = input("Skriv inn nummeret til personen du vil legge inn: ")
        legg_til(key,value)
    elif inpt == "avslutt":
        print("Avslutter programmet. ")
        run = False
    else:
        print("Kommando ikke gjennkjent. \n")

while run:
    user_input = input("Skriv inn kommando: Søk, Vis, Legg til ny, Avslutt: \n")
    handleInput(user_input)
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

def legg_til(key,val):
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
    if inpt == "vis":
        vis_alle()
    if inpt == "legg til ny":
        key = input("Skriv inn navnet på personen du vil legge inn: ")
        value = input("Skriv inn nummeret til personen du vil legge inn: ")
        legg_til(key,value)
    if inpt == "Avslutt":
        print("Avslutter programmet. ")
        run = False
    else:
        print("Kommando ikke gjennkjent")

while run:
    user_input = input("Skriv inn kommando: Søk, Vis, Legg til ny, Avslutt")
    handleInput(user_input)
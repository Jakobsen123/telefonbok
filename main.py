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


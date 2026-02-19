from pyscript import document

# In-memory storage for registered users
users_db = {}

def assign_team(registered, medical, grade, section):
    if registered != "yes":
        return "Please register online first."
    elif medical != "yes":
        return "Please secure a medical clearance."
    elif grade == 7:
        return f"Congratulations!\nGrade 7 - {section}\nYou are part of the Blue Bears."
    elif grade == 8:
        return f"Congratulations!\nGrade 8 - {section}\nYou are part of the Red Bulldogs."
    elif grade == 9:
        return f"Congratulations!\nGrade 9 - {section}\nYou are part of the Yellow Tigers."
    elif grade == 10:
        return f"Congratulations!\nGrade 10 - {section}\nYou are part of the Green Hornets."
    else:
        return "Invalid grade."

def signup(event):
    user = document.getElementById("username").value
    pwd = document.getElementById("password").value
    grade = int(document.getElementById("grade").value)
    section = document.getElementById("section").value

    if user == "" or pwd == "":
        document.getElementById("msg").innerText = "Please fill in all fields."
        return

    # Save user in memory
    users_db[user] = {"password": pwd, "grade": grade, "section": section}
    document.getElementById("msg").innerText = f"Account created for {user}!"

def checkEligibility(event):
    registered = "no"
    medical = "no"

    if document.getElementById("regYes").checked:
        registered = "yes"
    if document.getElementById("medYes").checked:
        medical = "yes"

    grade = int(document.getElementById("grade").value)
    section = document.getElementById("section").value

    result = assign_team(registered, medical, grade, section)
    document.getElementById("result").innerText = result

def show_players(event):
    players_list = [
        "Abaca",
        "Alavado",
        "Arenal",
        "Aventajado",
        "Buhain",
        "Carpio",
        "Cenon",
        "Cruz",
        "De Leon",
        "De Peralta",
        "Del Barrio",
        "Dida-agun",
        "Dumlao",
        "Estapia",
        "Galope",
        "Galura",
        "Guevarra",
        "Gurango",
        "Lazo",
        "Liwag",
        "Magpantay",
        "Moyaen",
        "Panuncialman",
        "Prowel",
        "Ramos",
        "Sannino",
        "Tecson",
        "Ulit"
    ]

    output = ""
    for name in players_list:
        output += name + "<br>"

    document.getElementById("players").innerHTML = output

from pyscript import document, display

Glee = {
    "title": "Glee Club",
    "desc": "A show choir group focused on vocal performance.",
    "time": "Fridays 2:30 PM to 5:30 PM ",
    "loc": "Music Room 101",
    "advisor": "Mr. De Guzman"
}

Monarch = {
    "title": "The Monarchs",
    "desc": "A club that inspires students to imrove their dancing skills",
    "time": "Mondays 12:00 PM to 3:00 PM",
    "loc": "MMH",
    "advisor": "Mr. Marutani"
}

Volleyball = {
    "title": "Volleyball Varsity",
    "desc": "A club that allows students to train and improve their volleyball skills",
    "time": "Tuesday 3:00 PM to 5:30 PM",
    "loc": "Quadrangle",
    "advisor": "Coach Mark Gervacio"
}

def show_glee(e):
    document.getElementById("output").innerHTML = ""
    
    display(f'{Glee["title"]}', target='output')
    display(f'{Glee["desc"]}', target='output')
    display(f'{Glee["time"]}', target='output')
    display(f'{Glee["loc"]}', target='output')
    display(f'{Glee["advisor"]}', target='output')

def show_monarchs(e):
    document.getElementById("output").innerHTML = ""
    
    display(f'{Monarch["title"]}', target='output')
    display(f'{Monarch["desc"]}', target='output')
    display(f'{Monarch["time"]}', target='output')
    display(f'{Monarch["loc"]}', target='output')
    display(f'{Monarch["advisor"]}', target='output')

def show_volleyball(e):
    document.getElementById("output").innerHTML = ""
    
    display(f'{Volleyball["title"]}', target='output')
    display(f'{Volleyball["desc"]}', target='output')
    display(f'{Volleyball["time"]}', target='output')
    display(f'{Volleyball["loc"]}', target='output')
    display(f'{Volleyball["advisor"]}', target='output')

document.getElementById("Glee").onclick = show_glee
document.getElementById("Monarchs").onclick = show_monarchs
document.getElementById("Volleyball").onclick = show_volleyball
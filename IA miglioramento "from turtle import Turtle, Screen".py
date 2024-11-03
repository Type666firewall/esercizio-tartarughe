from turtle import Turtle, Screen
from random import randint

# Imposta lo schermo e le dimensioni della finestra
screen = Screen()
screen.setup(width=500, height=400)

# Lista dei colori disponibili per le tartarughe
colori = ["red", "green", "purple", "yellow", "blue", "magenta"]
pos_y = [0, -25, -50, 25, 50, 75]

# Richiedi il numero di giocatori
num_giocatori = int(screen.textinput(title="Numero di Giocatori", prompt="Quanti giocatori vogliono scommettere?"))

# Raccogli le scommesse dei giocatori in una lista
scommesse = []
for i in range(num_giocatori):
    puntata = screen.textinput(
        title=f"Scommessa Giocatore {i + 1}",
        prompt=f"Scegli il colore della tartaruga ({', '.join(colori)}):"
    )
    # Verifica che il colore scelto sia valido
    while puntata not in colori:
        puntata = screen.textinput(
            title=f"Scommessa Giocatore {i + 1}",
            prompt=f"Colore non valido. Scegli un colore tra ({', '.join(colori)}):"
        )
    scommesse.append(puntata)

# Creazione delle tartarughe e posizionamento iniziale
turtles = []
for num in range(6):
    t = Turtle(shape="turtle")
    t.color(colori[num])
    t.penup()
    t.goto(x=-240, y=pos_y[num])
    turtles.append(t)

# Iniziamo la gara
start = True
while start:
    for turtle in turtles:
        # Controlla se una tartaruga ha raggiunto o superato il traguardo
        if turtle.xcor() > 230:
            start = False  # Ferma la gara
            winning_color = turtle.pencolor()
            
            # Verifica se qualche giocatore ha scommesso sul colore vincente
            vincitori = [i + 1 for i, puntata in enumerate(scommesse) if puntata == winning_color]
            
            if vincitori:
                print(f"Hai vinto! La tartaruga di colore {winning_color} ha vinto!")
                for vincitore in vincitori:
                    print(f"Giocatore {vincitore} ha indovinato il colore vincente!")
            else:
                print(f"Nessun giocatore ha indovinato. Ha vinto il colore {winning_color}")
            
            break  # Esce dal ciclo `for` per fermare tutte le tartarughe
        # Muove ogni tartaruga in avanti di un valore casuale tra 0 e 10
        turtle.forward(randint(0, 10))

# Attende il clic dell'utente per chiudere la finestra
screen.exitonclick()

#versione gpt4o
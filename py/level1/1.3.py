import tkinter as tk
import random

root = tk.Tk()
root.title("Гра")


canvas_height = 500
canvas_width  = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

player = canvas.create_rectangle(50, canvas_height - 40, 90, canvas_height - 10, fill="blue")

player_speed = 20

def move_left(event):
    canvas.move(player, -player_speed, 0)
    check_collision()

def move_right(event):
    canvas.move(player, player_speed, 0)
    check_collision()

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

bonus = canvas.create_rectangle(random.randint(0, canvas_width - 30), 0, random.randint(30, canvas_width), 30, fill="green")
antibonus = canvas.create_rectangle(random.randint(0, canvas_width - 30), 0, random.randint(30, canvas_width), 30, fill="red")

bonus_speed = 5
antibonus_speed = 5

score = 0
score_text = canvas.create_text(50, 20, text=f"Рахунок: {score}", font=("Arial", 16), fill="black")

def check_collision():
    global score
    player_coords = canvas.coords(player)
    bonus_coords = canvas.coords(bonus)
    antibonus_coords = canvas.coords(antibonus)

    if (player_coords[2] > bonus_coords[0] and player_coords[0] < bonus_coords[2] and
        player_coords[3] > bonus_coords[1] and player_coords[1] < bonus_coords[3]):
        score += 1
        canvas.itemconfig(score_text, text=f"Рахунок: {score}")
        reset_bonus()

    if (player_coords[2] > antibonus_coords[0] and player_coords[0] < antibonus_coords[2] and
        player_coords[3] > antibonus_coords[1] and player_coords[1] < antibonus_coords[3]):
        game_over()

def reset_bonus():
    canvas.coords(bonus, random.randint(0, canvas_width - 30), 0, random.randint(30, canvas_width), 30)

def game_over():
    global score
    txt = canvas.create_text(canvas_width / 2, canvas_height / 2, text="Ви загинули!", font=("Arial", 24), fill="red")
    root.unbind("<Left>")
    root.unbind("<Right>")
    root.after_cancel(update)
    score = 0
    canvas.itemconfig(score_text, text=f"Рахунок: {score}")

    def restart():
        global score
        root.bind("<Left>", move_left)
        root.bind("<Right>", move_right)
        canvas.itemconfig(txt, text="")
    root.after(2000, restart)

def update():
    canvas.move(bonus, 0, bonus_speed)
    canvas.move(antibonus, 0, antibonus_speed)
    if canvas.coords(bonus)[3] > canvas_height:
        reset_bonus()
    if canvas.coords(antibonus)[3] > canvas_height:
        canvas.coords(antibonus, random.randint(0, canvas_width - 30), 0, random.randint(30, canvas_width), 30)
    check_collision()
    root.after(50, update)
root.after(50, update)
update()
root.mainloop()
import tkinter as tk
import tkinter.messagebox as tkm

window=tk.Tk()

window.title("TicTacToe")
window.geometry("300x300")
window.resizable(False,False)

Area=[]
turn=0

def new_game():
    global turn
    global Area
    turn=0
    for x in range(3):
        for y in range(3):
            Area[x][y]["text"]=""


main_menu=tk.Menu(window)
window.configure(menu=main_menu)
file_menu=tk.Menu(main_menu)
main_menu.add_cascade(label="Menu",menu=file_menu)
file_menu.add_command(label="New Game",command=new_game)




def winner():
    if Area[0][0]["text"] == "X" and Area[1][1]["text"] == "X" and Area[2][2]["text"] == "X":
        return "X"
        print("X won!")
    if Area[0][2]["text"] == "X" and Area[1][1]["text"] == "X" and Area[2][0]["text"] == "X":
        return"X"
        print("X won!")

    if Area[0][0]["text"] == "X" and Area[1][0]["text"] == "X" and Area[2][0]["text"] == "X":
        return"X"
        print("X won!")
    if Area[0][1]["text"] == "X" and Area[1][1]["text"] == "X" and Area[2][1]["text"] == "X":
        return"X"
        print("X won!")
    if Area[0][2]["text"] == "X" and Area[1][2]["text"] == "X" and Area[2][2]["text"] == "X":
        return"X"
        print("X won!")

    if Area[0][0]["text"] == "X" and Area[0][1]["text"] == "X" and Area[0][2]["text"] == "X":
        return"X"
        print("X won!")
    if Area[1][0]["text"] == "X" and Area[1][1]["text"] == "X" and Area[1][2]["text"] == "X":
        return"X"
        print("X won!")
    if Area[2][0]["text"] == "X" and Area[2][1]["text"] == "X" and Area[2][2]["text"] == "X":
        return"X"
        print("X won!")




    if Area[0][0]["text"] == "O" and Area[1][1]["text"] == "O" and Area[2][2]["text"] == "O":
        return"O"
        print("O won!")
    if Area[0][2]["text"] == "O" and Area[1][1]["text"] == "O" and Area[2][0]["text"] == "O":
        return"O"
        print("O won!")

    if Area[0][0]["text"] == "O" and Area[1][0]["text"] == "O" and Area[2][0]["text"] == "O":
        return"O"
        print("O won!")
    if Area[0][1]["text"] == "O" and Area[1][1]["text"] == "O" and Area[2][1]["text"] == "O":
        return"O"
        print("O won!")
    if Area[0][2]["text"] == "O" and Area[1][2]["text"] == "O" and Area[2][2]["text"] == "O":
        return"O"
        print("O won!")

    if Area[0][0]["text"] == "O" and Area[0][1]["text"] == "O" and Area[0][2]["text"] == "O":
        return"O"
        print("O won!")
    if Area[1][0]["text"] == "O" and Area[1][1]["text"] == "O" and Area[1][2]["text"] == "O":
        return"O"
        print("O won!")
    if Area[2][0]["text"] == "O" and Area[2][1]["text"] == "O" and Area[2][2]["text"] == "O":
        return"O"
        print("O won!")

    return ""
def push(button):
    global turn
    print(turn)

    if turn %2 == 0:
        turn_char="O"

    else:
        turn_char="X"
    print(f"{turn_char}'s turn!")

    if button["text"]== "":
        button["text"]=turn_char
        turn+=1
    else:
        tkm.showinfo("Busy Place","This place is already taken!Try another one.")

    if winner() == "X":
        print("X Won!")
        tkm.showinfo("Winner","X won!")
        new_game()
    if winner() == "O":
        print("O won!")
        tkm.showinfo("Winner","O won!")
        new_game()
    if winner() == "" and turn == 10:
        print("Tie.")
        tkm.showinfo("Tie","It's a tie so no one won.")
        new_game()

        
       
for x in range(3):
    Area.append([])
    for a in range(3):   
        button=tk.Button(window,text="",width=13,height=6)
        Area[x].append(button)
        Area[x][a].place(x=x*100,y=a*100)
        Area[x][a]["command"]=lambda selected_button = button:push(selected_button)
print(Area)

       

       

window.mainloop()

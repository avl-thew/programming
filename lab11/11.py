import random
import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3

def create_database():
    conn = sqlite3.connect('tictactoe.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS games
                (id INTEGER PRIMARY KEY, player TEXT, result TEXT, date TEXT)''')
    conn.commit()
    conn.close()

create_database()

def save_game_result(player, result):
    try:
        conn = sqlite3.connect('tictactoe.db')
        c = conn.cursor()
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO games (player, result, date) VALUES (?, ?, ?)", (player, result, date))
        conn.commit()
    except Exception as e:
        print(f"Error saving game result: {e}")
    finally:
        conn.close()

class Game:
    def __init__(self):
        self.game_menu = tk.Tk()
        self.game_menu.configure(bg="#232a2f")
        self.game_menu.geometry("250x250")
        self.game_menu.title("Tik Tak Toe")
        title = tk.Label(self.game_menu, text="Tik Tak Toe", background="#232a2f", fg="white")
        singleplayer = tk.Button(self.game_menu, text="Single Player", background="#4e7da5", width=30, height=2, command=lambda: self.play("PC"))
        multiplayer = tk.Button(self.game_menu, text="Multi Player", background="#4e7da5", width=30, height=2, command=lambda: self.play("Human"))
        title.pack(side="top", pady="10px")
        singleplayer.pack(side="top", pady="10px")
        multiplayer.pack(side="top", pady="10px")
        self.current_turn = "X"
        self.board = None

    def is_winner(self, moves=None):
        if moves is None:
            moves = [[self.board[row][col]["text"] for col in range(3)] for row in range(3)]
        for row in range(3):
            if moves[row][0] == moves[row][1] == moves[row][2] != " ":
                return True
        
        for col in range(3):
            if moves[0][col] == moves[1][col] == moves[2][col] != " ":
                return True
        
        if moves[0][0] == moves[1][1] == moves[2][2] != " ":
            return True
        
        if moves[0][2] == moves[1][1] == moves[2][0] != " ":
            return True
        
        return False

    def get_potential_win(self):
        moves = [[self.board[row][col]["text"] for col in range(3)] for row in range(3)]
        for i in range(3):
            for j in range(3):
                if moves[i][j] != " ":
                    continue
                moves[i][j] = "O"
                if self.is_winner(moves=moves):
                    return (i, j)
                moves[i][j] = "X"
                if self.is_winner(moves=moves):
                    return (i, j)
                moves[i][j] = " "
        return None

    def is_board_full(self):
        for row in self.board:
            for button in row:
                if button["text"] == " ":
                    return False
        return True

    def make_a_move_human(self, frame, row, col):
        if self.board[row][col]["text"] == " ":
            self.board[row][col]["text"] = self.current_turn
            self.board[row][col]["state"] = "disabled"

        if self.is_winner():
            messagebox.showinfo("Игра окончена", f"Игрок {self.current_turn} победил!")
            save_game_result("Human" if self.current_turn == "X" else "PC", "Win")
            frame.destroy()
        elif self.is_board_full():
            messagebox.showinfo("Игра окончена", "Ничья!")
            save_game_result("Draw", "Draw")
            frame.destroy()
        else:
            self.current_turn = "O" if self.current_turn == "X" else "X"

    def make_a_move_pc(self, frame, row, col):
        if self.board[row][col]["text"] == " ":
            self.board[row][col]["text"] = self.current_turn
            self.board[row][col]["state"] = "disabled"
        
        if self.is_winner():
            messagebox.showinfo("Игра окончена", f"Компьютер победил!")
            save_game_result("PC", "Win")
            frame.destroy()
            return
        
        if self.is_board_full():
            messagebox.showinfo("Игра окончена", "Ничья!")
            save_game_result("Draw", "Draw")
            frame.destroy()
            return
        
        if self.board[1][1]["text"] == " ":
            self.board[1][1]["text"] = "O"
            self.board[1][1]["state"] = "disabled"
            return
        
        cell = self.get_potential_win()
        if cell:
            self.board[cell[0]][cell[1]]["text"] = "O"
            self.board[cell[0]][cell[1]]["state"] = "disabled"
        else:
            available_moves = []
            for row in range(3):
                for col in range(3):
                    if self.board[row][col]["text"] == " ":
                        available_moves.append((row, col))
            row, col = random.choice(available_moves)
            self.board[row][col]["text"] = "O"
            self.board[row][col]["state"] = "disabled"

    def create_board(self, frame, opponent):
        board = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(frame, text=" ", width=10, height=5)
                if opponent == "PC":
                    button.configure(command=lambda r=row, c=col: self.make_a_move_pc(frame, r, c))
                else:
                    button.configure(command=lambda r=row, c=col: self.make_a_move_human(frame, r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            board.append(button_row)
        self.board = board

    def play(self, opponent):
        self.game_menu.withdraw()
        board_window = tk.Toplevel(self.game_menu)
        board_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(board_window))
        board_window.configure(bg="#232a2f")
        board_window.geometry("290x250")
        board_window.resizable(width=False, height=False)
        board_window.title(f"Tik Tak Toe")
        self.create_board(board_window, opponent)
        board_window.mainloop()

    def start(self):
        self.game_menu.mainloop()

def on_closing(window):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        save_game_result("Draw", "Draw")
        window.destroy()
        game.game_menu.deiconify()

game = Game()
game.start()



import random
import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.game_menu = tk.Tk()
        self.game_menu.configure(bg="#232a2f")
        self.game_menu.geometry("250x250")
        self.game_menu.title("Tik Tak Toe")
        title = tk.Label(self.game_menu, text="Tik Tak Toe", background="#232a2f", fg="white")
        singleplayer = tk.Button(self.game_menu, text="Single Player", background="#4e7da5",
                                width=30, height=2, command=lambda x="PC": self.play(x))
        multiplayer = tk.Button(self.game_menu, text="Multi Player", background="#4e7da5",
                                width=30, height=2, command=lambda x="Human": self.play(x))
        title.pack(side="top", pady="10px")
        singleplayer.pack(side="top", pady="10px")
        multiplayer.pack(side="top", pady="10px")
        self.current_turn = "X"
        self.board: list
    
    def is_winner(self, moves=None):
        if moves == None:
            moves = [[self.board[row][col]["text"] for row in range(3)] for col in range(3)]
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
        moves = [[self.board[row][col]["text"] for row in range(3)] for col in range(3)]
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
            frame.destroy()
        elif self.is_board_full():
            messagebox.showinfo("Игра окончена", "Ничья!")
            frame.destroy()
        else:
            self.current_turn = "O" if self.current_turn == "X" else "X"
    
    def make_a_move_pc(self, frame, row, col):
        if self.board[row][col]["text"] == " ":
            self.board[row][col]["text"] = self.current_turn
            self.board[row][col]["state"] = "disabled"
        
        if self.is_winner():
            frame.withdraw()
            messagebox.showinfo("Игра окончена", f"Игрок победил!")
            frame.destroy()
            return
        
        if self.is_board_full():
            frame.withdraw()
            messagebox.showinfo("Игра окончена", "Ничья!")
            frame.destroy()
            return
        
        if self.board[1][1]["text"] == " ":
            self.board[1][1]["text"] = "O"
            self.board[1][1]["state"] = "disabled"
            return
        
        cell = self.get_potential_win()
        if cell:
            self.board[cell[1]][cell[0]]["text"] = "O"
            self.board[cell[1]][cell[0]]["state"] = "disabled"
        else:
            available_moves = []
            for row in self.board:
                for cell in row:
                    if cell["text"] == " ":
                        available_moves.append(cell)
            cell = random.choice(available_moves)
            cell["text"] = "O"
            cell["state"] = "disabled"
        
        if self.is_winner():          
            frame.withdraw()
            messagebox.showinfo("Игра окончена", f"Компьютер победил!")
            frame.destroy()
            return
    
    def create_board(self, frame, opponent):
        board = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(frame, text=" ", width=10, height=5)
                if opponent == "PC":
                    button.configure(command=lambda f=frame, r=row, c=col: self.make_a_move_pc(f, r, c))
                else:
                    button.configure(command=lambda f=frame, r=row, c=col: self.make_a_move_human(f, r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            board.append(button_row)
        self.board = board
    
    def start(self):
        self.game_menu.mainloop()

    def play(self, opponent):
        print(opponent)
        self.game_menu.withdraw()
        board_window = tk.Tk()
        board_window.bind("<Destroy>", self.game_menu.destroy())
        board_window.configure(bg="#232a2f")
        board_window.geometry("350x290")
        board_window.resizable(width=False, height=False)
        board_window.title(f"Tik Tak Toe")
        if opponent == "PC":
            self.create_board(board_window, "PC")
        else:
            self.create_board(board_window, "Human")
        board_window.mainloop()

if __name__ == "__main__":
    game = Game()
    game.start()
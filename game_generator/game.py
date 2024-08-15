"""
This was my prompt:

Enter your desired game's description: Develop a Tic-Tac-Toe game for two players that maintains the state of Player 1 and Player 2. The cards should be dark gray with borders and box shadows to resemble real cards. When a player clicks on a card, it should display a tick or a cross. The tick should be green, and the cross should be red. Maintain the shape of the cards to ensure easy distinction between them. Additionally, the game should announce the winner and restart automatically after 5 seconds. The game should only stop when the user closes the pop-up window.

The returned code is as follows, and it is error-free. Amazing!:
"""
import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.window, text='', font='Calibri 20 bold', height=3, width=6, 
                               bg='darkgrey', relief='raised', bd=5, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)  # Added padding for better appearance
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].configure(text=self.current_player, disabledforeground=("green" if self.current_player == 'X' else "red"))
            self.buttons[index].config(state='disabled')

            if self.check_winner():
                self.announce_winner()
            elif '' not in self.board:
                self.announce_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def announce_winner(self):
        winner = self.current_player
        messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        self.window.after(5000, self.reset_game)

    def announce_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.window.after(5000, self.reset_game)

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='', state='normal')

if __name__ == "__main__":
    TicTacToe()

import tkinter as tk
import random
import json


class Game2048:
    def __init__(self, size=4, difficulty='normal'):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.score = 0
        self.history = []
        self.difficulty = difficulty
        self.start_game()

    def start_game(self):
        if self.difficulty == 'easy':
            self.add_tile()
        elif self.difficulty == 'hard':
            self.add_tile()
            self.add_tile()
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty_tiles = [(r, c) for r in range(self.size)
                       for c in range(self.size) if self.board[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.board[r][c] = random.choice([2, 4])

    def slide_row_left(self, row):
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        return new_row + [0] * (self.size - len(new_row))

    def move_left(self):
        self.save_state()
        new_board = [self.slide_row_left(row) for row in self.board]
        if new_board != self.board:
            self.board = new_board
            self.add_tile()

    def move_right(self):
        self.save_state()
        self.board = [self.slide_row_left(row[::-1])[::-1]
                      for row in self.board]
        self.add_tile()

    def move_up(self):
        self.save_state()
        self.board = [list(x) for x in zip(*self.board)]
        self.move_left()
        self.board = [list(x) for x in zip(*self.board)]

    def move_down(self):
        self.save_state()
        self.board = [list(x) for x in zip(*self.board)]
        self.move_right()
        self.board = [list(x) for x in zip(*self.board)]

    def save_state(self):
        self.history.append((self.board, self.score))

    def undo(self):
        if self.history:
            self.board, self.score = self.history.pop()

    def is_game_over(self):
        for row in self.board:
            if 0 in row:
                return False
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.board[r][c] == self.board[r][c + 1]:
                    return False
        for r in range(self.size - 1):
            for c in range(self.size):
                if self.board[r][c] == self.board[r + 1][c]:
                    return False
        return True

    def get_high_scores(self):
        try:
            with open('high_scores.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_high_score(self):
        high_scores = self.get_high_scores()
        high_scores.append(self.score)
        high_scores = sorted(high_scores, reverse=True)[:5]
        with open('high_scores.json', 'w') as file:
            json.dump(high_scores, file)


class Game2048GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("2048 Game")
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.score_label = tk.Label(
            self.root, text="Score: 0", font=("Helvetica", 24))
        self.score_label.pack()
        self.cells = [[tk.Label(self.board_frame, text="", width=4, height=2, font=(
            "Helvetica", 24), bg="white") for _ in range(self.game.size)] for _ in range(self.game.size)]
        for r in range(self.game.size):
            for c in range(self.game.size):
                self.cells[r][c].grid(row=r, column=c, padx=5, pady=5)
        self.update_board()
        self.root.bind("<Left>", lambda event: self.handle_move('left'))
        self.root.bind("<Right>", lambda event: self.handle_move('right'))
        self.root.bind("<Up>", lambda event: self.handle_move('up'))
        self.root.bind("<Down>", lambda event: self.handle_move('down'))
        self.root.bind("<u>", lambda event: self.handle_undo())
        self.root.mainloop()

    def update_board(self):
        for r in range(self.game.size):
            for c in range(self.game.size):
                value = self.game.board[r][c]
                self.cells[r][c].config(
                    text=str(value) if value != 0 else "", bg=self.get_tile_color(value))
        self.score_label.config(text=f"Score: {self.game.score}")

    def get_tile_color(self, value):
        colors = {
            0: "lightgray",
            2: "lightyellow",
            4: "lightgoldenrodyellow",
            8: "orange",
            16: "darkorange",
            32: "tomato",
            64: "red",
            128: "yellow",
            256: "yellowgreen",
            512: "green",
            1024: "lightblue",
            2048: "blue",
        }
        return colors.get(value, "black")

    def handle_move(self, direction):
        if direction == 'left':
            self.game.move_left()
        elif direction == 'right':
            self.game.move_right()
        elif direction == 'up':
            self.game.move_up()
        elif direction == 'down':
            self.game.move_down()
        self.update_board()
        if self.game.is_game_over():
            self.show_game_over()

    def handle_undo(self):
        self.game.undo()
        self.update_board()

    def show_game_over(self):
        self.game.save_high_score()
        game_over_label = tk.Label(self.root, text="Game Over", font=(
            "Helvetica", 36), bg="red", fg="white")
        game_over_label.pack()


# Run the game
if __name__ == "__main__":
    difficulty = input(
        "Choose difficulty (easy/normal/hard): ").strip().lower()
    if difficulty not in ['easy', 'normal', 'hard']:
        difficulty = 'normal'
    game = Game2048(difficulty=difficulty)
    gui = Game2048GUI(game)

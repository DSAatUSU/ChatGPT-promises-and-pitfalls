import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon("icon.png"))
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.current_player = "X"
        self.init_ui()

    def init_ui(self):
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px")
        self.update_label()

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 3)

        buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setStyleSheet("font-size: 48px")
                button.clicked.connect(lambda _, i=i, j=j: self.button_clicked(i, j))
                layout.addWidget(button, i+1, j)
                row.append(button)
            buttons.append(row)

        self.setLayout(layout)
        self.show()

    def button_clicked(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.update_label()
            self.update_button(row, col)
            winner = self.check_winner()
            if winner:
                self.label.setText(f"Player {winner} wins!")
                self.disable_buttons()
            elif self.is_board_full():
                self.label.setText("It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_label(self):
        self.label.setText(f"Player {self.current_player}, it's your turn.")

    def update_button(self, row, col):
        button = self.layout().itemAtPosition(row+1, col).widget()
        button.setText(self.current_player)

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                button = self.layout().itemAtPosition(i+1, j).widget()
                button.setEnabled(False)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[2][0] is not None:
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            if None in row:
                return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())

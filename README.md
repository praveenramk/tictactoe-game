<h3>Tic Tac Toe Game</h3>
A simple two-player Tic Tac Toe game implemented in Python with comprehensive testing and CI/CD pipeline using GitHub Actions.
Features

Two-player console game - Players take turns as X and O
Input validation - Prevents invalid moves and provides clear error messages
Game state tracking - Tracks wins, draws, and current player
Play again option - Continue playing multiple rounds

<h3>How to Play</h3>

1.Run the game:
python tictactoe.py

2.Enter moves as row,col (e.g., 1,2 for row 1, column 2)
3.The board uses 0-based indexing (0-2 for both rows and columns)
4.First player to get 3 in a row wins!


<h3>Testing</h3>

Run tests locally:
#### Install test dependencies
pip install pytest pytest-cov

#### Run tests
pytest test_tictactoe.py -v

#### Run with coverage
pytest test_tictactoe.py --cov=tictactoe

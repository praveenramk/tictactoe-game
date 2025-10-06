"""
Tic Tac Toe Game Implementation in Python
A simple two-player game implementation
"""


class TicTacToe:
    """Main Tic Tac Toe game class for two human players"""
    
    def __init__(self):
        """Initialize the game"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        self.moves_count = 0
        
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        self.moves_count = 0
    
    def display_board(self):
        """Display the current board state"""
        print("\n   0   1   2")
        print("  -----------")
        for i in range(3):
            print(f"{i}| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} |")
            if i < 2:
                print("  -----------")
        print("  -----------\n")
    
    def make_move(self, row, col):
        """
        Make a move at the specified position
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            True if move was successful, False otherwise
        """
        if self.game_over:
            print("Game is already over!")
            return False
            
        if not self.is_valid_move(row, col):
            print("Invalid move! That position is already taken or out of bounds.")
            return False
        
        # Make the move
        self.board[row][col] = self.current_player
        self.moves_count += 1
        
        # Check for winner
        if self.check_winner():
            self.winner = self.current_player
            self.game_over = True
        elif self.is_board_full():
            self.game_over = True
            self.winner = 'Draw'
        else:
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def is_valid_move(self, row, col):
        """Check if a move is valid"""
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        return self.board[row][col] == ' '
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False
    
    def is_board_full(self):
        """Check if the board is full"""
        return self.moves_count >= 9
    
    def get_available_moves(self):
        """Get list of available moves"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def get_game_status(self):
        """Get current game status"""
        if self.game_over:
            if self.winner == 'Draw':
                return "Game ended in a draw!"
            else:
                return f"Player {self.winner} wins!"
        else:
            return f"Player {self.current_player}'s turn"
    
    def play_console(self):
        """Play the game in console mode"""
        print("Welcome to Tic Tac Toe!")
        print("Player X goes first")
        print("Enter moves as row,col (e.g., '1,2' for row 1, column 2)")
        print()
        
        while not self.game_over:
            self.display_board()
            print(self.get_game_status())
            
            try:
                # Get player input
                move_input = input("Enter your move (row,col): ").strip()
                
                # Handle quit command
                if move_input.lower() in ['quit', 'exit', 'q']:
                    print("Thanks for playing!")
                    break
                
                # Parse input
                if ',' not in move_input:
                    print("Invalid format! Use row,col (e.g., 1,2)")
                    continue
                
                row, col = move_input.split(',')
                row = int(row.strip())
                col = int(col.strip())
                
                # Make the move
                self.make_move(row, col)
                
            except ValueError:
                print("Invalid input! Please enter numbers only (e.g., 1,2)")
            except KeyboardInterrupt:
                print("\nGame interrupted!")
                break
        
        # Show final board and result
        if self.game_over:
            self.display_board()
            print("\n" + "="*30)
            print(self.get_game_status())
            print("="*30)
            
            # Ask to play again
            play_again = input("\nPlay again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y']:
                self.reset_game()
                self.play_console()


def main():
    """Main function to run the game"""
    game = TicTacToe()
    game.play_console()


if __name__ == "__main__":
    main()
"""
Unit tests for Tic Tac Toe game
"""

import unittest
from unittest.mock import patch
from io import StringIO
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test cases for TicTacToe class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.game = TicTacToe()
    
    def test_initial_state(self):
        """Test initial game state"""
        self.assertEqual(self.game.current_player, 'X')
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.moves_count, 0)
        
        # Check empty board
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_make_valid_move(self):
        """Test making a valid move"""
        result = self.game.make_move(0, 0)
        self.assertTrue(result)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')
        self.assertEqual(self.game.moves_count, 1)
    
    def test_make_invalid_move_out_of_bounds(self):
        """Test making moves out of bounds"""
        result = self.game.make_move(-1, 0)
        self.assertFalse(result)
        
        result = self.game.make_move(0, 3)
        self.assertFalse(result)
        
        result = self.game.make_move(3, 0)
        self.assertFalse(result)
        
        # Current player should not change
        self.assertEqual(self.game.current_player, 'X')
    
    def test_make_invalid_move_occupied(self):
        """Test making a move on an occupied position"""
        self.game.make_move(1, 1)  # X moves
        result = self.game.make_move(1, 1)  # O tries same position
        self.assertFalse(result)
        self.assertEqual(self.game.current_player, 'O')  # Should still be O's turn
    
    def test_player_switching(self):
        """Test that players alternate correctly"""
        self.assertEqual(self.game.current_player, 'X')
        
        self.game.make_move(0, 0)
        self.assertEqual(self.game.current_player, 'O')
        
        self.game.make_move(1, 1)
        self.assertEqual(self.game.current_player, 'X')
    
    def test_horizontal_win(self):
        """Test horizontal win conditions"""
        # X wins on top row
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(0, 2)  # X wins
        
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'X')
    
    def test_vertical_win(self):
        """Test vertical win conditions"""
        # O wins on middle column
        self.game.make_move(0, 0)  # X
        self.game.make_move(0, 1)  # O
        self.game.make_move(0, 2)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(1, 0)  # X
        self.game.make_move(2, 1)  # O wins
        
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'O')
    
    def test_diagonal_win_main(self):
        """Test main diagonal win (top-left to bottom-right)"""
        # X wins on main diagonal
        self.game.make_move(0, 0)  # X
        self.game.make_move(0, 1)  # O
        self.game.make_move(1, 1)  # X
        self.game.make_move(0, 2)  # O
        self.game.make_move(2, 2)  # X wins
        
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'X')
    
    def test_diagonal_win_anti(self):
        """Test anti-diagonal win (top-right to bottom-left)"""
        # O wins on anti-diagonal
        self.game.make_move(0, 0)  # X
        self.game.make_move(0, 2)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(1, 0)  # X
        self.game.make_move(2, 0)  # O wins
        
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'O')
    
    def test_draw_game(self):
        """Test draw condition"""
        # Create a draw scenario
        moves = [
            (0, 0), (0, 1), (0, 2),  # X, O, X
            (1, 0), (1, 2), (2, 0),  # X, O, X  
            (1, 1), (2, 2), (2, 1)   # O, X, O
        ]
        
        for move in moves:
            self.game.make_move(move[0], move[1])
        
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'Draw')
    
    def test_is_board_full(self):
        """Test board full detection"""
        self.assertFalse(self.game.is_board_full())
        
        # Fill the board
        for i in range(3):
            for j in range(3):
                self.game.board[i][j] = 'X'
                self.game.moves_count += 1
        
        self.assertTrue(self.game.is_board_full())
    
    def test_get_available_moves(self):
        """Test getting available moves"""
        # Initially all 9 positions should be available
        moves = self.game.get_available_moves()
        self.assertEqual(len(moves), 9)
        
        # Make some moves
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        self.game.make_move(2, 2)
        
        moves = self.game.get_available_moves()
        self.assertEqual(len(moves), 6)
        self.assertNotIn((0, 0), moves)
        self.assertNotIn((1, 1), moves)
        self.assertNotIn((2, 2), moves)
    
    def test_reset_game(self):
        """Test game reset functionality"""
        # Make some moves
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        
        # Reset the game
        self.game.reset_game()
        
        # Check initial state
        self.assertEqual(self.game.current_player, 'X')
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.moves_count, 0)
        
        # Check board is empty
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_game_status_messages(self):
        """Test game status messages"""
        # Initial status
        status = self.game.get_game_status()
        self.assertEqual(status, "Player X's turn")
        
        # After a move
        self.game.make_move(0, 0)
        status = self.game.get_game_status()
        self.assertEqual(status, "Player O's turn")
        
        # Win condition
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(0, 2)  # X wins
        
        status = self.game.get_game_status()
        self.assertEqual(status, "Player X wins!")
    
    def test_draw_status(self):
        """Test draw status message"""
        # Create a draw
        moves = [
            (0, 0), (0, 1), (0, 2),  # X, O, X
            (1, 0), (1, 2), (2, 0),  # X, O, X  
            (1, 1), (2, 2), (2, 1)   # O, X, O
        ]
        
        for move in moves:
            self.game.make_move(move[0], move[1])
        
        status = self.game.get_game_status()
        self.assertEqual(status, "Game ended in a draw!")
    
    def test_move_after_game_over(self):
        """Test that moves cannot be made after game is over"""
        # Create a win
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(0, 2)  # X wins
        
        # Try to make another move
        result = self.game.make_move(2, 2)
        self.assertFalse(result)
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'X')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_board(self, mock_stdout):
        """Test board display"""
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 1)  # O
        self.game.display_board()
        
        output = mock_stdout.getvalue()
        self.assertIn('X', output)
        self.assertIn('O', output)
        self.assertIn('0   1   2', output)
    
    def test_check_winner_empty_board(self):
        """Test that empty board has no winner"""
        self.assertFalse(self.game.check_winner())
    
    def test_all_winning_combinations(self):
        """Test all possible winning combinations"""
        winning_combinations = [
            # Horizontal wins
            [(0, 0), (0, 1), (0, 2)],  # Top row
            [(1, 0), (1, 1), (1, 2)],  # Middle row
            [(2, 0), (2, 1), (2, 2)],  # Bottom row
            # Vertical wins
            [(0, 0), (1, 0), (2, 0)],  # Left column
            [(0, 1), (1, 1), (2, 1)],  # Middle column
            [(0, 2), (1, 2), (2, 2)],  # Right column
            # Diagonal wins
            [(0, 0), (1, 1), (2, 2)],  # Main diagonal
            [(0, 2), (1, 1), (2, 0)],  # Anti diagonal
        ]
        
        for combo in winning_combinations:
            self.game.reset_game()
            
            # Place X in winning positions
            for pos in combo:
                self.game.board[pos[0]][pos[1]] = 'X'
            
            self.assertTrue(self.game.check_winner(), 
                          f"Failed to detect win for combination {combo}")


class TestGameIntegration(unittest.TestCase):
    """Integration tests for complete game scenarios"""
    
    def test_complete_game_x_wins(self):
        """Test a complete game where X wins"""
        game = TicTacToe()
        
        moves = [
            (1, 1),  # X center
            (0, 0),  # O corner
            (0, 1),  # X top middle
            (2, 1),  # O bottom middle
            (2, 1),  # X tries occupied (should fail)
            (2, 0),  # X bottom left
            (0, 2),  # O top right
            (1, 0),  # X middle left (X wins with middle row)
        ]
        
        # Play through the moves
        expected_players = ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X']
        move_index = 0
        
        for i, move in enumerate(moves):
            if i == 4:  # The invalid move
                result = game.make_move(move[0], move[1])
                self.assertFalse(result)
            else:
                self.assertEqual(game.current_player, expected_players[move_index])
                result = game.make_move(move[0], move[1])
                self.assertTrue(result)
                move_index += 1
                
                # Check if game is over after move index 7 (X wins)
                if move_index == 7:
                    break
        
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, 'X')
    
    def test_complete_game_draw(self):
        """Test a complete game ending in draw"""
        game = TicTacToe()
        
        # Sequence that leads to a draw
        moves = [
            (0, 0),  # X top-left
            (1, 1),  # O center
            (0, 2),  # X top-right
            (0, 1),  # O top-middle
            (2, 1),  # X bottom-middle
            (1, 0),  # O middle-left
            (1, 2),  # X middle-right
            (2, 0),  # O bottom-left
            (2, 2),  # X bottom-right
        ]
        
        for move in moves:
            game.make_move(move[0], move[1])
        
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, 'Draw')
        self.assertEqual(game.moves_count, 9)


if __name__ == '__main__':
    unittest.main()
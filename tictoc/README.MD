# Tic-Tac-Toe is a two-player game played on a 3×3 grid. Players take turns placing X and O on the board and the first player to get three symbols in a row wins the game.

## Winning Rules

- Player X and Player O take turns making moves.
- A player wins by placing three of their symbols in a row.
- The three symbols can be in a row, column, or diagonal.
- If all 9 positions are filled and no player wins, the game is a draw.
- A position already occupied by a player cannot be selected again.

## Algorithm

- Create a 3×3 board with numbered positions.
- Display the board and ask the first player to choose a position.
- Validate the user's input and check whether the position is available.
- Place the player's symbol on the selected position.
- Check all possible winning combinations.
- If a player has three symbols in a row, declare that player the winner.
- If all positions are filled without a winner, declare the game a draw.
- Switch to the other player.
- Repeat the process until the game ends.

# Maze Game Implementation Hints

## Core Data Structures You'll Need:
- Player position: `(row, col)` coordinates
- Set to track visited cells: `visited_positions = set()`
- Counters: `steps`, `wall_hits`

## Key Functions to Plan:
1. **Find starting position** - scan maze for 'S'
2. **Display maze** - replace current position with '*', show 'S' if player moved
3. **Check valid move** - is target position a space, 'S', or 'G'?
4. **Count total empty spaces** - count all ' ', 'S', 'G' in original maze
5. **Calculate percentage** - `len(visited) / total_empty * 100`

## Movement Logic:
```python
moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
```

## Key Implementation Tips:
- Convert maze tuple to list of lists for easier manipulation
- Keep original maze for counting empty spaces
- Track visited positions as (row, col) tuples in a set
- Check bounds: `0 <= row < len(maze)` and `0 <= col < len(maze[row])`
- Win condition: current position has 'G' in original maze

## Display Strategy:
- Create a copy of maze for display
- Replace player position with '*'
- If player moved from start, show original 'S'

## Statistics Calculation:
- Round percentage: `round(percentage, 1)`
- Count empty spaces once at start, reuse throughout

## Trickiest Parts:
The most challenging aspects will be:
1. Managing the display (keeping 'S' visible after moving)
2. Calculating the percentage correctly
3. Handling edge cases for movement validation

## Main Game Loop Structure:
```python
while True:
    # Display current state
    # Show statistics
    # Check win condition
    # Get user input
    # Validate and process move
    # Update statistics
```

Good luck with your implementation!
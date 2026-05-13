# Lesson 13 - Tic Tac Toe Part 1/3

## Recap 1: diceGuess function
Create a function named 'diceGuess' with in 1 parameter,
'guess' (an integer between 1 and 6). The function returns True
if the guess matches a randomly generated number between 1 and
6, and False otherwise.

1. Import 'random' library
2. Define 'diceGuess' function with 1 parameter, 'guess'
        a. Using '.randint()', create and assign the
           'random_number' variable a random number between 1
           and 6
        b. Using 'return', return the boolean value of
           'guess == random_number'

Usage example:
if diceGuess(5):
    print("Correct!")
else:
    print("Incorrect.")

## Task 1: Setup Turtle
Let’s start by setting up Turtle and creating a window.

1. Import the turtle library
2. Create a constant variable BOARD_SIZE and assign 800 to it, this will be the size of our window
3. Create a function named setup_turtle
4. Assign the screen and pen with .Screen() and .Turtle()
5. Setup the screen’s width and height with BOARD_SIZE
6. Set the pen size to 5 and .hideturtle()
7. Call the setup_turtle function and .mainloop()

## Task 2: Draw Grid
We will draw the grid by dividing the window into 3 rows and 3 columns.

1. Create a constant variable CELL_SIZE = BOARD_SIZE // 3
2. Create a function named draw_grid
3. Use the constant variables to set the pen’s position and draw the grid with a loop

## Task 3: Draw X
Refer to the slides

## Task 4: Draw O
Refer to the slides

## Task 5: Draw Symbol
We need a function to translate the row and column input into coordinates before drawing.
- e.g. row 1, col 1 = (CELL_SIZE, CELL_SIZE)

We will add a ‘current_symbol’ variable to determine which symbol we are drawing (X or O).

Try calling the draw_symbol() function to draw the symbols.

# Lesson 14 - Tic Tac Toe Part 2/3

## Task 1: Initialize board
Create an ‘initialize_board()’ function that returns a 3x3 Tic Tac Toe board using nested lists. Each item in each of the list holds a space (‘ ‘).

Create an ‘initialize_board()’ function that does the following:
1. Create an empty list, ‘board’
2. Using ‘for’ loop to iterate 3 times,
- Create an empty list, ‘row’
- Using ‘for’ loop to iterate 3 times,
- Using ‘.append()’, add a space (‘ ‘) into the list, ‘row’.
- Append (‘.append()’) the list, ‘row’ into the list, ‘board’ to create a nested list.
3. Return ‘board’

## Task 2: Get Player Move
Create a function named get_player_move

The function needs to take in 1 parameter, ‘board’
This allows the function to access the nested list we created

Ask for 2 inputs
1. row
2. Col

Use row and col to access the board and set it to ‘X’ or ‘O’
Call the function and print the updated board

## Task 3a: Check Board Full
1. Create a function named check_full
- Check if all moves have been made (i.e. the list is full)
2. The function needs to take in 1 parameter, ‘board’
- This allows the function to access the nested list we created
3. Loop through the nested list with a nested for loop
4. Check if the list has any empty spaces (‘ ‘)
5. Return true if there is, else return false

## Task 3b: Check Board Full
Call the check_full function in the main loop

If check_full returns true, break the loop

Print “Board is full.” before the program ends

## Task 4: Switch Symbol
1. Create a function named switch_symbol
- Change the symbol being set from “X” to “O” and vice versa
2. The function takes in 1 parameter, current_symbol
3. If current_symbol is “X”, return “O”, and vice versa
4. Initialize the current_symbol to “X”
5. Call the function in the main loop to reassign the current_symbol after each input
6. Modify the get_player_move function to take another parameter, current_symbol
7. Use current_symbol as the value set in the board

## Task 5a: Checking for Win Conditions
Let’s start by first creating a ‘WIN_CONDITIONS’ constant nested list that holds each of the following as a separate item:
1. All possible horizontal winning conditions
2. All possible vertical winning conditions
3. All possible diagonal winning conditions

There should be 8 items in total.

## Task 5b: Checking for Win Conditions
### ‘check_win’ function
Create a ‘check_win’ function with 1 parameter, ‘board’. This function must:
1. use the ‘WIN_CONDITIONS’ list you have created earlier
2. loop through each winning condition to check if:
- cell 1 == cell 2 == cell 3, and
- cell 1 != space (‘ ‘)
- return True if the above condition is met. Else, return False.

### Main game loop
Modify your main game loop to:
1. Use the ‘check_win’ function to break the loop if there is a win.
2. Print the board and print ‘{current_symbol} wins!’ if there is a win.

# Lesson 15 - Tic Tac Toe Part 3/3

## Task 1: Record Click Position
This function will convert the mouse pointer’s x and y coordinates in the window to rows and columns on the board.
Each square is CELL_SIZE so dividing the mouse coordinate by CELL_SIZE gives us the row and column.

For example:
- col = 400 // 266 = 1
- row = (800 – 150) // 266 = 2

## Task 2a: Wait for Click
1. Create a function, wait_for_click
2. The function uses the global clicked_row and clicked_col variables
3. Set clicked_row and clicked_col to None
4. Use Turtle’s onclick function to call record_click_position

## Task 2b: Wait for Click
1. Wait until a mouse click is detected using a while loop
- clicked_row and clicked_col is None when no clicks are detected
- Call turtle.update() to allow mouse clicks to be detected
2. Set screen.onclick(None) to stop detecting clicks
3. Return clicked_row and clicked_col values

## Task 3a: Get Player Move (Turtle)
1. Create a function, get_player_move_turtle
- The function takes 2 parameters, ‘board’ and ‘current_symbol’
2. In a while loop, 
- call the wait_for_click function and 
- create 2 variables to receive the return values, ‘row’ and ‘col’
3. Check if board[row][col] is empty, if it is:
- Use row, col, and current_symbol to set the symbol in the board
- Use row, col, and current_symbol and pass the values to the draw_symbol function as its parameters
- Break out of the loop

## Task 3b: Update Main Loop
Update the main code with the new functions and initialize the clicked_row and clicked_col global variables to be used by the functions.

## Task 4a: Display Messages
1. Create a function named, display_message
- It should take 1 parameter, ‘message’

2. Set the pen to go to the middle of the board

3. Use the pen.write() function to display the ‘message’ in the window

## Task 4b: Update Main Loop
Update the main loop to call display_message
- Display the winner if there is one, e.g. “Player X wins!”
- Else display “It’s a draw!”
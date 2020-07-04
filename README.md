# Sudoku-Solver
So this project took me roughly about 3 days to finish . The first 2 days were spent in me playing around with for/while loops.

The main obstacle in this project was Backtracking i.e retracing the path and rectifying the problem if the sudoku conditions are not satisfied.

Without backtracking , there are 9^81 diffent cases possible and therefore solving them using a normal algorithm would take ages.
There are many possible logics to solve this issue but the fastest one (according to me) is by using Recursive algorithm.
Commits that enhance the beauty of this program are openly welcomed . 

A GUI update can be expected soon :)

## The Rules Of Sudoku
The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.

The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.

The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, must also contain the numbers 1-9, without repetition or omission. 

![Sudoku Puzzle](SudokuImg.png)

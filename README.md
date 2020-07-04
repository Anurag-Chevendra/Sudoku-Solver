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

![Sudoku Puzzle](https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FRhydian_Lewis%2Fpublication%2F221411168%2Ffigure%2Ffig1%2FAS%3A648961878654978%401531735977703%2FExample-of-an-order-3-Sudoku-puzzle-This-particular-grid-is-logic-solvable.png&imgrefurl=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FExample-of-an-order-3-Sudoku-puzzle-This-particular-grid-is-logic-solvable_fig1_221411168&tbnid=ctaWbkyO_hFXJM&vet=12ahUKEwiwpL3tnrTqAhXm73MBHWk2CIAQMygGegUIARDaAQ..i&docid=-qoTy4plTdsv3M&w=510&h=383&q=sudoku%20puzzle&ved=2ahUKEwiwpL3tnrTqAhXm73MBHWk2CIAQMygGegUIARDaAQ)

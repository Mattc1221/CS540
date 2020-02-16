This program runs a hill climing algorithm to solve the nqueens problem.

The nqueens problem tries to place n queens on an n sized chess board such that 
no queen can attack another queen.

within this implementation of the n queens problem, a boulder has been placed on
the board that blocks each queen from passing through the position that the 
boulder has been placed on.

This programs input and output for the positioning of the queens is as follows:
	a list of integers where each integer pos at index i represents a queen
 	at position (i, pos) on the chess board with (0, 0) being the bottom of
	left corner of the board.
	Ex. [1,3,0,4,2] would be a chess board that looks like
		4    |   |   | Q |
		 --------------------
	 	3    | Q |   |   |
		 --------------------
		2    |   |   |   | Q
		 --------------------
		1  Q |   |   |   |
		 --------------------
		0    |   | Q |   | 
		   0   1   2   3   4
	    This would give us a board size of 5 with the queens at the 
	    positions above 

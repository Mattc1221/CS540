What does 8_torus_puzzle do?
  8_torus_puzzle solves an 8-torus puzzles in the minimun number of moves possible using the A* search algorithm
  This puzzle is different than the typical torus puzzle as tiles can be moved to the empty space from all 4 directions:
  Ex. 
     the following state of torus puzzle can be turned into any of the 4 states below it
        Original State:
        1 | 2 | 3 
          | 4 | 5  
        6 | 7 | 8
                    Possible Successor States:
                      | 2 | 3 
                    1 | 4 | 5  
                    6 | 7 | 8

                    1 | 2 | 3 
                    4 |   | 5  
                    6 | 7 | 8

                    1 | 2 | 3 
                    6 | 4 | 5  
                      | 7 | 8

                    1 | 2 | 3 
                    5 | 4 |    
                    6 | 7 | 8
                    
Most of the class priority_queue was written by my instructor Hobbes. She required me to modify it to handle the case where
a repeating state alread in the queue was enqueued.
As for the torus_puzzle class, I was designed everything from scratch.

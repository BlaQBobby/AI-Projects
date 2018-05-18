# AI-Projects
Mini AI Nuggets as I churn them out.
I decided to take on writing an AI for Tic-Tac-Toe which would be unbeatable by a human using the MiniMax Algorithm
Basically what happens is the AI takes a look at the possibilities based on the opponents moves down several branches till it arrives at a terminal state.
I denoted my terminal states as follows:
An AI win +10
A Draw 0
A Human win -10

The AI simulates each branch picking the best option for a human player and picking its best option as well as it goes back up the branch from it's current terminal state.
At the end of the day it optimizes all its options and picks its best solution which would never be worse than a tie.
If U let the AI go first, you'll notice a 4-5 sec pause, this position is the most tasking where it has no idea what the human opponent would play and as a result has to consider EVERYTHING.

Feel free to use my code for whatever... ;) 


# Sprite Packing Mini-Project
In this project, you will develop code to efficiently pack sprites onto a rectangular display of fixed resolution. This is a common task in computer graphics where programmers want to strategically load rectangular images onto the screen. Engineers are conscientious of the processing power required to render an entire screen, and thus need to be economical with the placement of the sprites.

Your task is simple: given a display of fixed size `(A, B)` and a set of `N` sprites, each of which is of size `(a_i, b_i)`, design and implement an algorithm to efficiently pack sprites onto the display. Your code should take as input the tuple `(A, B)` and a list of tuples `[(a_1, b_1), (a_2, b_2), ...`, and it should return a list of coordinates for the **upper left corner** of each sprite, and a list of sprites for each of those coordinates. You may assume that all rectangles have integer size (pixels can't be divided), and sprites cannot intersect with each other or the display boundary. *By convention, the first tuple element is the width; the second is the height*

Be aware this class of problem is `NP-hard`, and thus an exact optimal solution for the abstract task is certifiably computationally intractable. This project is therefore designed to evaluate: 

1. how you approach open-ended computing tasks
2. your skills in standing up code architecture from a blank slate
3. your ability to design, evaluate and communicate algorithms

Above all, though, this task is designed to give you room to display how you do engineering work, so feel free to dive deep into your algorithm!

Some questions to consider as you work:

1. What does "efficient" packing look like? 
2. Because this problem is `NP-hard`, what heuristics will you use to define your algorithm?
3. (Brownie points if you implement) How would your algorithm be different if you had knowledge of more displays? i.e., if you knew you had `M` displays of size`(A_1, B_1), (A_2, B_2) ... (A_M, B_M)` and the same `N` sprites to pack, how would you adjust your heuristics?

Please return an updated `sprites.py` file that includes your implementation of the `compute_sprite_positions` method, along with any and all documentation, examples or supporting files.

*Note*: some boiler plate code has been provided in the attached `sprites.py`. To test your code, provide a path to a text file as a command line argument to Python, i.e., `python3 sprites.py <file>`. This text file should have the following syntax:

```
Display: 
(A, B)

Sprites: 
(a_1, b_1)
(a_2, b_2)
(a_3, b_3)
...
```
Execution of the boiler plate code should print an ASCII representation of the sprites to the standard output. (You should keep your integers small enough to fit nicely in your terminal)

Try executing `python3 sprites.py example.txt` to see a few sprites rendered in your terminal. (You will need to install `prettytable` via `pip3`) 

*Note*: You are completely free to implement your algorithm in a languange other than Python, but you'll have to rewrite the boiler plate code in order to test your functions. 
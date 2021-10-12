# Sprite Packing Analysis and Documentation
## Reframing and motivation
Having actually worked with updating displays of finite pixels, I felt it was necessary to provide an alternative motivation for the sprite packing problem.  The computational power needed to update the display is a consideration, but would likely be dwarfed by all but the most simplistic placement algorithms.  As such, I chose to think of the problem as the "packing ads onto an arbitrary jumbotron" problem.  The reqirement to pack as efficiently as possible then makes sense without needing to be motivated by processing power.

![like this jumbotron for example](https://gocommandoapp.com/wp-content/uploads/2015/08/Jumbotron.jpg)

Additionally, we can make at least two assumptions, without loss of generality, to simplify the solution design:

1. For a display specified in the form `(Width, Height)`, we can assume that `Width >= Height`.  Transposing both the sprites and the display is sufficient to address the more general problem with this simplifying assumption.
2. We can also assume that the largest `w_i <= Width` and that the largest `h_i <= H` for all sprites.  Cases where this is false are fundamentally untractable because there is no set of displays capable of displaying all the sprites.

## Program design
Main goals were to extend the flexibility and modularity of the program to facilitate the testing of multiple datasets and multiple algorithms, eventually to be contributed by multiple authors.
### Flexibility
blah
### Modularity
blah
### Colaboration
blah

## Algorithm design


## What is effeciency?

The most straight forward measure of effeciency for a single screen is the number of pixels displaying sprites over the total number of pixels.  We'll call this **Individual Screen Effeciency** or **ICE**.  ICE can be useful as we'll see below, but it fails to be an effective means for identifying efficient algorithms on its own.  Using ICE across multiple samples of randomized display and sprites provides a slightly better metric, but may have trouble distinguishing performance of algorithms that routienly perform very well.  If all we care about is efficient packing of a single screen, we could end here.  If, however, we're seeking to select the most effecient packing algorithm, we'll need another measure.

This brings us to our foundational performance metric, called **Total Efficiency** or **TE**, which is simply the total number of screens required to show all the sprites.  When used for a specific display and set of sprites, this metric might be insufficient to accurately differentiate between two or more algorithms.  For example, when the volume of sprites is such that it is not quite possible to fit them all on one screen, both a good packing algorithm and a bad packing algorithm may achive a TE of 2.  There is no need to calculate pixel level efficiency across all the screens because if all the sprites are plotted on the same total number of screens, the same total number of pixels must be used/unused in total, regardless of the arrangement of the sprites.

In order to evaluate algorithms more holisticly, it is necessary to randomly generate display sizes and sprites to evaluate each algorithm over thousands (or even tens of thousands of samples).  Summing the Total Effeciency for an algorithm across each of the samples would allow us to calulate a score, called **Sum Total Effeciency** or **STE**.  The STE metric is of course specific to the parameters of random generation and the number of samples, but is a more robust indicator of which algorithms tend to be more efficient.  As long as the same large set of samples is used to evaluate all the algorithms, STE provides a resonable metric by which to choose an algorithm under most circumstances.  If necessary, ties can be broken with the *lowest* average ICE score on the last screen of each sample.

### Bonus points
...algorithm improvements...

...metrics improvements...



Some questions to consider as you work:

1. What does "efficient" packing look like? 
2. Because this problem is `NP-hard`, what heuristics will you use to define your algorithm?
3. (Brownie points if you implement) How would your algorithm be different if you had knowledge of more displays? i.e., if you knew you had `M` displays of size`(A_1, B_1), (A_2, B_2) ... (A_M, B_M)` and the same `N` sprites to pack, how would you adjust your heuristics?

Please return an updated `sprites.py` file that includes your implementation of the `compute_sprite_positions` method, along with any and all documentation, examples or supporting files.

*Note*: some boiler plate code has been provided in the attached `sprites.py`. To test your code, provide a path to a text file as a command line argument to Python, i.e., `python3 sprites.py <file>`. This text file should have the following syntax:


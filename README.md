# Sprite Packing Analysis and Documentation
## Note to unfamiliar readers
The remainder of this document assumes familiarity with the challenge as stated in [the instructions](https://github.com/cadet702/Display_Puzzle/blob/master/Instructions.md).  None of the context is repeated here, so new readers are advised to continue only after reviewing the other document.

## Reframing and motivation
Having actually worked with updating displays of finite pixels, I felt it was necessary to provide an alternative motivation for the sprite packing problem.  The computational power needed to update the display is a consideration, but would likely be dwarfed by the computational power needed by all but the most simplistic placement algorithms.  As such, I chose to think of the problem as the "packing ads onto an arbitrary jumbotron" problem.  The reqirement to pack as efficiently as possible then makes sense without needing to be motivated by processing power.

![like this jumbotron for example](https://gocommandoapp.com/wp-content/uploads/2015/08/Jumbotron.jpg)

Additionally, we can make at least two assumptions, without loss of generality, to simplify the solution design:

1. For a display specified in the form `(Width, Height)`, we can assume that `Width >= Height`.  Transposing both the sprites and the display is sufficient to address the more general problem with this simplifying assumption.
2. We can also assume that the largest `w_i <= Display Width` and that the largest `h_i <= Display Height` for all sprites.  Cases where this is false are fundamentally untractable because there is no set of displays capable of displaying all the sprites.

## Program design
Main goals were to extend the flexibility and modularity of the program to facilitate the testing of multiple datasets and multiple algorithms, eventually to be contributed to by multiple authors.

### Flexibility
The program was extended to allow an (optional) additional argument which specifies the algorithm to be used for packing sprites onto the display.  Additionally, multiple test datasets were created to make use of the flexibility provided by the first argument. Additionally, a method for generating random datasets is supported.

### Modularity
The program is designed to facilitate the testing of multiple algorithms.  To make this easier, all functions in the callable_algorithms.py file are included in the local scope.  This means that a contributer only needs to modify the callable_algorithms.py file in order to be able to call their new algorithm via sprites.py.  Future work would allow all functions in all files of the helper_functions folder to be automatically included in a similar manner.

### Collaboration
To facilitate ease of use on Windows PCs, a .bat file was added providing both the location of the python interpreter and the script to be executed, including any arguments.  Additionally, the requirements.txt file has been included in the repository to make exact reproduction of the environment possible.  The clarity of several comments was also improved and the display was modified to plot sequential characters instead of random characters to help make different packing algorithms more understandable.

## Algorithm design
The primary algorithm used for demonstration is a form of binary search.  This approach was selected for its balance of reasonable performance and ease of implementation in a limited time window.  A second algorithm was also devised, however, there was insufficient time for more than a rough outline and documentation of the intended design.  Each of these algorithms are discussed in more detail below.

### Binary search
This simply plots the tallest sprite that fits in the display and then subdivides the unused area into two smaller displays to repeat the process.  One display is formed from all unused pixels that are strictly to the right of the sprite.  The second display is formed from the pixels of all rows below the sprite.  The function is applied recursively until no additional sprites can be plotted in the remaining display(s), either because there are no more, or the room in each of the remaining displays is insufficient.

### Aglomeration and diagonal packer
This process begins by finding all pairs of sprites that have a common width or height and forming a list of aglomerated sprites with the combined dimensions.  This process is repeated until no more aglomerations can be formed that fit within the display.  It is important to track meta-data with these aglomerations to allow for efficient sprite selection and avoid unnecessary duplication.

With all possible aglomerations in hand, the algorithm would select the tallest sprite (or aglomeration) that fits for each step, plotting them across the top until no more can be plotted.  After each step, it is important to cull all spites and aglomerations from the list that contain any of the sprites just plotted as these are no longer valid candidates for packing.  Retaining meta data about the plotted sprites and aglomerations allows us to now switch to plotting the tallest sprites that don't colide with existing sprites in the antiparallel direction along the bottom.  With the retention or computation of additional data, it is possible to now make numerous passes down the diagonal to continue attempting to plot sprites until no more can be plotted.

## What is efficiency?
The most straight forward measure of efficiency for a single screen is the number of pixels displaying sprites over the total number of pixels.  We'll call this **Individual Screen efficiency** or **ICE**.  ICE can be useful as we'll see below, but it fails to be an effective means for identifying efficient algorithms on its own.  Using ICE across multiple samples of randomized display and sprites provides a slightly better metric, but may have trouble distinguishing performance of algorithms that routinely perform very well.  If all we care about is efficient packing of a single screen, we could end here.  If, however, we're seeking to select the most effecient packing algorithm, we'll need another measure.

This brings us to our foundational performance metric, called **Total Efficiency** or **TE**, which is simply the total number of screens required to show all the sprites.  When used for a specific display and set of sprites, this metric might be insufficient to accurately differentiate between two or more algorithms.  For example, when the volume of sprites is such that it is not quite possible to fit them all on one screen, both a good packing algorithm and a bad packing algorithm may achieve a TE of 2.  There is no need to calculate pixel level efficiency across all the screens because if all the sprites are plotted on the same total number of screens, the same total number of pixels must be used/unused in total, regardless of the arrangement of the sprites.

In order to evaluate algorithms more holisticly, it is necessary to randomly generate display sizes and sprites to evaluate each algorithm over thousands (or even tens of thousands of samples).  Summing the Total efficiency for an algorithm across each of the samples would allow us to calulate a score, called **Sum Total efficiency** or **STE**.  The STE metric is of course specific to the parameters of random generation and the number of samples, but is a more robust indicator of which algorithms tend to be more efficient.  As long as the same large set of samples is used to evaluate all the algorithms, STE provides a resonable metric by which to choose an algorithm under most circumstances.  If necessary, ties can be broken with the *lowest* average ICE score on the last screen of each sample.

## Bonus points

### Algorithm improvements
Needing to pack multiple displays of different sizes introduces the possibility that optimal packing on one display may induce severely suboptimal packing on another.  My instinct would be for an algorithm to start by trying to pack the displays from smallest to largest, but it is easy to envision a way this could go awry.

### Metrics improvements
It still makes sense to measure overall efficiency across the multiple displays when scoring algorithms, however, the algorithms themselves may benefit from using the packing efficiency on a screen to inform their decisions.  The method of measuring efficiency by requiring all sprites to be displayed on as many displays as needed can also be generalized by treating the displays of various size as a set that must be duplicated in its entirety to handle sprites that were not packed into earlier sets of displays.
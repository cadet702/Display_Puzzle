'''
Program Name: main
AKA: wrapper or calling script

Purpose: to orchestrate the calling of the various
    functions needed to pack sprites into displays

Author: Peter Griffin
'''

from helper_functions import callable_algorythms


def render(display, sprites, algorythm='hardcoded_example'):
    if algorythm=='hardcoded_example':
        log.info("No algorythm specified, defaulting to example.")
        print("No algorythm specified, defaulting to example.")
        positions, sprites = callable_algorythms.hardcoded_example(display, sprites)
    elif algorythm in imported_functions:
        log.info("Algorythm " + algorythm + " selected")
        print("Algorythm " + algorythm + " selected")
        positions, sprites = globals()[algorythm](display, sprites)
    else:
        log.error("No algorythm named "  + algorythm + " was found!")
        print("ERROR: No algorythm named "  + algorythm + " was found!")

    ## Create the display array
    out = np.empty(display, dtype=str)
    ## Fill with .
    out[:] = "."
    ## For each sprite, get its position and size, and fill in the array with a 
    ## randomly selected character
    for pos, sprite in zip(positions, sprites):
        x_start, y_start = pos
        x_end, y_end = x_start + sprite[0], y_start + sprite[1]
        out[x_start:x_end, y_start:y_end] = random.choice(string.ascii_letters)

    out = out.T ## Transpose so width and height are correct per problem definition
    
    ## Use prettytable to make nice ASCII table
    p = PrettyTable()
    for row in out:
        p.add_row(row)
    print(p.get_string(header=False, border=True, vrules=FRAME))

## Only execute code if run directly (only define functions if imported)
if __name__ == "__main__":
    import re
    import argparse
    import os
    import pandas as pd
    import numpy as np
    import string
    import random
    import datetime

    from prettytable import PrettyTable, FRAME ## Use prettytable to make nice ASCII table

    #from dynamic_import import *

    before_import = set(dir()) #print(before_import)
    from helper_functions.misc                import * ## Imports all functions in misc into the local scope (so they can be called directly)
    from helper_functions.callable_algorythms import * ## Imports all functions in callable_algorythms into the local scope (so they can be called directly)
    after_import = set(dir()) - set(['before_import']) #print(after_import)
    imported_functions = after_import - before_import
    print("Diff: ", imported_functions)

    # Force Pandas to show all of the columns using the following commands
    pd.set_option('display.max_columns', 1000) # Now we will see up to 1000 columns
    pd.set_option('display.max_colwidth', 1000) # And we will see up to 1000 characters in each column

    # Create Log Path
    log_path = "C:/Users/" + str.lower(os.getlogin()) + "/Desktop/Display_Puzzle/program_logs/"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # print (now.strftime("%Y-%m-%d %H h %M m %S s"))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H h %M m %S s")
    my_log_name = log_path + "Box Plotter v0.0.1 run " + now + " by " + str.lower(os.getlogin())

    # Create log function that uses a new and distinct file in the BOX folder
    log = construct_logger(my_log_name)
    ## -------------------------------- Begin Main Code --------------------------------------
    log.info("Wrapper program run from __main__")

    parser = argparse.ArgumentParser(description='Sprite Packing')
    parser.add_argument('inp_file', type=str)
    parser.add_argument('algorythm_name', type=str)
    args = parser.parse_args()

    if ~(str(args.inp_file) in('original_example.txt','manual_inputs.txt','perverse_inputs.txt')):
        ## generate new data and ouput to file:
        display_width  = random.choice(list(range(1, 31)))
        display_height = random.choice(list(range(1, 31)))
        sprite_count = random.choice(list(range(5, 11)))
        random_sprites = list()
        for i in range(1, sprite_count):
            ## Append a randomly sized tuple to the list
            random_sprites.append((random.choice(list(range(1, display_width+1))), random.choice(list(range(1, display_height+1)))))

        with open(args.inp_file, 'w') as f:
            f.write('Display:\n')
            f.write('(')
            f.write(str(display_width))
            f.write(', ')
            f.write(str(display_height))
            f.write(')\n\n')
            f.write('Sprites:\n')
            for sprite in random_sprites:
                f.write(str(sprite))
                f.write('\n')


    with open(args.inp_file, 'r') as f:
        lines = f.readlines()

    ## Initialize these variables before looping through the lines in the file
    get_display = False
    get_sprites = False
    sprites = list()

    for line in lines:
        ## Allows for whitespace in file to not be disruptive (by skipping those lines)
        if line == "\n": 
            continue

        ## When recording flag is set, ingest the line of data
        if get_display:
            display = eval(line)
            get_display = False
        if get_sprites: ## Note: this must be the last section of the file b/c recording is never turned off
            sprites.append(eval(line))

        ## When the line matches the key word, record the following non-blank line
        if line.startswith("Display:"):
            get_display = True
        if line.startswith("Sprites:"):
            get_sprites = True

    print(display)
    print(sprites)
    ## Display is in the form (W,H)
    ## We can assume WOLOG that W >= H (algorythm code will make this assumption)
    ## We can assume that the largest w_i <= W and the largest h_i <= H

    ## Run the specified algorythm and data set
    algorythm = args.algorythm_name
    if args.inp_file == 'original_example':
        render(display, sprites)
    else:
        render(display, sprites, algorythm)


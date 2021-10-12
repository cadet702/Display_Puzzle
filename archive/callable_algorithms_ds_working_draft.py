'''
This is the default used with the example file
'''
def hardcoded_example(display, sprites):
    return [(0,0), (6, 6)], sprites

'''
This reformats the inputs for use in binary search
'''
def reformat_inputs(display, sprites):
    formatted_sprites = 'blah'
    start_location = [0,0]
    display, sprites = binary_search(display, formatted_sprites, start_location)
    return display, sprites

'''
This uses a recursive binary search to plot sprites
'''    
def binary_search(display, sprites, start, call_count=0):
    sprites_to_plot = list()
    raw_plot_point_list = list()
    raw_sprites_in_plot_order = list()
    print('call_count = ', call_count)
    call_count += 1

    sprites_that_fit = [sprite for sprite in sprites if not ((sprite['width'] > display[0]) or (sprite['height'] > display[1]))]
    if len(sprites_that_fit) == 0:
        print('No sprites fit!')
        empty_list_of_sprites = list()
        empty_list_of_locations = list()
        return empty_list_of_locations, empty_list_of_sprites
    else:
        ## Find largest valid (width < display[0], height < display[1]) sprite
        selected_sprite = max(sprites_that_fit, key=lambda x:x['height'])

        ## Move selected sprite to new list (Find the index of 1st base unit and add it to the list to plot)
        index_of_sprite_to_pop = next((index for (index, d) in enumerate(sprites) if d['image id'] == selected_sprite['image id']), None)
        if ~(index_of_sprite_to_pop is None):
            #print('index_of_sprite_to_pop = ', index_of_sprite_to_pop)
            sprites_to_plot.append(sprites.pop(index_of_sprite_to_pop))
        else:
            print('I hate python:', selected_sprite)
        ## start location to list and add sprite tuple to list 
        raw_plot_point_list.append((start[0],start[1]))
        raw_sprites_in_plot_order.append((selected_sprite['width'],selected_sprite['height']))

        print('raw_plot_point_list: ', raw_plot_point_list)
        print('raw_sprites_in_plot_order: ',raw_sprites_in_plot_order)

    #return raw_plot_point_list, raw_sprites_in_plot_order

        ## Calculate new display_1
        display_1 = (display[0]-selected_sprite['width'], selected_sprite['height'])
        print('display_1 = ', display_1)
        if display_1[0] > 0:
            ## Calculate new start_location_1
            new_start_1 = [start[0] + selected_sprite['width'], start[1]]
            raw_location_list_1, raw_sprite_list_1 = binary_search(display_1, sprites, new_start_1, call_count)
            print('raw_location_list_1: ', raw_location_list_1)
            print('raw_sprite_list_1: ', raw_sprite_list_1)
            if raw_location_list_1:
                for returned_location in raw_location_list_1:
                    raw_plot_point_list.append(returned_location)
                for returned_sprite in raw_sprite_list_1:
                    raw_sprites_in_plot_order.append(returned_sprite)
                    ## Need to remove each returned sprite from list BEFORE 2nd call? Apparently not..
                    #index_of_returned_sprite_to_pop = next((index for (index, d) in enumerate(sprites) if (d['width'] == returned_sprite[0]) and (d['height'] == returned_sprite[1]) ), None)
                    #print('index_of_returned_sprite_to_pop: ', index_of_returned_sprite_to_pop)
                    #if ~(index_of_returned_sprite_to_pop is None):
                    #    sprites_to_plot.append(sprites.pop(index_of_returned_sprite_to_pop))
                    #else:
                    #    print('None found when returned_sprite is: ', returned_sprite)
                print('lists updated')
                print('sprites = ', sprites)

        ## Calculate new display_2
        display_2 = (display[0], display[1]-selected_sprite['height'])
        if display_2[1] > 0:
            ## Calculate new start_location_2
            new_start_2 = [start[0], start[1] + selected_sprite['height']]
            raw_location_list_2, raw_sprite_list_2 = binary_search(display_2, sprites, new_start_2, call_count)
            print('raw_location_list_2: ', raw_location_list_2)
            print('raw_sprite_list_2: ', raw_sprite_list_2)
            if len(raw_location_list_2) > 0:
                for returned_location in raw_location_list_2:
                    raw_plot_point_list.append(returned_location)
                for returned_sprite in raw_sprite_list_2:
                    raw_sprites_in_plot_order.append(returned_sprite)

    return raw_plot_point_list, raw_sprites_in_plot_order

## ------------------------------------ PG Algorithm ----------------------------------------
'''
This makes sprite aglomerations and then calls another algorithm
'''
def compute_sprite_positions(display, sprites):
    ## Find sets of all sprites with the same height (where total_width <= display[0])

    ## Find sets of all sprites with the same width (where total_height <= display[1])

    display_results, sprite_results = simple_place_across(display, sprites)
    return display_results, sprite_results

'''
This is the most basic algorithm to plot sprites
'''
def simple_place_across(display, sprites):
    remaining_sprites = sprites
    upper_bound_points = [[display[0],display[1]]]
    lower_bound_points = [[0,0]]
    sprites_to_plot = list()
    absolute_location_of_sprites = list()
    raw_sprites_in_plot_order = list()
    raw_plot_point_list = list()
    start_location = [0,0]

    import numpy as np
    from operator import itemgetter

    while_index=0
    while len(remaining_sprites) > 0:
        #print(while_index)
        ## FIX: add boundry condition check!

        ## Find height of the tallest sprite(s)
        tallest_value = max(remaining_sprites, key=lambda x:x['height'])['height']
        #print('tallest value: ',tallest_value)
        
        ## Find all sprites with that height and keep the fewest sub-units
        list_of_candidate_sprites = [d for d in remaining_sprites if d['height'] == tallest_value]
        fewest_sub_units = len(min(list_of_candidate_sprites, key=lambda x:len(x['contains']))['contains'])

        ## Find all sprites with that many sub-units and keep the widest
        list_of_candidate_sprites = [d for d in list_of_candidate_sprites if len(d['contains']) == fewest_sub_units]
        selected_sprite = max(list_of_candidate_sprites, key=lambda x:x['width'])
        #print("selected sprite: ", selected_sprite)
        #print("start_location: ", start_location)

        ## FIX: double check that handle aglomerations once that featue is complete
        #for base_unit, relative_locations in selected_sprite['contains'],selected_sprite['offset position']:
        #for base_unit, relative_locations in itemgetter('contains', 'offset position')(selected_sprite):
        for i, base_unit in enumerate(selected_sprite['contains']):
            relative_locations = selected_sprite['offset position'][i]
            #print('i = ', i)
            #print('base_unit = ', base_unit)
            #print('relative_locations = ', relative_locations)
            
            ## Find the index of 1st base unit and add it to the list to plot:
            index_of_sprite_to_pop = next((index for (index, d) in enumerate(remaining_sprites) if d['image id'] == base_unit), None)
            #print('index_of_sprite_to_pop = ', index_of_sprite_to_pop)
            sprites_to_plot.append(remaining_sprites.pop(index_of_sprite_to_pop))
            
            ## Calculate the associated absolute position and add it to the list
            #absolute_location = [s + r for s, r in zip(start_location, relative_locations)] ## non-numpy alternative
            absolute_location = np.add(start_location, relative_locations)
            absolute_location_of_sprites.append(absolute_location)

            ## Remove all sprites that contain the base unit
            index_of_sprites_to_remove = -1
            while ~(index_of_sprites_to_remove == None):
                index_of_sprites_to_remove = next((index for (index, d) in enumerate(remaining_sprites) if base_unit in d['contains']), None)
                if index_of_sprites_to_remove == None:
                    break
                #print('index_of_sprites_to_remove = ', index_of_sprites_to_remove)
                #print('remaining_sprites: ', remaining_sprites)
                junk = remaining_sprites.pop(index_of_sprites_to_remove)
                #print('junk = ', junk)
            
            #print('remaining_sprites: ', remaining_sprites)
        
        #print("remaining_sprites: ", remaining_sprites)

        ## Add lower corner to list of start location points ## FIX: this need to be revised to handle plotting along other edges!


        ## Update start_location ## FIX: this need to be revised to handle plotting along other edges!
        start_location = [start_location[0] + selected_sprite['width'], 0]

        while_index+=1

    for i, sprite in enumerate(sprites_to_plot):
        location = absolute_location_of_sprites[i]
        #print('i: ', i)
        #print('sprite: ', sprite)
        print('location: ', location)
        raw_sprites_in_plot_order.append((sprite['width'],sprite['height']))
        raw_plot_point_list.append((location[0],location[1]))

    return raw_plot_point_list, raw_sprites_in_plot_order

    
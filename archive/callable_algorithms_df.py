'''
This is the default used with the example file
'''
def hardcoded_example(display, sprites):
    return [(0,0), (6, 6)], sprites

'''
This is the most basic algorithm to plot sprites
'''
def simple_place_across(display, sprites):
    remaining_sprites = sprites
    list_of_plot_points = list()
    sprites_in_plot_order = list()
    start_location = [0,0]
    from operator import itemgetter
    
    for i in range(len(sprites)):
        print(i)
        ## find the sprite w/ the largest short dimension (height)
        tallest_sprite = max(remaining_sprites,key=itemgetter(1))
        #print("start_location: ", start_location)
        sprites_in_plot_order.append(tallest_sprite)
        list_of_plot_points.append(start_location)
        remaining_sprites.remove(tallest_sprite)
        #print("remaining_sprites: ", remaining_sprites)
        start_location = [start_location[0] + tallest_sprite[0], 0]
        #print(list_of_plot_points, sprites_in_plot_order)
    return list_of_plot_points, sprites_in_plot_order

    
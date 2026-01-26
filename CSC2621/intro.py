# Experiment: A cup has 3 marbles, 2 blue and 1 red. Draw 2 marbles without replacement
# and record if the marbles picked are the same color or different colors.

import random

def draw_marbles(colors, num_marbles):
    # for each add a color to the cup, looping through until we run out of num_marbles
    cup = []
    for marble in range(num_marbles):
        # use mod on the color list to loop through colors
        cup.append(colors[marble % len(colors)])
    first_draw = random.choice(cup)
    # with replacement 
    cup.remove(first_draw)
    second_draw = random.choice(cup)
    
    if first_draw == second_draw:
        return 'same color (' + first_draw + ')'
    else:
        return 'different colors (' + first_draw + ') (' +second_draw + ')'

# run 10 times, counting the number of same vs different color draws 
same_color_count = 0
different_color_count = 0
for _ in range(100):
    same_color_count = 0
    different_color_count = 0
    for _ in range(100):
        if 'same color' in draw_marbles(['blue', 'blue', 'red'], 3):
            same_color_count += 1
        else:
            different_color_count += 1
    print(f'Same color count: {same_color_count/100*100}%')
    print(f'Different color count: {different_color_count/100*100}%')

            

# Part 1: Problem Statement
"""The Eleves need you to finish decorating the North Pole by December 12th. Collect Stars by solving puzzles. 
You arrive at a secret entrance to the North Pole base ready to start decorating. The password seems to have been changed and you can't get in.
A document explains that the password is locked in the safe below. See attached document for new combination.

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial,
it makes a small click noise as it reaches each number. 

Input: sequence of rotation

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
Following these rotations would cause the dial to move as follows:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82. -1
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
Because the dial points at 0 a total of three times during this process, the password in this example is 3.

Analyze the rotations in your attached document. What's the actual password to open the door?"""

# Import required libraries
import csv

# Get puzzle input and store into a list for iterating through
with open('day1_input.txt', 'r') as file:
    reader = csv.reader(file)   
    list_of_input = list(reader)

#Create Variables to store the output of each turn and how many times we end at 0
start_val = 50
combo_counter = 0
# Iterate through every turn in the list by parsing the first part of the string which determines direction and the rest that determines the rotation. Only count if we end at 0.
for i in range(len(list_of_input)):
    turn = list_of_input[i][0][0] 
    turn_amt = int(list_of_input[i][0][1:])
    if turn == 'R':
        # When we turn right we increment by 1. When the value is 100 we default this to 0 and start over acting as if the range is 1 - 99
        # print("Starting at {s}, we move right {num} of spaces".format(s=start_val, num=turn_amt))
        for x in range(turn_amt):
            next_val = start_val + 1 
            if next_val == 0 or next_val == 100:
                next_val = 0
            elif next_val > 100:
                next_val = next_val - 100
            start_val = next_val
    elif turn == 'L':
        # print("Starting at {s}, we move left {num} of spaces".format(s=start_val, num=turn_amt))
        for x in range(turn_amt):
            next_val = start_val - 1
            if next_val < 0:
                # when moving left, we want to turn negative numbers descending from 99 to 1
                next_val = 100 + next_val
            start_val = next_val
    if start_val == 0:
        # if after turning we end at 0 add to our counter
        combo_counter +=1
    # print("We finished at 0: {times}, and are now at {new_num}".format(times=combo_counter, new_num =start_val))

print("The first combination is: ", combo_counter)


# Part 2: Count every time we pass 0 through sequence
# Update above code to count when passes through 0 as part of sequence
start_val = 50
combo_counter = 0
# Iterate through every turn in the list by parsing the first part of the string which determines direction and the rest that determines the rotation. Only count if we end at 0.
for i in range(len(list_of_input)):
    turn = list_of_input[i][0][0] 
    turn_amt = int(list_of_input[i][0][1:])
    if turn == 'R':
        # When we turn right we increment by 1. When the value is 100 we default this to 0 and start over acting as if the range is 1 - 99
        # print("Starting at {s}, we move right {num} of spaces".format(s=start_val, num=turn_amt))
        for x in range(turn_amt):
            next_val = start_val + 1 
            if next_val == 0 or next_val == 100:
                next_val = 0
                combo_counter+=1
            elif next_val > 100:
                next_val = next_val - 100
            start_val = next_val
    elif turn == 'L':
        # print("Starting at {s}, we move left {num} of spaces".format(s=start_val, num=turn_amt))
        for x in range(turn_amt):
            next_val = start_val - 1
            if next_val < 0:
                # when moving left, we want to turn negative numbers descending from 99 to 1
                next_val = 100 + next_val
            if next_val == 0:
                combo_counter+=1
            start_val = next_val
    # print("We finished at 0: {times}, and are now at {new_num}".format(times=combo_counter, new_num =start_val))

print("The second combination is: ", combo_counter)
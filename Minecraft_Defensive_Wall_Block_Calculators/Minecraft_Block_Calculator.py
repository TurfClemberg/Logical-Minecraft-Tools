# Minecraft Block Calculator v1.0
# Created by: Ankush
# Function: Calculates total blocks and stack counts for 4-sided walls, accounting for corner overlaps.

# Visualizing Diagram for easy understanding, necessary for correct user input
def visualize_diagram():
    print("""
    For helping you understand what values to input in which prompt, here is a quick diagram that will help you visualize your build:
                               A -------------------------------------------------------- B
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                 |                                                       |
                                D ------------------------------------------------------ C
    In the above diagram, AB is the length of the wall, and AD is the width""")

# User Input Prompts
def get_user_input():
    height_of_AB = int(input("Enter the height of AB of your wall (In Blocks): "))
    height_of_AD = int(input("Enter the height of AD of your wall (In Blocks): "))
    length_of_AB = int(input("Enter the length of AB of your wall (In Blocks): "))
    length_of_AD = int(input("Enter the length of AD of your wall (In Blocks): "))
    width_of_AB = int(input("Enter the width of AB of your wall (In Blocks): "))
    width_of_AD = int(input("Enter the width of AD of your wall (In Blocks): "))
    return height_of_AB, height_of_AD, length_of_AB, length_of_AD, width_of_AB, width_of_AD

# Logic for calculating total blocks, accounting for overlaps and intersections at the corners
def logic_calculation(height_of_AB, height_of_AD, length_of_AB, length_of_AD, width_of_AB, width_of_AD):
intersecting_blocks = ((width_of_AB * width_of_AD) * min(height_of_AB, height_of_AD))
    total_blocks_for_length = (length_of_AB * height_of_AB * width_of_AB) * 2
    total_blocks_for_breadth = ((length_of_AD * height_of_AD * width_of_AD) - intersecting_blocks * 2) * 2
    total_blocks = total_blocks_for_length + total_blocks_for_breadth
    stacks = total_blocks // 64
    remainder = total_blocks % 64
    return total_blocks, total_blocks_for_length, total_blocks_for_breadth, intersecting_blocks, stacks, remainder

# Program Output
def display_output(total_blocks, total_blocks_for_length, total_blocks_for_breadth, intersecting_blocks, stacks, remainder):
    print(f"Total Blocks required to build 4-sided wall: {total_blocks}")
    print(f"Blocks required to build the length of the wall: {total_blocks_for_length}")
    print(f"Blocks required to build the breadth of the wall: {total_blocks_for_breadth}")
    print(f"Intersecting Blocks: {intersecting_blocks * 4}, where each intersection point has {intersecting_blocks} blocks")
    print(f"Materials required: {stacks} stacks, and {remainder} more blocks")
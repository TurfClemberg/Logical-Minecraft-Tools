height_length = int(input("Enter the height of the longer side (length) of your wall (In Blocks): "))
height_breadth = int(input("Enter the height of the shorter side (breadth) of your wall (In Blocks): "))
length_length = int(input("Enter the length of the longer side (length) of your wall (In Blocks): "))
length_breadth = int(input("Enter the length of the shorter side (breadth) of your wall (In Blocks): "))
width_length = int(input("Enter the width of the longer side (length) of your wall (In Blocks): "))
width_breadth = int(input("Enter the width of the shorter side (breadth) of your wall (In Blocks): "))
if height_length == height_breadth:
    intersecting_blocks = (width_length * width_breadth * height_length)
elif height_length > height_breadth:
    intersecting_blocks = (width_length * width_breadth * height_breadth)
else:
    intersecting_blocks = (width_length * width_breadth * height_length)
total_blocks_for_length = (length_length * height_length * width_length) * 2
total_blocks_for_breadth = ((length_breadth * height_breadth * width_breadth) - intersecting_blocks * 2) * 2
total_blocks = total_blocks_for_length + total_blocks_for_breadth
stacks = total_blocks // 64
remainder = total_blocks % 64
print(f"Total Blocks required to build 4-sided wall: {total_blocks}")
print(f"Blocks required to build the length of the wall: {total_blocks_for_length}")
print(f"Blocks required to build the breadth of the wall: {total_blocks_for_breadth}")
print(f"Intersecting Blocks: {intersecting_blocks * 4}, where each intersection point has {intersecting_blocks} blocks")
print(f"Materials required: {stacks} stacks, and {remainder} more blocks")
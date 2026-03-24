import Calculator as calc
def main():
    # Show ASCII Diagram
    calc.visualize_diagram()
    # Get User Input
    h_ab, h_ad, l_ab, l_ad, w_ab, w_ad = calc.get_user_input()
    # Perform Calculations
    total_blocks, total_blocks_for_length, total_blocks_for_breadth, intersecting_blocks, stacks, remainder = calc.logic_calculation(h_ab, h_ad, l_ab, l_ad, w_ab, w_ad)
    # Display Output
    calc.display_output(total_blocks, total_blocks_for_length, total_blocks_for_breadth, intersecting_blocks, stacks, remainder)
if __name__ == "__main__":
    main()
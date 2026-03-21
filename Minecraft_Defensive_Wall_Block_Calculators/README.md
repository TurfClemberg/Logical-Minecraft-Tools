## Technical Specification: 4-Sided Wall Intersection Logic

### Overview
This project provides a high-precision computational solution for calculating the exact block volume required to construct a rectangular perimeter in a 3D grid environment. Unlike standard geometric approximations, this algorithm accounts for **Variable Axis Intersections**, ensuring zero-waste resource procurement for structures with varying heights, lengths, and thicknesses.

### The Problem: The Intersection Paradox
In a discrete voxel environment (like Minecraft), a standard calculation of four independent walls leads to "Double-Counting" at the four corner vertices. If a wall has a width ($W$) greater than 1, these overlaps become 3D volumes. 

Failing to account for these intersections results in an inventory surplus. This program identifies the shared volume between the "Length" and "Breadth" planes and subtracts them from the secondary axis to achieve a perfect fit.



### Core Logic & Formula
The algorithm operates on a **Primary-Axis Priority** model. The "Longer Side" (Length) is calculated as a full volume. The "Shorter Side" (Breadth) is then treated as a bridge between the two Length walls, with its intersecting corners removed.

#### 1. Intersection Detection
The program first determines the effective height of the intersection. If the two connecting walls have different heights, the shared volume is limited by the shorter wall:
* If $H_{length} == H_{breadth}$, Intersection Height = $H_{length}$
* If $H_{length} > H_{breadth}$, Intersection Height = $H_{breadth}$
* Otherwise, Intersection Height = $H_{length}$

#### 2. Volume Calculations
* **Single Corner Volume:** $W_{length} \times W_{breadth} \times \text{Intersection Height}$
* **Total Length Volume:** $(L_{length} \times H_{length} \times W_{length}) \times 2$
* **Total Breadth Volume:** $((L_{breadth} \times H_{breadth} \times W_{breadth}) - (\text{Single Corner Volume} \times 2)) \times 2$

### Technical Performance (Example Case)
For a fortification with the following parameters:
* **Dimensions:** $20 \times 15$ blocks
* **Height:** 4 blocks
* **Thickness (Width):** 4 blocks

**The Calculation Path:**
1.  **Length Walls:** $20 \times 4 \times 4 = 320$ per wall (**640 Total**)
2.  **Corner Overlap:** $4 \times 4 \times 4 = 64$ per corner
3.  **Breadth Walls (Adjusted):** $(15 \times 4 \times 4) - (64 \times 2) = 112$ per wall (**224 Total**)
4.  **Final Aggregate:** **864 Blocks**

### Inventory Logistics
To facilitate survival-mode builds, the output includes a **Voxel-to-Stack Conversion**. By applying Euclidean division and the modulo operator, the program translates the raw block count into standard 64-unit stacks. 

* **Logic:** `Total // 64` (Full Stacks) and `Total % 64` (Remainder)
* **Output for Example Case:** 13 Stacks, 32 Blocks.

### License
This project is licensed under the **MIT License**. It is designed for open collaboration and high-performance structural engineering.


### Implementation Instructions
1.  Clone the repository to your local environment.
2.  Execute `Minecraft_Block_Calculator.py`.
3.  Input your desired dimensions in integers (No rounding required).
4.  Utilize the output for precise `/give` commands or manual chest organization.
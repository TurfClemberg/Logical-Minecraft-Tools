## Modualtion
- [ ] Make the code modulable, using def()s to separate different parts of the code, such as input handling, calculations, and output generation. This will make the code more organized and easier to maintain.
- [ ] Create a main function that calls the other functions in a logical order, allowing for better readability and flow of the code.
## Input Handling
- [ ] Implement a loop, probably while True, to continously ask the user for input, so that unwanted inputs can be handled and the user can correct their input without crashing the program.
- [ ] Add error handling for invalid inputs, such as non-numeric values or negative numbers, to prevent the program from crashing and to provide feedback to the user about what went wrong.
- [ ] Add prompts, which can handle values required for intersection area calculations, specifying the distance from the outer/inner edge of the adjoining wall, sticking out/inside from the interconnection, as shown in Fig 1.0, 1.1, DS Book, Important Notes (Second Page)
This TODO is referring to Index, DS Book.
## Calculations
- [ ] Create a function that performs the necessary calculations for the defensive wall block, so that edge cases can be handled more easily and that such situations can be tested, handled and fixed without affecting the rest of the code, alongside making the code more organized and easier to read.
- [ ] Implement checks for edge cases, such as extremely large or small input values, to ensure that the program can handle a wide range of inputs without crashing or producing incorrect results.
- [ ] Add calculation logic, which will allow the user to freely enter a customised intersection area, by seting the distance from the outward/inward extending edge, closest to the adjacent edge wall, sticking out/in. (Note: Max intersection area is the width of AB/AD, when it is sticking in, or as a perimeter boudary {perfect square, no inwardness or outwardness}, DOES NOT APPLY WHEN STICKING OUT) Referrece to Fig 1.0 and Fig 1.1, alongside Important Notes (Second Page), DC Book.
## Output Generation
- [ ] Create a function that generates the output based on the calculations, allowing for better separation of concerns and making it easier to modify the output format in the future if needed.
- [ ] Format the output in a clear and user-friendly manner, providing all necessary information in a way that is easy to understand, such as using labels and units for the calculated values.
## Versatility
- [ ] Add features, or change them in a manner, such that they work equally good, cross-device, especially the ASCII Diagram, as on mobile, the diagram is not being displayed properly.
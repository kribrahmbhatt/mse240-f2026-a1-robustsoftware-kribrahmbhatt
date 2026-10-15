# Example Project 3: Store Inventory

## Project overview
For this project, you will pick any object for an online store, and implement it as a class. For example, you might pick a bicycle, a car, a book, handmade jewelry for your Esty shop, whatever.

For the design of the class, you may implement accessors/mutators as you think appropriate for your store interface. You thus have some flexibility in the logic of how you determine accessors and mutators, so long as it follows the requirements below. Just make sure your logic is consistent and your decisions make sense in that context.

You'll also need to design the main function - look at example projects 1 and 2 for inspiration.

## Initial goal: design and write a class using these requirements

    - Must have a string attribute _name representing the name of an individual item in an online store
        - For example, a bicycle might have a name like "MEC Midtown 2 Bicycle" or "Cannondale 2020 Tesoro Neo X 3 Remixte E-Bicycle"
    - Must have an accessor with the header "get_name(self) -> str"
    - Must have a float attribute _price representing the current price of an individual item
        - For example, a bicycle might have a price like 499.99 or 2,999.93
    - Must have an accessor with the header "get_price(self) -> float"
    - Must have at least one boolean attribute
    - Must have at least one integer attribute
    - Must have at least one list, set, or dictionary attribute
    - Must have at least two mutually dependent attributes (e.g., changing one changes the other, or changing one is depends on the value of the other)
    - Must have appropriate accessors and mutators for the represented object
    - Must have at least one accessor that requires calculation
        - (e.g., weight in kg and weight in lbs; one attribute, two accessors).
    - Must have at least one default value in the constructor.
    - TypeErrors and ValueErrors should appear as appropriate.

## Stretch goal: sort and filter with a variety of different parameters
As we start to work on lists and sorting algorithms, try implementing a sorting algorithm or two to sort your inventory in different ways, or filter different items out. You can add new commands for that in your main function. This will give you a head start on assignments 2 and 3.


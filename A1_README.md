# Assignment 1 Robust Software
In this assignment, there are several mini-projects for you to **practice your ability to design and implement correct, robust, and maintainable software.**

Things to focus on:
 - Object Oriented Programming (class design and implementation)
 - Software Engineering Process (git and test-driven development)
 - Coding Style (comments, documentation, variable names, ...)

There multiple example classes, each with a different focus and level of detail in its specification. You are encouraged to make each of them your own.

# Connection with Reflection 1
You can use your experience doing this assignment to inform your reflections, e.g., as the situation and/or task. This assignment is specifically aligned with the same professional skill used for Reflection 1 - the ability to design and implement correct, robust, and maintainable software.

# Grading
The grades for this assignment are simple: for full marks, you must have a **total of 100 passing, implemented unit tests across all projects.** Your grade will simply be the number of passing unit tests up to a maximum of 100. This means you can focus on a single sub-project (e.g., the pet tracker) or you can work across multiple ones. The initial tests in the projects can be used, modified, discarded, or built-upon.

The unit tests should **focus on the class definitions** in each project, **not the main interactive loop.** However, you may want to run and improve the interactive loop for both context and interactive testing to complement your unit tests. 

For unit tests to count, they must actually test the units. They cannot just be empty. As such, your grade, as a proportion, will be dictated by the following equation:

    (min(passing_unit_tests, 100) * multiplier)/100

Where multiplier ranges from [0, 1], judged across all of your unit tests and guided by the following rubric:
    0 if there are unit tests trivially pass (e.g., they're empty, call `self.assertTrue(True)`) to get the numbers up
    0.5 if the unit tests have many clear mistakes or don't line up with what they should be testing (e.g., in a unit test for `get_price()`, testing only for `get_name()` )
    0.75 if the unit tests are appropriate but universally have only 1 assertion each.
    1 if unit tests are appropriate and some have multiple assertions related to the same test. For example, you might assert multiple pre- and post-conditions; with `set_name()`, this could look like testing the name before and after calling the method, and checking that `set_name()` didn't change any other  variables by using `get_name()` alongside `get_price()` and other getters). Note that some unit tests will be short (especially errors), but it's good practice to have some that use multiple assertions in a more comprehensive way.

Although marking is purely based the the number and nature of the passing tests, you will want to use this as a chance to practice the processes developed in class, as this can provide some examples you can use for your reflections and let you solidify some of the concepts that will come up in the exams.

# Process

## Part 1: Specification and test plan
One way to help write robust software is with test-driven development (TDD): writing unit tests for a behavior before implementing it.

Your first task is thus to design the class, document its intended behaviour, and make a test plan. This enables you to really think through the behaviour of the class; what values are allowed vs. not allowed. While this is not submitted for Assignment 1, you can record it for Reflection 1.


# Implement Tests then Class

After specifying your test plan, you will follow test-driven development to create the class then implement it as per your specification. In this step, make sure to **track your progress so that you can write about it in your reflection** (e.g., screenshots or notes). We want to see evidence of class design first, then test plan implementation, then class implementation. **Take screenshots or and use git commits effectively** to help make your case. It is a good idea to commit frequently, especially after every major implementation (e.g., implementing a set of unit tests, or after creating a method or set of methods).

# A Note on Class Design
Once you have started implementing you class, you may want to make sure things are more efficient. There are a couple ideas here:

 1. Make things correct before making them efficient. Becaues you have a suite of tests, you can always tweak things to be faster. You may want to try implementing some of the algorithms or data structures we're talking about in class (e.g., sorting).
 2. Don't Repeat Yourself (DRY): One aspect of writing maintainable code is to not have redundant variables or functions. If you find yourself having the same code in multiple places, that's an easy way for bugs to sneak in - you might change one and not the others. In these cases, try to pull the code out into a single variable or function. I recommend having code never occuring 3 or more times.
 3. Document. Make sure you clearly explain what is going on and use variable names that are clear.

## Refactoring

When you start to add more complex features, you may want to **refactor** your code: change how your code is written or implemented without changing the behaviour. One example here in the Pet Tracker project is renaming the `dog` module and `Dog` class to a more general `pet` module and `Pet` class. If you do this, make sure tests are working, commit your work to source control, then start refactoring. You can continue to re-run your tests when done to make sure the behaviour is done.

Refactoring is not a requirement for MSE240, but rather a sneak peak of software engineering terms you may encounter in later classes.


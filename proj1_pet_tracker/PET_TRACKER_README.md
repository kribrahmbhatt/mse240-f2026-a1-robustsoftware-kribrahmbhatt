# Example Project 1: Pet Tracker

## Project overview

Build an application that mimics a pet-tracking app. It should help people keep useful information about their pets in one place, such as:

- Name and birthday
- Age (calculated from the birthday)
- Health issues or notes
- When the pet was last walked

Start with the core features and data your application needs, then expand them as you go.

## Initial goal: implement support for dogs

The current program has a main function that supports the Dog class, as developed in lecture. Your first goal is to implement this functionality, both through test-driven development of the Dog test suite and Dog class, then through minor modifications of the main loop.

## Stretch goal: support different kinds of pets

Go beyond dogs and support other pets, such as cats, turtles, and more. This is an opportunity to practice abstraction and reducing repetitive code and refactoring. Consider using inheritance and abstract base classes to share common pet behavior while allowing each kind of pet to provide its own details. You may have to do individual research here. Alternatively, design the model with private fields that can represent the species or type of pet. 

## How to run

Run the app (from the repository root): `python proj1_pet_tracker/pet_tracker_main.py`

Run the unit tests (from the repository root): `python -m unittest discover -s proj1_pet_tracker -t . -v`
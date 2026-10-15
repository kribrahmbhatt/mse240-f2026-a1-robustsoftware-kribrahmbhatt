# A1-template

Name: Krisha Brahmbhatt
Email: kri.brahmbhatt@gmail.com
Student number: 20952086

## Project Description

Pet Tracker is a small Python project for MSE 240 (Assignment 1: Robust Software). It models individual dogs and tracks their basic information and daily care.

**The `Dog` class** (`proj1_pet_tracker/dog/Dog.py`) stores a dog's name, breed, gender, weight, colour, potential health issues and birth year. It also tracks when the dog was last walked and fed.

- Every input is validated. A wrong type raises a `TypeError`, and an invalid value (an empty name, a weight of 0 or less or over 500 lbs, a birth year outside 1996 to 2026) raises a `ValueError`.
- A failed update leaves the dog unchanged.
- Getters return copies of internal data so outside code can't change it by accident.
- `needs_walk()` and `needs_meal()` report whether the dog is due, based on configurable time limits (default 8 hours between walks and 12 hours between meals).

**The interactive program** (`proj1_pet_tracker/pet_tracker_main.py`) is a text-based loop where you can add, remove, rename and weigh dogs, record health issues, and view dog information.

**Testing:** the class was built with test-driven development. The unit tests in `proj1_pet_tracker/test/test_Dog.py` cover constructor validation, accessors, mutators and the walk and meal logic, with 114 passing tests. Each test group was committed before the code that makes it pass, so the git history shows the process.


# Acknowledgements

I used generative AI (ChatGPT) as an assistive tool to clarify instructions, understand concepts, and troubleshoot coding issues. All code was reviewed and tested by me, and I am responsible for the final submitted work.
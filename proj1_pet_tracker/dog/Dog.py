# Dog.py
#
# Author: Krisha Brahmbhatt
# Email: kri.brahmbhatt@gmail.com
# Student ID: 20952086
# 
# Source code for the Dog class.
from datetime import datetime, timedelta

class Dog:
    """ Dog
        A class representing an individual dog.
    """

    CURRENT_YEAR = 2026                 # the year is assumed to always be 2026
    MAX_WEIGHT = 500.0                  # maximum weight in lbs
    MIN_BIRTH_YEAR = 1996               # oldest believable dog (30 years)
    DEFAULT_MAX_TIME_BETWEEN_WALKS = timedelta(hours=8)
    DEFAULT_TYPICAL_TIME_BETWEEN_MEALS = timedelta(hours=12)

    def __init__(self, name: str, breed: str, gender: str, initial_weight: float,
                 colour: str, potential_health_issues: list[str], birth_year: int):
        """ Dog constructor

            name    the dog's given name
            breed   the dog's breed
            gender  the dog's gender
            initial_weight  the dog's initial weight (lbs); int or float
            colour  a description of the dog's colour
            potential_health_issues a list of known potential health issues (each a string)
            birth_year  the year the dog was born

            Raises TypeError for wrong types and ValueError for invalid values.
        """
        # validate (type checks come before value checks inside each helper)
        Dog._check_text(name, "name")
        Dog._check_text(breed, "breed")
        Dog._check_text(gender, "gender")
        Dog._check_text(colour, "colour")
        Dog._check_weight(initial_weight)
        if not isinstance(potential_health_issues, list):
            raise TypeError("potential_health_issues must be a list")
        for issue in potential_health_issues:
            Dog._check_text(issue, "health issue")
        if type(birth_year) is not int:
            raise TypeError("birth_year must be an int")
        if birth_year < Dog.MIN_BIRTH_YEAR or birth_year > Dog.CURRENT_YEAR:
            raise ValueError("birth_year must be between MIN_BIRTH_YEAR and CURRENT_YEAR")

        # initialize private fields
        self._name = name
        self._breed = breed
        self._gender = gender
        self._weight = float(initial_weight)
        self._colour = colour
        self._potential_health_issues = list(potential_health_issues)  # defensive copy
        self._birth_year = birth_year
        self._most_recent_walk_time = None
        self._most_recent_meal_time = None
        self._max_time_between_walks = Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS
        self._typical_time_between_meals = Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS

     ###########################
    # Validation helpers (DRY)#
    ###########################

    @staticmethod
    def _check_text(value, label: str):
        """ raise TypeError if value is not a str, ValueError if blank """
        if not isinstance(value, str):
            raise TypeError(f"{label} must be a string")
        if value.strip() == "":
            raise ValueError(f"{label} cannot be empty")

    @staticmethod
    def _check_weight(value):
        """ raise TypeError/ValueError unless 0 < value <= MAX_WEIGHT """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("weight must be a number")
        if value <= 0:
            raise ValueError("weight must be > 0")
        if value > Dog.MAX_WEIGHT:
            raise ValueError("weight must be <= MAX_WEIGHT")

    @staticmethod
    def _check_duration(value, label: str):
        """ raise TypeError/ValueError unless value is a positive timedelta """
        if not isinstance(value, timedelta):
            raise TypeError(f"{label} must be a timedelta")
        if value <= timedelta(0):
            raise ValueError(f"{label} must be positive")

    @staticmethod
    def _resolve_time(when):
        """ return when (validated) or the current time if when is None """
        if when is None:
            return datetime.now()
        if not isinstance(when, datetime):
            raise TypeError("time must be a datetime")
        return when


    #############
    # Accessors #
    #############

    
    def get_name(self) -> str:
        """ get_name

            returns the dog's name as a string
        """
        return self._name
    

    def get_breed(self) -> str:
        """ get_breed

            returns the dog's breed as a string
        """
        return self._breed
    
    def get_gender(self) -> str:
        """ get_gender

            returns the dog's gender as a string
        """
        return self._gender
    
    def get_weight(self) -> float:
        """ get_weight

            return the dog's weight in lbs
        """
        return self._weight

    def get_colour(self) -> str:
        """ get_colour

            return the dog's colour as a description
        """
        return self._colour
    
    def get_potential_health_issues(self) -> list[str]:
        """ return a copy of the dog's known potential health issues """
        return list(self._potential_health_issues)

    def get_age(self) -> int:
        """ return the dog's age in years (relative to CURRENT_YEAR) """
        return Dog.CURRENT_YEAR - self._birth_year
    
    def get_most_recent_walk_time(self):
        """ return the datetime of the last walk, or None if never walked """
        return self._most_recent_walk_time

    def get_most_recent_meal_time(self):
        """ return the datetime of the last meal, or None if never fed """
        return self._most_recent_meal_time

    def get_max_time_between_walks(self) -> timedelta:
        """ return the longest the dog should go between walks """
        return self._max_time_between_walks

    def get_typical_time_between_meals(self) -> timedelta:
        """ return the typical time between meals """
        return self._typical_time_between_meals

    def needs_walk(self, now: datetime = None) -> bool:
        """ return True if the dog needs a walk, False otherwise

            now  optional current time (defaults to datetime.now(); useful for testing)
            A dog that has never been walked needs a walk.
        """
        now = Dog._resolve_time(now)
        if self._most_recent_walk_time is None:
            return True
        return now - self._most_recent_walk_time >= self._max_time_between_walks

    def needs_meal(self, now: datetime = None) -> bool:
        """ return True if the dog needs a meal, False otherwise

            now  optional current time (defaults to datetime.now(); useful for testing)
            A dog that has never been fed needs a meal.
        """
        now = Dog._resolve_time(now)
        if self._most_recent_meal_time is None:
            return True
        return now - self._most_recent_meal_time >= self._typical_time_between_meals


    ############
    # Mutators #
    ############


    def set_name(self, new_name: str):
        """ new_name    the dog's new name (non-empty string) """
        Dog._check_text(new_name, "name")
        self._name = new_name
    
    def set_weight(self, new_weight: float):
        """ new_weight  the new measured weight of the dog (in lbs), 0 < w <= MAX_WEIGHT """
        Dog._check_weight(new_weight)
        self._weight = float(new_weight)
    
    def add_potential_health_issue(self, health_issue: str):
        """ add a health issue (non-empty string); exact duplicates are ignored """
        Dog._check_text(health_issue, "health issue")
        if health_issue not in self._potential_health_issues:
            self._potential_health_issues.append(health_issue)

    def record_walk(self, when: datetime = None):
        """ record a walk at time `when` (defaults to now) """
        self._most_recent_walk_time = Dog._resolve_time(when)

    def record_meal(self, when: datetime = None):
        """ record a meal at time `when` (defaults to now) """
        self._most_recent_meal_time = Dog._resolve_time(when)

    def set_max_time_between_walks(self, duration: timedelta):
        """ set the longest allowed time between walks (positive timedelta) """
        Dog._check_duration(duration, "max time between walks")
        self._max_time_between_walks = duration

    def set_typical_time_between_meals(self, duration: timedelta):
        """ set the typical time between meals (positive timedelta) """
        Dog._check_duration(duration, "typical time between meals")
        self._typical_time_between_meals = duration

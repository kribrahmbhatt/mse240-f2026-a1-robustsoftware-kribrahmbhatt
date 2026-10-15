# Dog.py
#
# Author: Oliver Schneider 
# Email: oliver.schneider@uwaterloo.ca
# Student ID: 1234567890 
# 
# Source code for the Dog class.

class Dog:
    """ Dog
        A class representing an individual dog.
    """

    MAX_WEIGHT = 500.0 # maximum weight in lbs

    def __init__(self, name : str, breed : str, gender : str, initial_weight : float, 
                 colour: str, potential_health_issues : list[str], birth_year: int):
        """ Dog constructor

            name    the dog's given name
            breed   the dog's breed
            gender  the dog's gender
            initial_weight  the dog's initial weight (lbs)
            colour  a description of the dog's colour
            potential_health_issues a list of known potential health issues (each a string)
            birth_year  the year the dog was born
        """
        # check for type errors
        if type(name) is not str:
            raise TypeError("Name must be a string")
        
        if type(initial_weight) is not float:
            raise TypeError("initial_weight must be a float")


        # check for value errors
        if name == "":
            raise ValueError("Name cannot be empty")
        if initial_weight > Dog.MAX_WEIGHT:
            raise ValueError("Weight must be <= MAX_WEIGHT")

        


        # initialize private fields
        self._name = name
        self._breed = breed
        self._gender = gender
        self._weight = initial_weight
        self._colour = colour
        self._potential_health_issues = potential_health_issues
        self._birth_year = birth_year
        self._most_recent_walk_time = None
        self._most_recent_meal_time = None
        self._max_time_between_walks = None
        self._typical_time_between_meals = None



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
        """ get_potential_health_issues

            return the dog's known potential_health_issues as a list
        """
        return self._potential_health_issues
    
    def get_age(self) -> int:
        """ get_age

            return the dog's age
        """
        # assume that the year will always be 2026
        return 2026 - self._birth_year

    def needs_walk(self) -> bool:
        """ needs_walk

            return True if the dog needs a walk, False otherwise
        """
        #stub
        pass

    def needs_meal(self) -> bool:
        """ needs_meal

            return True if the dog needs a meal, False otherwise
        """
        #stub
        pass


    ############
    # Mutators #
    ############


    def set_name(self, new_name : str):
        """ set_name

            new_name    the dog's new name
        """
        #stub
        pass
    
    def set_weight(self, new_weight : float):
        """ set_weight

            new_weight  the new measured weight of the dog (in lbs)
        """
        #stub
        pass
    
    def add_potential_health_issue(self, health_issue : str):
        """ add_potential_health_issues

            add a health issue to the potential health issues
        """
        #stub
        pass


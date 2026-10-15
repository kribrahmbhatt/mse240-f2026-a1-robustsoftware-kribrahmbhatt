import unittest
from datetime import datetime, timedelta
from ..dog.Dog import Dog

NOW = datetime(2026, 10, 14, 12, 0, 0)


class TestDog(unittest.TestCase):
    """ TestDog

        Unit tests for the Dog class
    """

    def setUp(self):
        """ set up typical examples for each test """
        self._waffle = Dog("Waffle", "Newfoundland", "Male", 130, "Black",
                           ["geriatric hips"], 2018)
        self._george = Dog("George", "Goldendoodle", "Male", 145, "Brown",
                           [], 2020)

    def _make(self, **overrides):
        """ build a valid Dog, replacing any fields given as keyword overrides """
        args = dict(name="Waffle", breed="Newfoundland", gender="Male",
                    initial_weight=130.0, colour="Black",
                    potential_health_issues=["geriatric hips"], birth_year=2018)
        args.update(overrides)
        return Dog(**args)

    #
    # Constructor tests
    #

    def test_constructor_typical1(self):
        dog = self._waffle
        self.assertEqual("Waffle", dog.get_name())
        self.assertEqual("Newfoundland", dog.get_breed())
        self.assertEqual("Male", dog.get_gender())
        self.assertAlmostEqual(130, dog.get_weight())
        self.assertEqual("Black", dog.get_colour())
        self.assertEqual(["geriatric hips"], dog.get_potential_health_issues())
        self.assertEqual(8, dog.get_age())

    def test_constructor_typical2(self):
        dog = self._george
        self.assertEqual("George", dog.get_name())
        self.assertEqual("Goldendoodle", dog.get_breed())
        self.assertEqual("male", dog.get_gender().lower())
        self.assertAlmostEqual(145, dog.get_weight())
        self.assertEqual("Brown", dog.get_colour())
        self.assertEqual([], dog.get_potential_health_issues())
        self.assertEqual(6, dog.get_age())

    def test_constructor_int_weight_stored_as_float(self):
        self.assertIsInstance(self._waffle.get_weight(), float)
        self.assertEqual(130.0, self._waffle.get_weight())

    def test_constructor_valueerror_emptyname(self):
        with self.assertRaises(ValueError):
            self._make(name="")

    def test_constructor_valueerror_whitespacename(self):
        with self.assertRaises(ValueError):
            self._make(name="   ")
        with self.assertRaises(ValueError):
            self._make(name="\t")

    def test_constructor_typeerror_numericname(self):
        for bad in (3, 3.2, -8):
            with self.assertRaises(TypeError):
                self._make(name=bad)

    def test_constructor_typeerror_nonename(self):
        with self.assertRaises(TypeError):
            self._make(name=None)
        with self.assertRaises(TypeError):
            self._make(name=["Waffle"])

    def test_constructor_valueerror_negativeweight(self):
        with self.assertRaises(ValueError):
            self._make(initial_weight=-130)
        with self.assertRaises(ValueError):
            self._make(initial_weight=-0.01)

    def test_constructor_valueerror_zeroweight(self):
        with self.assertRaises(ValueError):
            self._make(initial_weight=0)
        with self.assertRaises(ValueError):
            self._make(initial_weight=0.0)

    def test_constructor_valueerror_maxweight(self):
        with self.assertRaises(ValueError):
            self._make(initial_weight=750)
        with self.assertRaises(ValueError):
            self._make(initial_weight=500.1)

    def test_constructor_max_weight_boundary_ok(self):
        dog = self._make(initial_weight=500)
        self.assertEqual(Dog.MAX_WEIGHT, dog.get_weight())
        self.assertEqual("Waffle", dog.get_name())

    def test_constructor_typeerror_weight(self):
        with self.assertRaises(TypeError):
            self._make(initial_weight="500")
        with self.assertRaises(TypeError):
            self._make(initial_weight=[1, 2, 3])
        with self.assertRaises(TypeError):
            self._make(initial_weight=None)

    def test_constructor_typeerror_boolweight(self):
        with self.assertRaises(TypeError):
            self._make(initial_weight=True)

    def test_constructor_typeerror_breed(self):
        with self.assertRaises(TypeError):
            self._make(breed=5)
        with self.assertRaises(TypeError):
            self._make(breed=None)

    def test_constructor_valueerror_emptybreed(self):
        with self.assertRaises(ValueError):
            self._make(breed="")

    def test_constructor_typeerror_gender(self):
        with self.assertRaises(TypeError):
            self._make(gender=1)
        with self.assertRaises(TypeError):
            self._make(gender=None)

    def test_constructor_valueerror_emptygender(self):
        with self.assertRaises(ValueError):
            self._make(gender="")

    def test_constructor_typeerror_colour(self):
        with self.assertRaises(TypeError):
            self._make(colour=0xFFFFFF)
        with self.assertRaises(TypeError):
            self._make(colour=None)

    def test_constructor_valueerror_emptycolour(self):
        with self.assertRaises(ValueError):
            self._make(colour="")

    def test_constructor_typeerror_issues_not_list(self):
        with self.assertRaises(TypeError):
            self._make(potential_health_issues="hips")
        with self.assertRaises(TypeError):
            self._make(potential_health_issues=None)

    def test_constructor_typeerror_issue_not_string(self):
        with self.assertRaises(TypeError):
            self._make(potential_health_issues=["hips", 5])

    def test_constructor_valueerror_issue_empty(self):
        with self.assertRaises(ValueError):
            self._make(potential_health_issues=["hips", ""])

    def test_constructor_copies_issue_list(self):
        issues = ["hips"]
        dog = self._make(potential_health_issues=issues)
        issues.append("eyes")
        self.assertEqual(["hips"], dog.get_potential_health_issues())
        self.assertEqual(["hips", "eyes"], issues)

    def test_constructor_typeerror_birth_year(self):
        with self.assertRaises(TypeError):
            self._make(birth_year="2018")
        with self.assertRaises(TypeError):
            self._make(birth_year=2018.5)

    def test_constructor_typeerror_bool_birth_year(self):
        with self.assertRaises(TypeError):
            self._make(birth_year=True)

    def test_constructor_valueerror_future_birth_year(self):
        with self.assertRaises(ValueError):
            self._make(birth_year=2027)
        with self.assertRaises(ValueError):
            self._make(birth_year=3000)

    def test_constructor_valueerror_too_old_birth_year(self):
        with self.assertRaises(ValueError):
            self._make(birth_year=1995)
        with self.assertRaises(ValueError):
            self._make(birth_year=-5)

    def test_constructor_birth_year_current_ok(self):
        dog = self._make(birth_year=2026)
        self.assertEqual(0, dog.get_age())

    def test_constructor_birth_year_min_ok(self):
        dog = self._make(birth_year=1996)
        self.assertEqual(30, dog.get_age())

    def test_class_constants(self):
        self.assertEqual(500.0, Dog.MAX_WEIGHT)
        self.assertEqual(2026, Dog.CURRENT_YEAR)
        self.assertLess(Dog.MIN_BIRTH_YEAR, Dog.CURRENT_YEAR)

    #
    # Accessors
    #

    def test_get_name_typical1(self):
        self.assertEqual("Waffle", self._waffle.get_name())

    def test_get_name_typical2(self):
        self.assertEqual("George", self._george.get_name())

    def test_get_breed_typical1(self):
        self.assertEqual("Newfoundland", self._waffle.get_breed())

    def test_get_breed_typical2(self):
        self.assertEqual("Goldendoodle", self._george.get_breed())

    def test_get_gender_typical1(self):
        self.assertEqual("Male", self._waffle.get_gender())

    def test_get_gender_typical2(self):
        self.assertEqual("Female", self._make(gender="Female").get_gender())
        self.assertEqual("Male", self._george.get_gender())

    def test_get_weight_typical1(self):
        self.assertAlmostEqual(130, self._waffle.get_weight())

    def test_get_weight_typical2(self):
        self.assertAlmostEqual(145, self._george.get_weight())
        self.assertAlmostEqual(12.5, self._make(initial_weight=12.5).get_weight())

    def test_get_colour_typical1(self):
        self.assertEqual("Black", self._waffle.get_colour())

    def test_get_colour_typical2(self):
        self.assertEqual("Brown", self._george.get_colour())

    def test_get_issues_typical(self):
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())

    def test_get_issues_empty(self):
        self.assertEqual([], self._george.get_potential_health_issues())
        self.assertIsInstance(self._george.get_potential_health_issues(), list)

    def test_get_issues_returns_copy(self):
        issues = self._waffle.get_potential_health_issues()
        issues.append("tampered")
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())
        self.assertEqual(2, len(issues))

    def test_get_age_typical(self):
        self.assertEqual(8, self._waffle.get_age())
        self.assertEqual(6, self._george.get_age())

    def test_get_age_puppy(self):
        self.assertEqual(1, self._make(birth_year=2025).get_age())
        self.assertEqual(0, self._make(birth_year=2026).get_age())

    def test_get_age_not_mutated_by_other_calls(self):
        self._waffle.set_weight(100)
        self._waffle.set_name("Wafflez")
        self.assertEqual(8, self._waffle.get_age())

    #
    # set_name
    #

    def test_set_name_typical(self):
        self.assertEqual("Waffle", self._waffle.get_name())
        self._waffle.set_name("Maple")
        self.assertEqual("Maple", self._waffle.get_name())

    def test_set_name_other_fields_unchanged(self):
        self._waffle.set_name("Maple")
        self.assertEqual("Newfoundland", self._waffle.get_breed())
        self.assertEqual("Male", self._waffle.get_gender())
        self.assertAlmostEqual(130, self._waffle.get_weight())
        self.assertEqual("Black", self._waffle.get_colour())
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())
        self.assertEqual(8, self._waffle.get_age())

    def test_set_name_typeerror(self):
        for bad in (3, 3.2, None, ["x"]):
            with self.assertRaises(TypeError):
                self._waffle.set_name(bad)

    def test_set_name_valueerror_empty(self):
        with self.assertRaises(ValueError):
            self._waffle.set_name("")
        with self.assertRaises(ValueError):
            self._waffle.set_name("  ")

    def test_set_name_invalid_leaves_name(self):
        with self.assertRaises(ValueError):
            self._waffle.set_name("")
        self.assertEqual("Waffle", self._waffle.get_name())
        with self.assertRaises(TypeError):
            self._waffle.set_name(7)
        self.assertEqual("Waffle", self._waffle.get_name())

    def test_set_name_same_name_ok(self):
        self._waffle.set_name("Waffle")
        self.assertEqual("Waffle", self._waffle.get_name())

    def test_set_name_does_not_affect_other_dog(self):
        self._waffle.set_name("Maple")
        self.assertEqual("George", self._george.get_name())
        self.assertEqual("Maple", self._waffle.get_name())
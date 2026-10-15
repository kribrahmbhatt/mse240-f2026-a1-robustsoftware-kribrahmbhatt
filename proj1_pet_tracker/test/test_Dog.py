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

    #
    # set_weight
    #

    def test_set_weight_typical(self):
        self.assertAlmostEqual(130, self._waffle.get_weight())
        self._waffle.set_weight(135.5)
        self.assertAlmostEqual(135.5, self._waffle.get_weight())

    def test_set_weight_int_stored_as_float(self):
        self._waffle.set_weight(120)
        self.assertIsInstance(self._waffle.get_weight(), float)
        self.assertEqual(120.0, self._waffle.get_weight())

    def test_set_weight_other_fields_unchanged(self):
        self._waffle.set_weight(120)
        self.assertEqual("Waffle", self._waffle.get_name())
        self.assertEqual("Newfoundland", self._waffle.get_breed())
        self.assertEqual("Male", self._waffle.get_gender())
        self.assertEqual("Black", self._waffle.get_colour())
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())
        self.assertEqual(8, self._waffle.get_age())

    def test_set_weight_valueerror_negative(self):
        with self.assertRaises(ValueError):
            self._waffle.set_weight(-1)
        with self.assertRaises(ValueError):
            self._waffle.set_weight(-0.001)

    def test_set_weight_valueerror_zero(self):
        with self.assertRaises(ValueError):
            self._waffle.set_weight(0)

    def test_set_weight_valueerror_over_max(self):
        with self.assertRaises(ValueError):
            self._waffle.set_weight(500.1)
        with self.assertRaises(ValueError):
            self._waffle.set_weight(10000)

    def test_set_weight_max_boundary_ok(self):
        self._waffle.set_weight(Dog.MAX_WEIGHT)
        self.assertEqual(Dog.MAX_WEIGHT, self._waffle.get_weight())

    def test_set_weight_typeerror(self):
        for bad in ("130", None, [130], True):
            with self.assertRaises(TypeError):
                self._waffle.set_weight(bad)

    def test_set_weight_invalid_leaves_weight(self):
        with self.assertRaises(ValueError):
            self._waffle.set_weight(-5)
        self.assertAlmostEqual(130, self._waffle.get_weight())
        with self.assertRaises(TypeError):
            self._waffle.set_weight("heavy")
        self.assertAlmostEqual(130, self._waffle.get_weight())

    def test_set_weight_can_be_called_repeatedly(self):
        self._waffle.set_weight(131)
        self._waffle.set_weight(129)
        self.assertAlmostEqual(129, self._waffle.get_weight())

    #
    # add_potential_health_issue
    #

    def test_add_issue_typical(self):
        self._george.add_potential_health_issue("allergies")
        self.assertEqual(["allergies"], self._george.get_potential_health_issues())

    def test_add_issue_appends_to_existing(self):
        self._waffle.add_potential_health_issue("bloat")
        self.assertEqual(["geriatric hips", "bloat"], self._waffle.get_potential_health_issues())

    def test_add_issue_preserves_order(self):
        for issue in ("a", "b", "c"):
            self._george.add_potential_health_issue(issue)
        self.assertEqual(["a", "b", "c"], self._george.get_potential_health_issues())

    def test_add_issue_typeerror(self):
        for bad in (5, None, ["x"]):
            with self.assertRaises(TypeError):
                self._george.add_potential_health_issue(bad)
        self.assertEqual([], self._george.get_potential_health_issues())

    def test_add_issue_valueerror_empty(self):
        with self.assertRaises(ValueError):
            self._george.add_potential_health_issue("")
        with self.assertRaises(ValueError):
            self._george.add_potential_health_issue("   ")
        self.assertEqual([], self._george.get_potential_health_issues())

    def test_add_issue_duplicate_ignored(self):
        self._waffle.add_potential_health_issue("geriatric hips")
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())

    def test_add_issue_other_fields_unchanged(self):
        self._george.add_potential_health_issue("allergies")
        self.assertEqual("George", self._george.get_name())
        self.assertAlmostEqual(145, self._george.get_weight())
        self.assertEqual("Brown", self._george.get_colour())
        self.assertEqual(6, self._george.get_age())

    def test_add_issue_does_not_affect_other_dog(self):
        self._george.add_potential_health_issue("allergies")
        self.assertEqual(["geriatric hips"], self._waffle.get_potential_health_issues())

    def test_add_issue_does_not_modify_constructor_list(self):
        issues = ["hips"]
        dog = self._make(potential_health_issues=issues)
        dog.add_potential_health_issue("eyes")
        self.assertEqual(["hips"], issues)
        self.assertEqual(["hips", "eyes"], dog.get_potential_health_issues())

    #
    # record_walk / record_meal
    #

    def test_record_walk_typical(self):
        self._waffle.record_walk(NOW)
        self.assertEqual(NOW, self._waffle.get_most_recent_walk_time())

    def test_record_walk_default_is_now(self):
        before = datetime.now()
        self._waffle.record_walk()
        after = datetime.now()
        self.assertGreaterEqual(self._waffle.get_most_recent_walk_time(), before)
        self.assertLessEqual(self._waffle.get_most_recent_walk_time(), after)

    def test_record_walk_typeerror(self):
        with self.assertRaises(TypeError):
            self._waffle.record_walk("noon")
        with self.assertRaises(TypeError):
            self._waffle.record_walk(12)
        self.assertIsNone(self._waffle.get_most_recent_walk_time())

    def test_record_walk_does_not_touch_meal(self):
        self._waffle.record_walk(NOW)
        self.assertIsNone(self._waffle.get_most_recent_meal_time())
        self.assertEqual("Waffle", self._waffle.get_name())

    def test_record_walk_latest_replaces_previous(self):
        self._waffle.record_walk(NOW)
        self._waffle.record_walk(NOW + timedelta(hours=1))
        self.assertEqual(NOW + timedelta(hours=1), self._waffle.get_most_recent_walk_time())

    def test_record_meal_typical(self):
        self._waffle.record_meal(NOW)
        self.assertEqual(NOW, self._waffle.get_most_recent_meal_time())

    def test_record_meal_default_is_now(self):
        before = datetime.now()
        self._waffle.record_meal()
        after = datetime.now()
        self.assertGreaterEqual(self._waffle.get_most_recent_meal_time(), before)
        self.assertLessEqual(self._waffle.get_most_recent_meal_time(), after)

    def test_record_meal_typeerror(self):
        with self.assertRaises(TypeError):
            self._waffle.record_meal("noon")
        with self.assertRaises(TypeError):
            self._waffle.record_meal(None.__class__)
        self.assertIsNone(self._waffle.get_most_recent_meal_time())

    def test_record_meal_does_not_touch_walk(self):
        self._waffle.record_meal(NOW)
        self.assertIsNone(self._waffle.get_most_recent_walk_time())
        self.assertAlmostEqual(130, self._waffle.get_weight())

    def test_record_meal_latest_replaces_previous(self):
        self._waffle.record_meal(NOW)
        self._waffle.record_meal(NOW + timedelta(hours=5))
        self.assertEqual(NOW + timedelta(hours=5), self._waffle.get_most_recent_meal_time())

    def test_constructor_initial_care_state(self):
        dog = self._waffle
        self.assertIsNone(dog.get_most_recent_walk_time())
        self.assertIsNone(dog.get_most_recent_meal_time())
        self.assertEqual(Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS, dog.get_max_time_between_walks())
        self.assertEqual(Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS, dog.get_typical_time_between_meals())

    #
    # set_max_time_between_walks / set_typical_time_between_meals
    #

    def test_set_max_walk_time_typical(self):
        self._waffle.set_max_time_between_walks(timedelta(hours=4))
        self.assertEqual(timedelta(hours=4), self._waffle.get_max_time_between_walks())
        self.assertEqual(Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS,
                         self._waffle.get_typical_time_between_meals())

    def test_set_max_walk_time_typeerror(self):
        for bad in (4, "4 hours", None, 4.5):
            with self.assertRaises(TypeError):
                self._waffle.set_max_time_between_walks(bad)

    def test_set_max_walk_time_valueerror_zero(self):
        with self.assertRaises(ValueError):
            self._waffle.set_max_time_between_walks(timedelta(0))

    def test_set_max_walk_time_valueerror_negative(self):
        with self.assertRaises(ValueError):
            self._waffle.set_max_time_between_walks(timedelta(hours=-1))

    def test_set_max_walk_time_invalid_leaves_value(self):
        with self.assertRaises(ValueError):
            self._waffle.set_max_time_between_walks(timedelta(0))
        self.assertEqual(Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS, self._waffle.get_max_time_between_walks())
        with self.assertRaises(TypeError):
            self._waffle.set_max_time_between_walks(3)
        self.assertEqual(Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS, self._waffle.get_max_time_between_walks())

    def test_set_meal_time_typical(self):
        self._waffle.set_typical_time_between_meals(timedelta(hours=6))
        self.assertEqual(timedelta(hours=6), self._waffle.get_typical_time_between_meals())
        self.assertEqual(Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS, self._waffle.get_max_time_between_walks())

    def test_set_meal_time_typeerror(self):
        for bad in (6, "6 hours", None, 6.5):
            with self.assertRaises(TypeError):
                self._waffle.set_typical_time_between_meals(bad)

    def test_set_meal_time_valueerror_zero(self):
        with self.assertRaises(ValueError):
            self._waffle.set_typical_time_between_meals(timedelta(0))

    def test_set_meal_time_valueerror_negative(self):
        with self.assertRaises(ValueError):
            self._waffle.set_typical_time_between_meals(timedelta(minutes=-1))

    def test_set_meal_time_invalid_leaves_value(self):
        with self.assertRaises(ValueError):
            self._waffle.set_typical_time_between_meals(timedelta(0))
        self.assertEqual(Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS,
                         self._waffle.get_typical_time_between_meals())
        with self.assertRaises(TypeError):
            self._waffle.set_typical_time_between_meals("soon")
        self.assertEqual(Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS,
                         self._waffle.get_typical_time_between_meals())

        #
    # needs_walk
    #

    def test_needs_walk_never_walked(self):
        self.assertTrue(self._waffle.needs_walk(NOW))
        self.assertIsNone(self._waffle.get_most_recent_walk_time())

    def test_needs_walk_just_walked(self):
        self._waffle.record_walk(NOW)
        self.assertFalse(self._waffle.needs_walk(NOW))

    def test_needs_walk_before_threshold(self):
        self._waffle.record_walk(NOW)
        self.assertFalse(self._waffle.needs_walk(NOW + timedelta(hours=7, minutes=59)))

    def test_needs_walk_exactly_at_threshold(self):
        self._waffle.record_walk(NOW)
        self.assertTrue(self._waffle.needs_walk(NOW + Dog.DEFAULT_MAX_TIME_BETWEEN_WALKS))

    def test_needs_walk_after_threshold(self):
        self._waffle.record_walk(NOW)
        self.assertTrue(self._waffle.needs_walk(NOW + timedelta(hours=20)))

    def test_needs_walk_custom_max(self):
        self._waffle.record_walk(NOW)
        self._waffle.set_max_time_between_walks(timedelta(hours=2))
        self.assertFalse(self._waffle.needs_walk(NOW + timedelta(hours=1)))
        self.assertTrue(self._waffle.needs_walk(NOW + timedelta(hours=2)))

    def test_needs_walk_changing_max_changes_answer(self):
        self._waffle.record_walk(NOW)
        later = NOW + timedelta(hours=5)
        self.assertFalse(self._waffle.needs_walk(later))
        self._waffle.set_max_time_between_walks(timedelta(hours=3))
        self.assertTrue(self._waffle.needs_walk(later))

    def test_needs_walk_meal_does_not_matter(self):
        self._waffle.record_meal(NOW)
        self.assertTrue(self._waffle.needs_walk(NOW))
        self._waffle.record_walk(NOW)
        self.assertFalse(self._waffle.needs_walk(NOW))

    def test_needs_walk_default_now(self):
        self.assertTrue(self._waffle.needs_walk())
        self._waffle.record_walk()
        self.assertFalse(self._waffle.needs_walk())

    def test_needs_walk_typeerror_now(self):
        with self.assertRaises(TypeError):
            self._waffle.needs_walk("now")
        with self.assertRaises(TypeError):
            self._waffle.needs_walk(5)

    def test_needs_walk_independent_per_dog(self):
        self._waffle.record_walk(NOW)
        self.assertFalse(self._waffle.needs_walk(NOW))
        self.assertTrue(self._george.needs_walk(NOW))

    #
    # needs_meal
    #

    def test_needs_meal_never_fed(self):
        self.assertTrue(self._waffle.needs_meal(NOW))
        self.assertIsNone(self._waffle.get_most_recent_meal_time())

    def test_needs_meal_just_fed(self):
        self._waffle.record_meal(NOW)
        self.assertFalse(self._waffle.needs_meal(NOW))

    def test_needs_meal_before_threshold(self):
        self._waffle.record_meal(NOW)
        self.assertFalse(self._waffle.needs_meal(NOW + timedelta(hours=11, minutes=59)))

    def test_needs_meal_exactly_at_threshold(self):
        self._waffle.record_meal(NOW)
        self.assertTrue(self._waffle.needs_meal(NOW + Dog.DEFAULT_TYPICAL_TIME_BETWEEN_MEALS))

    def test_needs_meal_after_threshold(self):
        self._waffle.record_meal(NOW)
        self.assertTrue(self._waffle.needs_meal(NOW + timedelta(days=2)))

    def test_needs_meal_custom_interval(self):
        self._waffle.record_meal(NOW)
        self._waffle.set_typical_time_between_meals(timedelta(hours=4))
        self.assertFalse(self._waffle.needs_meal(NOW + timedelta(hours=3)))
        self.assertTrue(self._waffle.needs_meal(NOW + timedelta(hours=4)))

    def test_needs_meal_walk_does_not_matter(self):
        self._waffle.record_walk(NOW)
        self.assertTrue(self._waffle.needs_meal(NOW))
        self._waffle.record_meal(NOW)
        self.assertFalse(self._waffle.needs_meal(NOW))

    def test_needs_meal_default_now(self):
        self.assertTrue(self._waffle.needs_meal())
        self._waffle.record_meal()
        self.assertFalse(self._waffle.needs_meal())

    def test_needs_meal_typeerror_now(self):
        with self.assertRaises(TypeError):
            self._waffle.needs_meal("now")
        with self.assertRaises(TypeError):
            self._waffle.needs_meal(5)

    def test_needs_meal_independent_per_dog(self):
        self._george.record_meal(NOW)
        self.assertFalse(self._george.needs_meal(NOW))
        self.assertTrue(self._waffle.needs_meal(NOW))


        
# Dog class specification and test plan

## Fields and allowed values
| Field | Type | Rule |

| name, breed, gender, colour | str | non-empty (not just whitespace) |

| weight | int or float (bool rejected) | 0 < weight <= 500 lbs; stored as float |

| potential health issues | list[str] | each item a non-empty str; list is copied |

| birth year | int (bool rejected) | 1996 <= year <= 2026 |

| max time between walks | timedelta | > 0, default 8 hours |

| typical time between meals | timedelta | > 0, default 12 hours |

Wrong type -> `TypeError`. Right type, bad value -> `ValueError`.

## Methods
- Accessors: `get_name/breed/gender/weight/colour/potential_health_issues/age`, plus walk/meal time getters.
  `get_potential_health_issues` returns a copy. `get_age` = 2026 - birth year.
- `set_name`, `set_weight`, `add_potential_health_issue` validate like the constructor.
  A failed call leaves the object unchanged. Exact duplicate issues are ignored.
- `record_walk(when=None)`, `record_meal(when=None)`: `when` is a datetime (default now).
- `set_max_time_between_walks`, `set_typical_time_between_meals`: positive timedelta.
- `needs_walk(now=None)`, `needs_meal(now=None)`: True if never done, or if elapsed time >= the interval.

## Test plan
For every method: typical cases, boundaries (weight 500 vs 500.1, weight 0, birth year 2026/1996/1995/2027,
elapsed time exactly equal to the interval), wrong types, empty values, "failed call leaves state unchanged",
and "other fields unchanged".
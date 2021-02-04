from time_manager import _mins_from_bound, get_next_lesson

assert _mins_from_bound("8:17") == 8 * 60 + 17
assert get_next_lesson(8, 0) == 1
assert get_next_lesson(8, 0) == 1
assert get_next_lesson(7, 29) == 0
assert get_next_lesson(12, 25) == 5
assert get_next_lesson(21, 36) == 0

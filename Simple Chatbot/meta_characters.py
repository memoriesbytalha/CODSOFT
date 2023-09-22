import re

# Example using .

pattern_dot = r'h.t'  # Matches "hat", "hot", "hit", etc.
result_dot = re.search(pattern_dot, "hat hot hit")
print(result_dot.group() if result_dot else "No match")

# Example using ^
pattern_start = r'^start'  # Matches "start of the line"
result_start = re.search(pattern_start, "start of the line")
print(result_start.group() if result_start else "No match")

# Example using $
pattern_end = r'end$'  # Matches "end of the line"
result_end = re.search(pattern_end, "end of the line")
print(result_end.group() if result_end else "No match")

# Example using *
pattern_zero_or_more = r'go*gle'  # Matches "ggle", "google", "gooogle", etc.
result_zero_or_more = re.search(pattern_zero_or_more, "ggle google gooogle")
print(result_zero_or_more.group() if result_zero_or_more else "No match")

# Example using +
pattern_one_or_more = r'go+gle'  # Matches "google", "gooogle", but not "ggle"
result_one_or_more = re.search(pattern_one_or_more, "ggle google gooogle")
print(result_one_or_more.group() if result_one_or_more else "No match")

# Example using ?
pattern_zero_or_one = r'colou?r'  # Matches "color" and "colour"
result_zero_or_one = re.search(pattern_zero_or_one, "color colour")
print(result_zero_or_one.group() if result_zero_or_one else "No match")

# Example using []
pattern_character_set = r'[aeiou]'  # Matches any vowel
result_character_set = re.search(pattern_character_set, "hello")
print(result_character_set.group() if result_character_set else "No match")

# Example using ()
pattern_grouping = r'(ab)+'  # Matches "ab", "abab", "ababab", etc.
result_grouping = re.search(pattern_grouping, "ab abab ababab")
print(result_grouping.group() if result_grouping else "No match")

# Example using \
pattern_escape = r'\.'  # Matches a literal period (dot)
result_escape = re.search(pattern_escape, "This is a sentence with a dot.")
print(result_escape.group() if result_escape else "No match")


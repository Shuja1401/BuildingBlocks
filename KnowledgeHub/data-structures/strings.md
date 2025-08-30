## STRINGS
These are sequence of characters enclosed inside quotes (' ', " ").

## CONCEPTS
- **Indexing:** Access individual characters using square brackets `[]`.  
- **Slicing:** Access a substring using `[start:end:step]`.  
- **Concatenation:** Combine strings with `+`.  
- **Repetition:** Repeat strings using `*`.  
- **Immutability:** Strings cannot be modified after creation; operations return new strings.

# Strings in Python

Strings are sequences of characters enclosed in quotes (`' '` or `" "`).  
They are **immutable**, meaning you cannot change a character in place once the string is created.

## Concepts
- **Indexing:** Access individual characters using square brackets `[]`.  
- **Slicing:** Access a substring using `[start:end:step]`.  
- **Concatenation:** Combine strings with `+`.  
- **Repetition:** Repeat strings using `*`.  
- **Immutability:** Strings cannot be modified after creation; operations return new strings.

## Common String Methods
| Method | Description | Example |
|--------|-------------|---------|
| `.lower()` | Convert all letters to lowercase | `"Hello".lower()` → `"hello"` |
| `.upper()` | Convert all letters to uppercase | `"Hello".upper()` → `"HELLO"` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace substring | `"hello".replace("l", "x")` → `"hexxo"` |
| `.split(sep)` | Split string into list by separator | `"a,b,c".split(",")` → `['a','b','c']` |
| `.join(iterable)` | Join iterable into string | `",".join(['a','b','c'])` → `"a,b,c"` |
| `.find(sub)` | Return index of first occurrence | `"hello".find("l")` → `2` |
| `.count(sub)` | Count occurrences | `"hello".count("l")` → `2` |
| `.startswith(prefix)` | Check if string starts with prefix | `"hello".startswith("he")` → `True` |
| `.endswith(suffix)` | Check if string ends with suffix | `"hello".endswith("lo")` → `True` |

### ✅ Complete List of String Methods in Python

1. `capitalize()` : Capitalizes the first character.
2. `casefold()` : Case-insensitive lowercase conversion (stronger than `.lower()`).
3. `center(width[, fillchar])` : Centers string in given width.
4. `count(sub[, start[, end]])` : Counts occurrences of substring.
5. `encode(encoding="utf-8", errors="strict")` : Returns encoded bytes.
6. `endswith(suffix[, start[, end]])` : Checks if string ends with suffix.
7. `expandtabs(tabsize=8)` : Replaces tabs with spaces.
8. `find(sub[, start[, end]])` : Finds lowest index of substring, or -1.
9. `format(*args, **kwargs)` : String formatting.
10. `format_map(mapping)` : Formatting with a mapping object.
11. `index(sub[, start[, end]])` : Like `.find()` but raises `ValueError` if not found.
12. `isalnum()` : True if all characters are alphanumeric.
13. `isalpha()` : True if all characters are alphabetic.
14. `isascii()` : True if all characters are ASCII.
15. `isdecimal()` : True if all characters are decimal digits.
16. `isdigit()` : True if all characters are digits.
17. `isidentifier()` : True if string is a valid Python identifier.
18. `islower()` : True if all cased characters are lowercase.
19. `isnumeric()` : True if all characters are numeric.
20. `isprintable()` : True if all characters are printable.
21. `isspace()` : True if all characters are whitespace.
22. `istitle()` : True if string is titlecased.
23. `isupper()` : True if all cased characters are uppercase.
24. `join(iterable)` : Concatenates iterable with string as separator.
25. `ljust(width[, fillchar])` : Left-justifies string.
26. `lower()` : Converts to lowercase.
27. `lstrip([chars])` : Removes leading whitespace/characters.
28. `maketrans(x, y[, z])` : Returns a translation table for `.translate()`.
29. `partition(sep)` : Splits into 3 parts: before sep, sep, after sep.
30. `removeprefix(prefix)` : Removes prefix if present.
31. `removesuffix(suffix)` : Removes suffix if present.
32. `replace(old, new[, count])` : Replaces occurrences of substring.
33. `rfind(sub[, start[, end]])` : Finds highest index of substring, or -1.
34. `rindex(sub[, start[, end]])` : Like `.rfind()` but raises error if not found.
35. `rjust(width[, fillchar])` : Right-justifies string.
36. `rpartition(sep)` : Like `.partition()` but from the right.
37. `rsplit(sep=None, maxsplit=-1)` : Splits from the right.
38. `rstrip([chars])` : Removes trailing whitespace/characters.
39. `split(sep=None, maxsplit=-1)` : Splits string into list.
40. `splitlines([keepends])` : Splits at line breaks.
41. `startswith(prefix[, start[, end]])` : Checks if string starts with prefix.
42. `strip([chars])` : Removes leading & trailing whitespace/characters.
43. `swapcase()` : Swaps case of all characters.
44. `title()` : Converts string to title case.
45. `translate(table)` : Maps characters using a translation table.
46. `upper()` : Converts to uppercase.
47. `zfill(width)` : Pads string with leading zeros.
joined = "-".join(words)
print(joined)        # 'Hello-World!'

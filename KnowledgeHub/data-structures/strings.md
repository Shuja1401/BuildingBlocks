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


joined = "-".join(words)
print(joined)        # 'Hello-World!'

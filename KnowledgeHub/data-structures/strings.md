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


# 🔹 47 Python String Methods by 8 Category

### **1. Case Conversion Methods**

* `capitalize()` : First character uppercase, rest lowercase.
* `casefold()` : Aggressive lowercase (for comparisons).
* `lower()` : Converts to lowercase.
* `upper()` : Converts to uppercase.
* `swapcase()` : Swaps uppercase ↔ lowercase.
* `title()` : Title case (Each Word Capitalized).

---

### **2. Search & Check Methods**

* `find(sub[, start[, end]])` : Lowest index, or `-1`.
* `rfind(sub[, start[, end]])` : Highest index, or `-1`.
* `index(sub[, start[, end]])` : Like `.find()`, but raises error if not found.
* `rindex(sub[, start[, end]])` : Like `.rfind()`, but raises error if not found.
* `startswith(prefix[, start[, end]])` : True if starts with prefix.
* `endswith(suffix[, start[, end]])` : True if ends with suffix.
* `count(sub[, start[, end]])` : Number of occurrences.

---

### **3. Validation / Boolean Checks**

(check the content of the string → return True/False)

* `isalnum()` : Alphanumeric only.
* `isalpha()` : Alphabetic only.
* `isascii()` : ASCII only.
* `isdecimal()` : Decimal numbers only.
* `isdigit()` : Digits only.
* `isnumeric()` : Numeric characters.
* `islower()` : Lowercase only.
* `isupper()` : Uppercase only.
* `istitle()` : Titlecase only.
* `isspace()` : Whitespace only.
* `isidentifier()` : Valid Python identifier?
* `isprintable()` : Printable characters only.

---

### **4. Whitespace & Cleanup**

* `strip([chars])` : Removes leading & trailing whitespace/characters.
* `lstrip([chars])` : Removes from left side only.
* `rstrip([chars])` : Removes from right side only.
* `removeprefix(prefix)` : Removes prefix if present.
* `removesuffix(suffix)` : Removes suffix if present.

---

### **5. Splitting & Joining**

* `split(sep=None, maxsplit=-1)` : Splits into list.
* `rsplit(sep=None, maxsplit=-1)` : Splits from right.
* `splitlines([keepends])` : Splits at line breaks.
* `partition(sep)` : Splits into 3 parts: before, sep, after.
* `rpartition(sep)` : Like `.partition()`, from the right.
* `join(iterable)` : Joins iterable into a string with separator.

---

### **6. Alignment & Padding**

* `center(width[, fillchar])` : Centers string.
* `ljust(width[, fillchar])` : Left-justifies.
* `rjust(width[, fillchar])` : Right-justifies.
* `zfill(width)` : Pads with leading zeros.

---

### **7. Replacement & Translation**

* `replace(old, new[, count])` : Replace substrings.
* `translate(table)` : Map characters via translation table.
* `maketrans(x, y[, z])` : Build translation table for `.translate()`.

---

### **8. Encoding & Special**

* `encode(encoding="utf-8", errors="strict")` : Encodes string to bytes.
* `expandtabs(tabsize=8)` : Replace `\t` with spaces.
* `format(*args, **kwargs)` : String formatting.
* `format_map(mapping)` : Formatting with dict-like mapping.




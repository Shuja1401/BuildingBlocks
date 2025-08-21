### 1. **`==` for dicts → compares keys and values (order doesn’t matter).**

In Python, the `==` operator checks if **two dictionaries have the same set of keys and matching values**.
Order of insertion doesn’t matter, only the content.

```python
a = {"name": "Alice", "age": 25}
b = {"age": 25, "name": "Alice"}

print(a == b)   # True ✅ (same keys and values, just different order)
```

So `==` looks at **dictionary content**.

---

### 2. **`is` for dicts → checks if both variables point to the same object in memory.**

The `is` operator checks **identity**, not content.
Two different dictionary objects can have the same content but still not be the *same* object in memory.

```python
a = {"name": "Alice"}
b = {"name": "Alice"}
c = a   # c points to the exact same object as a

print(a == b)  # True ✅ (contents match)
print(a is b)  # False ❌ (different objects in memory)
print(a is c)  # True ✅ (same object in memory)
```

So `is` looks at **object identity**.

---

### 3. **`.remove(x)` → uses `==` under the hood.**

When you call `.remove(x)` on a list, Python scans through the list and checks each element with `==`.

* If it finds a match, it removes the **first occurrence** and stops.
* It doesn’t care about identity (`is`).

```python
contacts = [{"name": "Alice"}, {"name": "Bob"}]

# new dictionary with same content as first element
to_remove = {"name": "Alice"}  

contacts.remove(to_remove)  # Works ✅ because == matches by content
print(contacts)  # [{'name': 'Bob'}]
```

But if you used `is` instead of `==`, it wouldn’t match here because the two `{"name": "Alice"}` objects are not the *same object in memory*.

---

⚡ In short:

* `==` → compares **values**.
* `is` → compares **memory identity**.
* `.remove(x)` → internally uses `==` to compare list items.


Example of using "==" and "is" in dictionary:

a = {"name": "Alice"}
b = {"name": "Alice"}
c = a   # c points to the same object as a

print("a == b:", a == b)   # ✅ True (same content)
print("a is b:", a is b)   # ❌ False (different memory addresses)

print("a == c:", a == c)   # ✅ True (same content)
print("a is c:", a is c)   # ✅ True (same memory address)

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))

Output: 

a == b: True
a is b: False
a == c: True
a is c: True
id(a): 140404444875776
id(b): 140404444878336
id(c): 140404444875776

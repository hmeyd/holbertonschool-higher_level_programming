# Python - Everything is Object

This repository is part of the **Holberton School Higher Level Programming** curriculum.

The goal of this project is to understand the concepts behind how Python handles objects, memory references, mutability, and object identity.

## 📚 Learning Objectives

By completing this project, you should be able to:

- Understand that **everything in Python is an object**
- Distinguish between **mutable and immutable types**
- Know how variables reference objects in memory
- Understand the difference between `is` and `==`
- Use the functions `type()` and `id()` to inspect Python objects

## 🧠 Topics Covered

- Object identity and value
- Reference and aliasing
- Object comparison (`is` vs `==`)
- Mutable vs immutable types
- Python memory model

## 📝 Files Description

Each question corresponds to a `.txt` file with the answer (no code unless explicitly requested):

| File             | Description                                         |
|------------------|-----------------------------------------------------|
| `0-answer.txt`   | Name of the function used to print object type      |
| `1-answer.txt`   | Function used to get object ID (memory address)     |
| `2-answer.txt`   | Do two variables point to the same object? (No)     |
| `3-answer.txt`   | Do two variables point to the same object? (Yes)    |
| `4-answer.txt`   | Do a and b refer to the same object? (Yes)          |
| `5-answer.txt`   | Do a and b refer to the same object? (No)           |
| ...              | ...                                                 |
| `14-answer.txt`  | Result of appending to a list referenced by another |
| `15-answer.txt`  | Result of list reassignment with `+` operator       |
| `16-answer.txt`  | Output after trying to increment an integer         |

## 🧪 How to Test

You can test your understanding by copying the code snippets into the Python shell or writing small test scripts like:

```python
a = 89
b = a
print(a is b)  # True

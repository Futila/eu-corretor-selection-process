# Eu Corretor Technical Challenges

Repository containing my solutions to the Eu Corretor selection process technical challenges.

## Exercise 1: Find First Non-Repeating Character in a String

### Problem Statement

Implement a function that finds the first character that does not repeat in a string. If all characters repeat, return -1.

### Solution

```python
def findFirstNonReapeatingCharacterInAString(input_string: str) -> int:
    """
    Finds the index of the first non-repeating character in a string.

    Args:
        input_string (str): The string to analyze (e.g., "abacabad")

    Returns:
        int: Index of first unique character or -1 if none exists
    """
    occurrencesOfEachCharacter = {}

    for char in input_string:
        occurrencesOfEachCharacter[char] = occurrencesOfEachCharacter.get(char, 0) + 1

    for i, char in enumerate(input_string):
        if occurrencesOfEachCharacter[char] == 1:
            return i

    return -1
```

### Approach

**Character Frequency Analysis**:

- Create a dictionary to count occurrences of each character

**Linear Scan**:

- Traverse the string to find the first character with count = 1

### Test Cases

```bash
print(findFirstNonReapeatingCharacterInAString("abacabad"))  # Output: 3 ('c')
print(findFirstNonReapeatingCharacterInAString("aaabb"))     # Output: -1
print(findFirstNonReapeatingCharacterInAString("abcdef"))    # Output: 0 ('a')
```

### How to Run

```bash
python exe1.py
```

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

## Exercise 2: Merge Intervals

### Problem Statement

Given a list of intervals represented as `[start, end]` pairs, merge all overlapping intervals and return a new list of non-overlapping intervals.

### Key Algorithm Steps

    Edge Case Handling: Immediate return if input is empty

    Sorting Phase:

        Sorts intervals by start value using key=lambda x: x[0]

        Critical for ensuring adjacent overlaps

    Merging Phase:

        Uses a greedy algorithm to merge intervals in single pass

        Only keeps track of the last merged interval for comparison

# Normal case with multiple merges

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

# Output: [[1, 6], [8, 10], [15, 18]]

# Edge case with adjacent intervals

print(merge_intervals([[1,4],[4,5]]))

# Output: [[1, 5]]

# No overlaps case

print(merge_intervals([[1,2],[3,4],[5,6]]))

# Output: [[1,2], [3,4], [5,6]]

# Single interval case

print(merge_intervals([[1,3]]))

# Output: [[1,3]]

### How to Run

```bash
python exe2.py
```

## Exercise 3: Word Ladder (Escada de Palavras)

### Problem Statement

Find the length of the shortest transformation sequence from `initialWord` to `finalWord` where:

1. Only one letter can be changed at a time
2. Each intermediate word must exist in `wordList`
3. Return 0 if no such sequence exists

### Test Cases

```bash
# Standard case (path exists)
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: 5 ("hit"→"hot"→"dot"→"dog"→"cog")

# No possible path
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
# Output: 0

# Immediate transformation
print(ladderLength("hot", "dot", ["dot","cot"]))
# Output: 2 ("hot"→"dot")

# Same start and end word
print(ladderLength("hot", "hot", ["hot"]))
# Output: 1

```

### How to Run

```bash
python exe3.py
```

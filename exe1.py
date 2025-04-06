def findFirstNonReapeatingCharacterInAString(input_string: str) -> int: 

  occurrencesOfEachCharacter = {}

  for char in input_string: 
    occurrencesOfEachCharacter[char] = occurrencesOfEachCharacter.get(char, 0) + 1 

  
  for i, char in enumerate(input_string):
    if occurrencesOfEachCharacter[char] == 1:
      return i
    
  return -1


#For testing purposes
print(findFirstNonReapeatingCharacterInAString("abacabad")) #The output must be: 3 ("c")
print(findFirstNonReapeatingCharacterInAString("aaabb")) #The output must be: 1  (não há caracteres não repetidos)
print(findFirstNonReapeatingCharacterInAString("abcdef")) #The output must be: 0 ("a")
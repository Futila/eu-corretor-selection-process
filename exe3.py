from collections import deque

def ladderLength(initialWord: str, finalWord: str, wordList: list) -> int:
  
    if finalWord not in wordList:
        return 0
    
    wordSet = set(wordList)
    queue = deque([(initialWord, 1)])
    
    while queue:
        current_word, level = queue.popleft()
        
        if current_word == finalWord:
            return level
            
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, level + 1))
    
    return 0


#For testing purposes
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # Output: 5
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) # Output: 0


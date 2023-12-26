# exercise 14:
#Write a function clean_anagrams(words) that returns a list of words cleaned from anagrams

def is_anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    if len(word1) != len(word2): 
        return False
    for i in range(len(word1)):
        if word1[i] in word2:
            if word1.count(word1[i]) != word2.count(word1[i]):
                return False
        else:
            return False
    return True


def clean_anagrams(words):
   for i in range(len(words)):
       for j in range(len(words)-1 , i,-1):
           if (is_anagram(words[i], words[j])):
               words.pop(j)
                
              
   return words


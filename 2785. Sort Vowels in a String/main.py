class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU' 
        sorted_vowels = sorted([c for c in s if c in vowels]) 
        new_string = "" 
        for c in s: 
            if c in vowels: 
                new_string += sorted_vowels.pop(0) 
            else: 
                new_string += c 
        return new_string

from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_substrings_with_vowels(word, k):
            vowel_count = Counter()
            result = left_pointer = non_vowel_count = 0

            for right_pointer in range(len(word)):
                char = word[right_pointer]
                
                if char in "aeiou":
                    vowel_count[char] += 1
                else:
                    non_vowel_count += 1
                
                while non_vowel_count >= k and len(vowel_count) == 5:
                    left_char = word[left_pointer]
                    if left_char in "aeiou":
                        vowel_count[left_char] -= 1
                        if vowel_count[left_char] == 0:
                            vowel_count.pop(left_char)
                    else:
                        non_vowel_count -= 1
                    left_pointer += 1

                result += left_pointer

            return result
        
        return count_substrings_with_vowels(word, k) - count_substrings_with_vowels(word, k + 1)

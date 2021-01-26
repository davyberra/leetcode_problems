class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Given a string of letters, returns the longest substring
            without repeating any letters, as well as the length of said string."""
        # List to store letters to check if any are being repeated
        hash_list = []
        # Keeps track of the longest substring encountered so far
        longest_substring = ''
        # Keeps track of the current substring at given time
        current_substring = ''
        for letter in s:
            # Checks if we are repeating a letter. If so, log, the current substring as our longest
            # if it is the longest so far, and starts the substring counting over again.
            if letter in hash_list:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                # Reset the substring counters
                hash_list = []
                current_substring = ''

            current_substring = current_substring + letter
            hash_list.append(letter)
            # print(hash_list)

        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        print(f"The answer is '{longest_substring}' with a length of {len(longest_substring)}.")


obj = Solution()
obj.lengthOfLongestSubstring('David K. Anthony Berra')
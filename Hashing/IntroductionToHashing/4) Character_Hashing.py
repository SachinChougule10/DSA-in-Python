# ASCII stands for American Standard Code for Information Interchange.
# It is a character encoding system that assigns a unique numerical value (integer) to every character ,including:

# English letters :-	A–Z, a–z
# Digits :-	0–9
# Special characters :-	@, #, $, %, &, etc.
# Control characters :-	newline (\n), tab (\t), etc.


s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_list = [0] * 26

for char in s:
    ascii_value = ord(char)
    index_value = ascii_value - 97
    hash_list[index_value] += 1

for i in q:
    ascii_value = ord(i)
    index_value = ascii_value - 97
    print(f"Frequency of {i}: ", hash_list[index_value])

    """
        Constraints :-
            'a' <= s[i] <= 'z'
            
        Time Complexity :-
            - In first loop we will iterate for 'm' no of times, m = no.of characters
            - In second loop we will iterate for 'n' no of times, n = no.of characters 
            - first for loop will run for 'm' times and second will run for 'n' times.
            - Time Complexity = O(m x n)
            
        Space Complexity :-
            - We are using a fixed sized list of 26 length, which will remain constant regardless of the input size
            - Space Complexity = O(1)
    """

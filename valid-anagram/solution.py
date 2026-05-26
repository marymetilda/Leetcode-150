def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    charCounts = [0] * 26

    for i in range(len(s)):
        charCounts[ord(s[i]) - ord('a')] += 1
        charCounts[ord(t[i]) - ord('a')] -= 1

    for count in charCounts:
        if count != 0:
            return False
        
    return True

print(is_anagram('rat', 'tat'))
print(is_anagram('rat', 'tar'))
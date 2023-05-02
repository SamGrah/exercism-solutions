def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    word_count = dict()
    for char in word:
        word_count[char] = word_count.get(char, 0) + 1
 
    for candidate in candidates:
        upper_candidate = candidate
        candidate = candidate.lower()
        if len(candidate) != len(word) or candidate == word:
            continue
        isAnagram = True
        candidate_count = dict()
        for char in candidate:
            candidate_count[char] = candidate_count.get(char, 0) + 1
            word_max = word_count.get(char, 0)
            char_count = candidate_count[char]
            if (word_max < char_count):
                isAnagram = False
                break
        if isAnagram:
            anagrams.append(upper_candidate)
    return anagrams

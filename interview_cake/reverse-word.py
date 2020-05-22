from typing import List

def solution(words: List):
    size = len(words)

    # O(n)
    for i in range(size // 2):
        head, tail = i, -(i+1)
        words[head], words[tail] = words[tail], words[head]

    word_start = 0

    # O(n) ish
    for i in range(size + 1):
        if i == size or words[i] == ' ':
            word_size = i - word_start
            for j in range(word_start, word_start + word_size // 2):
                head, tail = j, i - (j + 1 - word_start)

                words[head], words[tail] = words[tail], words[head]

            word_start = i + 1


test = list('cake pound steal')

solution(test)

print(test)
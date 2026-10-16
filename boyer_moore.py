
def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    last = {}

    for i in range(m):
        last[pattern[i]] = i

    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index", s)

            if s + m < n:
                s += m - last.get(text[s + m], -1)
            else:
                s += 1
        else:
            s += max(1, j - last.get(text[s + j], -1))


text = "ABAAABCD"
pattern = "ABC"

boyer_moore_search(text, pattern)

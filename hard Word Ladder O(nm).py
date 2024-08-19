def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    transform, seen, words, q = 2, set(), defaultdict(list), deque([beginWord])

    for word in wordList:
        for i in range(len(endWord)):
            words[word[:i] + '!' + word[i + 1:]].append(word)

    while q:
        for _ in range(len(q)):
            for i in range(len(endWord)):
                for word in words[q[0][:i] + '!' + q[0][i + 1:]]:
                    if endWord == word:
                        return transform

                    if word not in seen:
                        q.append(word)
                        seen.add(word)

            q.popleft()

        transform += 1
        
    return 0

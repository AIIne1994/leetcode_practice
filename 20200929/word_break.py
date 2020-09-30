def word_break(s, wordDict):
    words=set(wordDict)
    cache={}
    def breaker(s):
        if s not in cache:
            for w in words:
                if s[:len(w)]==w:
                    if len(s)==len(w):
                        cache[s]=True
                        return True
                    else:
                        cache[s]=breaker(s[len(w):])
                            
                        if cache[s]:
                            return True
            cache[s]=False
        return cache[s]
    return breaker(s)


if __name__ == "__main__":
    s = "cars"
    wordDict = ["car","ca","rs"]
    print(word_break(s, wordDict))

import os

def read_input():
    choice = input()
    if "I" in choice:
        pattern = input()
        text = input()
    else:
        folder = "tests/06"
        with open(folder, "r") as files:
            pattern = files.readline()
            text = files.readline()
    
    return (pattern.rstrip(), text.rstrip())

def hash_func(s, prime, x):
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % prime
    return h

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    prime = 10**9 + 7
    x = 263
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash_func(pattern, prime, x)
    t_hashes = [hash_func(text[i:i+p_len], prime, x) for i in range(t_len-p_len+1)]
    occurrences = [i for i in range(t_len-p_len+1) if t_hashes[i] == p_hash]
    return occurrences
 


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


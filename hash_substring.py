import os

def read_input():
    example=input().rstrip()
    if check=="I":
      pattern=input().rstrip()
      text=input().rstrip()
      return pattern, text
    if check=="F":
      path = os.getcwd()
      os.chdir(path) 
      file_path = f"{path}/tests/06"
      return pattern, text
    
    
    return (input().rstrip(), input().rstrip())

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


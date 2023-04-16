import os

def read_input():
    example=input().rstrip()
    if check=="I"
      pattern=input().rstrip()
      text=input().rstrip()
      return pattern, text
    if check=="F"
      path = os.getcwd()
      os.chdir(path) 
      file_path = f"{path}/tests/06"
      return pattern, text
    
    
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
   
def hash_func(s, prime=10**9 + 7, x=263):
    y= 0
    for c in reversed(s):
        y= (y * x + ord(c)) % prime
    return y

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash_func(pattern)
    text_hashes = [hash_func(text[i:i+pattern_len]) for i in range(text_len-pattern_len+1)]
    occurances= [i for i in range(text_len-pattern_len+1) if text_hashes[i] == pattern_hash]
    return occurances
 


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


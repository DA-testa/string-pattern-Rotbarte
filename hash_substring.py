
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    example = input()
    if "I" in example:
        pattern = input()
        text = input()
    if "F" in example:
        folder = "./tests/" + "06"
        with open(folder, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    
    return (pattern.rstrip(), text.rstrip())
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    # return both lines in one return
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

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

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

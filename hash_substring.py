
def read_input():
 
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


def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def hash_func(s, z=10**9 + 7, x=263):
    y= 0
    for c in reversed(s):
        y= (y * x + ord(c)) % z
    return y

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash_func(pattern)
    text_hashes = [hash_func(text[i:i+pattern_len]) for i in range(text_len-pattern_len+1)]
    occurrences = []
    for i in range(text_len-pattern_len+1):
        if p_hash == text_hashes[i]:
            if pattern == text[i:i+pattern_len]:
                occurrences.append(i)
    return occurances


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

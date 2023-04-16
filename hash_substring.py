
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

def get_occurrences(pattern, text):
   
    prime = 10**9 + 7
    x = 263
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = 0
    text_hashes = []
    h = 1
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * x + ord(pattern[i])) % prime
        h = (h * x) % prime
    for i in range(text_len - pattern_len + 1):
        text_hash = 0
        for j in range(pattern_len):
            text_hash = (text_hash * x + ord(text[i+j])) % prime
        if text_hash == pattern_hash and text[i:i+pattern_len] == pattern:
            occurrences.append(i)
    return occurrences



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

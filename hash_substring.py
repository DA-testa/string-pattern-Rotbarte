
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
    h = 1
    for i in range(pattern_len):
        pattern_hash = (pattern_hash + ord(pattern[i]) * h) % prime
        h = (h * x) % prime
    text_hashes = []
    h = 1
    for i in range(text_len - pattern_len + 1):
        if i == 0:
            for j in range(pattern_len):
                text_hashes.append((ord(text[pattern_len - 1 - j]) * h) % prime)
                if j < pattern_len - 1:
                    h = (h * x) % prime
        else:
            prev_h = (ord(text[i - 1]) * h) % prime
            new_h = (ord(text[i + pattern_len - 1]) * x) % prime
            text_hashes[i] = (text_hashes[i - 1] - prev_h + new_h) % prime
    occurrences = [i for i in range(text_len - pattern_len + 1) if pattern_hash == text_hashes[i]]
    return occurrences




if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

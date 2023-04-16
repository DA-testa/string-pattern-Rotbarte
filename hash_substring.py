
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
    occurrences = []
    lenpattern = len(pattern)
    
    prime = 10**9+7
    x = 256
    y = pow(x, lenpattern-1, prime)
    pattern2 = 0
    text2 = 0
    for i in range(lenpattern):
        pattern2 = (pattern2*x + ord(pattern[i])) % prime
        text2 = (text2*x + ord(text[i])) % prime

    if pattern2 == text2 and pattern == text[:lenpattern]:
        occurrences.append(0)

    for i in range(1, len(text) - lenpattern + 1):
        text2 = ((text2-ord(text[i-1])*y)*x + ord(text[i+lenpattern-1])) % prime
        if pattern2 == text2 and pattern == text[i:i+lenpattern]:
            occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

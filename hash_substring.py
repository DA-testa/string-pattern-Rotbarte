
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
    d = 256
    h = pow(d, lenpattern-1, prime)
    pattern2 = 0
    textHashVal = 0
    for i in range(lenpattern):
        pattern2 = (pattern2*d + ord(pattern[i])) % prime
        textHashVal = (textHashVal*d + ord(text[i])) % prime

    if pattern2 == textHashVal and pattern == text[:lenpattern]:
        occurrences.append(0)

    for i in range(1, len(text) - lenpattern + 1):
        textHashVal = (d*(textHashVal-ord(text[i-1])*h) + ord(text[i+lenpattern-1])) % prime
        if pattern2 == textHashVal and pattern == text[i:i+lenpattern]:
            occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

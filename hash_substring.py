
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
    patternLength = len(pattern)
    
    prime = 10**9+7
    d = 256
    h = pow(d, patternLength-1, prime)
    patternHashVal = 0
    textHashVal = 0
    for i in range(patternLength):
        patternHashVal = (patternHashVal*d + ord(pattern[i])) % prime
        textHashVal = (textHashVal*d + ord(text[i])) % prime

    if patternHashVal == textHashVal and pattern == text[:patternLength]:
        count.append(0)

    for i in range(1, len(text) - patternLength + 1):
        textHashVal = (d*(textHashVal-ord(text[i-1])*h) + ord(text[i+patternLength-1])) % prime
        if patternHashVal == textHashVal and pattern == text[i:i+patternLength]:
            occurrences.append(i)

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

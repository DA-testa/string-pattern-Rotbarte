
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
    count = []
    patternLength = len(pattern)
    B = 263
    Q = 1000000007
    
    patternHashVal = sum(ord(pattern[i]) * pow(B, patternLength - i - 1) for i in range(patternLength)) % Q
    textHashVal = sum(ord(text[i]) * pow(B, patternLength - i - 1) for i in range(patternLength)) % Q
    
    if patternHashVal == textHashVal and pattern == text[:patternLength]:
        count.append(0)

    for i in range(1, len(text) - patternLength + 1):
        textHashVal = (textHashVal - ord(text[i - 1]) * pow(B, patternLength - 1)) % Q
        textHashVal = (textHashVal * B + ord(text[i + patternLength - 1])) % Q
        if patternHashVal == textHashVal and pattern == text[i:i+patternLength]:
            count.append(i)

    return count

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

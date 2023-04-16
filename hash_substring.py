
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
    
    patternHashVal = hash_func(pattern)
    textHashVals = [hash_func(text[i:i+patternLength]) for i in range(len(text)-patternLength+1)]

    for i, hashVal in enumerate(textHashVals):
        if patternHashVal == hashVal and pattern == text[i:i+patternLength]:
            count.append(i)

    return count


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

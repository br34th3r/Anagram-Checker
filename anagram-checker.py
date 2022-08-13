import sys

def get_letter_counts(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

if __name__ == '__main__':
    if(len(sys.argv) <= 2 or len(sys.argv) > 3):
        print("Invalid Arguments")
        sys.exit()

    ordered = sys.argv[1]
    anagram = sys.argv[2]

    if get_letter_counts(ordered) == get_letter_counts(anagram):
        print("Valid Anagram")
    else:
        print("Invalid Anagram")


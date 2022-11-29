# Read a dictionary file and return a list of 5-letter words from in that dictionary
def read_file(filename):
    len5_dicts = []
    with open(filename, "r") as fh:
        while True:
            word = fh.readline().rstrip()
            if len(word) == 5:
                len5_dicts.append(word)
            if len(word) == 0:
                break

        return len5_dicts

# Write a list of words to a file
def write_file(filename, content):
    with open(filename, "w") as fh:
        for word in content:
            fh.write(word + "\n")

def contains_exactly(word, char_list):
    for i in range(len(char_list)):
        if char_list[i] != '-' and word[i] != char_list[i]:
            return False
    
    return True

def contains_any(word, char_list):
    for char in char_list:
        if char in word:
            return True

    return False

def contains_indet(word, char_dict):
    for c in char_dict.keys():
        if not c in word or word.rfind(c) in char_dict[c]:
            return False
    
    return True

def advanced_solve(known, blacklist, indeterminate, dictionary, talkative=False):
    known = list(known)
    # Check if the word contains eleminated characters
    first_pass_potential = [word for word in dictionary if not contains_any(word, blacklist)]
    # Check if the word contains characters we know in the right place
    second_pass_potential = [word for word in first_pass_potential if contains_exactly(word, known)]
    # Check if the word contains characters we know should be in there, but aren't sure where
    final_pass_potential = [word for word in second_pass_potential if contains_indet(word, indeterminate)]
    
    if talkative:
        for guess in final_pass_potential: print(guess)
    else:
        write_file("./guesses.txt", final_pass_potential)
advanced_solve("p--ch", ['a', 'o'], {}, read_file("./len5_dict.txt"), talkative=False)
# Running this script doesn't do anything since there are no function calls
# Import it from withing Python with "import ex25" then call its functions there

def break_words(stuff):
    # This multi-line string immediately after the function definition is a documentation comment (docstring)
    # Python automatically populates the function and module help using these comments
    """This function will break up words for us."""
    # split() returns a list of words in the string separated by, in this case, a space
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    # sorted() takes a list, sorts it, then returns the new sorted list
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # pop() removes and returns the last or index-specified item from a list
    # Index 0 is the first item in a list
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    # Index -1 is the last item in a list and is the default for pop()
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
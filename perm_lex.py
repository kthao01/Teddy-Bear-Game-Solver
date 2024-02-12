

def perm_gen_lex(word):

    """function that generates all permutations of the
    characters in a sting"""

    if len(word) <= 1:               #checking to see if word is is less than or equal to 1
        return [word]                #returns word as list to perms if it is = 1

    perms = perm_gen_lex(word[1:])   #calling self
    char = word[0]
    res = []

    for perm in perms:               #iterate through perms
        for i in range(len(perm)+1):            #loop for length of perm + 1
            res.append(perm[:i] + char + perm[i:])       #combines selected character with combination
    return sorted(res)                                   #of other letters in the word
                                                         #returns the result sorted



w = input('Word: ')
print(perm_gen_lex(w))

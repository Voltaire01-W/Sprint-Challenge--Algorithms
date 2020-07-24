'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # catch empty words and single letter words
    if not word:
        return 0
    if len(word) == 1:
        return 0

    # recurse down the word
    if len(word) > 1:
        count += count_th(word[1:])

    # find 'th's
    if word[:2] == 'th':
        count += 1
    
    return count
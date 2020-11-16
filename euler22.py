
def euler22():
    """Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    with open('data/p022_names.txt') as fp:
        names = fp.read().split(',')
        names = [name.strip('"') for name in names]
    
    names.sort()

    def name_score(name):
        return sum(ord(c) - 64 for c in name)

    return sum((i+1)*name_score(name) for i,name in enumerate(names))
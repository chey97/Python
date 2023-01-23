# given a list of words, and have to write an algorithm to group all the words which are anagrams of each other.

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i=" ".join(sorted(i)) #This line sorts the characters of the current string in the for loop, i, and then joins them back together with a space between them. It assigns the resulting string to a variable called sorted_i.
        dfdict[sorted_i].append(i) #This line adds the current string in the for loop, i, to the list of values in the defaultdict that corresponds to the key sorted_i. If the key sorted_i does not yet exist in the defaultdict, it will be automatically created with an empty list as the value.
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
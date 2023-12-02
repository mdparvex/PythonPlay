#anargam is if we rearrange a world we will get same alphabet
from collections import defaultdict

def anargam(word_list):
    dictionary = defaultdict(list)
    for word in word_list:
        sorted_word = "".join(sorted(word))
        dictionary[sorted_word].append(word)
    return dictionary.values()
    
if __name__=="__main__":
    word_list = ['cat', 'tac', 'good', 'gdoo']
    print(anargam(word_list))
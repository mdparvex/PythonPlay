
def find_duplicate(word_list):
    duplicate=[]
    for i in range(len(word_list)):
        if word_list[i] in word_list[i+1:] and word_list[i] not in duplicate:
            duplicate.append(word_list[i])

    return duplicate

if __name__=="__main__":
    word_list = ['hello', 'go','come','hello', 'hello', 'go']
    print(find_duplicate(word_list))
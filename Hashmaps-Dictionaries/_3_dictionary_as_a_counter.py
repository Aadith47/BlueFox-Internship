def word_counting():
    paragraph = "apple cherry blueberry cherry apple"
    words=paragraph.split()
    words_count = {}

    for word in words:
        if word in words_count:
            words_count[word] +=1
        else:
            words_count[word] = 1

    return words_count


def main():

    result1 = word_counting()
    print(result1)
    
main()
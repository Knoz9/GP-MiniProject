def main():
    path_a = './words/holy_words.txt'
    path_b = './words/eng_words.txt'
    print_result(path_a)
    print_result(path_b)


def count_different(lst):
    return len(set(lst))


def count_occurrences(lst):
    dct = {}
    for i in lst:
        if i not in dct.keys():  # If item is not a key add it
            dct[i] = 0
        dct[i] += 1
    return dct


def read_file(file_path):
    txt_file = open(file_path, 'r')
    lst = list()
    for line in txt_file:
        lst.extend(line.replace('\n', '').split('\n'))
    txt_file.close()
    return lst


def print_result(path):
    lst = read_file(path)
    unique_words = count_different(lst)

    print('- Result for the file', path.split('/')[-1])
    print('* The number of different words in the file:', unique_words)

    print('* The 10 most freq. occurring words with a length larger than 4:')

    occur = count_occurrences(lst)

    # Sort the dictionary by the value (time of occurrence)
    occur = sorted(occur.items(), key=lambda itm: itm[1])
    print('_'*33 + '\n Rank\tOccur\t\tWord\t\n' + '_'*33)

    # print the last 10 key, value pair where word length > 4
    i, j = 1, 0  # 'i' is the iterator value, j is to break from the while-loop
    while j < 10:  # loop until we get 10 words
        if len(occur[-i][0]) > 4:  # if the word > 4 print and add 1 to 'j'
            print(f'({j+1})\t{occur[-i][1]}\t\t- {occur[-i][0]} ')
            j += 1
        i += 1

    print('_'*33 + '\n')


main()

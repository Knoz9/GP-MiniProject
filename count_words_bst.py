from data_structure import BstMap as bst
from data_structure import HashSet as hset


def main():
    path_a = './words/holy_words.txt'
    path_b = './words/eng_words.txt'
    print_result(path_a)
    print_result(path_b)


def count_different(lst):
    hash_set = hset.HashSet()
    hash_set.init()
    for i in lst:
        hash_set.add(i)
    return hash_set


def count_occurrences(lst):
    bmap = bst.BstMap()

    for i in lst:
        if len(i) > 4:  # Remove words that are not of size >4
            occur = bmap.get(i)
            if occur is not None:
                bmap.put(i, occur+1)
            else:
                bmap.put(i, 1)
    # Generate bstmap to a list
    bst_lst = bmap.as_list()
    # return the converted list and the max depth of BST
    return bst_lst, bmap.max_depth()


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
    occur, max_depth = count_occurrences(lst)

    print('- Result for the file', path.split('/')[-1])
    print('* The number of different words in the file:'
          + str(unique_words.get_size()))
    print(f'- Max bucket size for HashSet: {unique_words.max_bucket_size()}')
    print('- Max depth for BstMap: ', max_depth)

    print('* The 10 most freq. occurring words with a length larger than 4:')

    # Sort list and get top ten tuples
    # REF: https://www.programiz.com/python-programming/methods/built-in/sorted
    top_ten = sorted(occur, key=lambda x: x[1], reverse=True)[0:10]

    print('_'*33 + '\n Rank\tOccur\t\tWord\t\n' + '_'*33)

    j = 0  # j is the rank of the word
    for i in top_ten:  # loop top ten list
        print(f'({j+1})\t{i[1]}\t\t- {i[0]} ')
        j += 1

    print('_'*33 + '\n')


main()

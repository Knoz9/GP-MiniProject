from data_structure import BstMap as bst
from data_structure import HashSet as hset
import matplotlib.pyplot as plt


def main():
    path = './words/eng_words.txt'
    lst = read_file(path)
    length_count = word_length_count(lst)
    added_unique = word_added_unique(lst)
    plot_length_count(length_count, added_unique)


def read_file(file_path):
    print('Opening and reading file...')
    txt_file = open(file_path, 'r', encoding='utf8')
    lst = list()
    for line in txt_file:
        lst.extend(line.replace('\n', '').split('\n'))
    txt_file.close()
    return lst


def word_length_count(lst):

    print('Adding to BstMap...')

    bmap = bst.BstMap()

    # for each word, add its length to bstmap
    for i in lst:
        word_length = len(i)
        word_count = bmap.get(word_length)
        if word_count is not None:  # If the length exist, + 1 the value
            bmap.put(word_length, word_count+1)
        else:  # Add new lenth
            bmap.put(word_length, 1)

    # Generate bstmap to a list
    bst_lst = bmap.as_list()
    # return the converted BstMap
    return bst_lst


def word_added_unique(lst):

    print('Adding to HashSet...')

    hash_set = hset.HashSet()
    hash_set.init()
    added_words = []
    # for each word in the list add it to the hashset
    for i in lst:
        hash_set.add(i)
        added_words.append(hash_set.get_size())  # keep track of hashset size

    # Return list of the hashset for each time we tried adding a word
    return added_words


def plot_length_count(length_count, added_unique):

    print('Plotting...')

    plt.style.use('seaborn')
    fig, (count_plt, uniq_plt) = plt.subplots(1, 2)

    # Length-Count Graph
    length = [i[0] for i in length_count]
    count = [i[1] for i in length_count]
    count_plt.bar(length, count)
    count_plt.set_title('”Length” vs ”Count” in the file eng_words.txt')
    count_plt.set_xlabel('Word Length')
    count_plt.set_ylabel('Count (log)')
    count_plt.set_yscale('log')

    # Added_Unique Graph
    added_words = [i+1 for i in range(len(added_unique))]  # the index + 1
    unique_words = added_unique
    uniq_plt.set_title("”Added” vs ”Unique” In the HashSet")
    uniq_plt.set_xlabel('Added Words')
    uniq_plt.set_ylabel('Unique Words (hash set size)')
    uniq_plt.plot(added_words, unique_words)
    plt.tight_layout()

    plt.show()


main()

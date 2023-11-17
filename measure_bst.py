# Measure the time to look-up a fix number of keys (say 20000)
# in trees of different sizes in your BST based map implementation.
# We expect the look-up time to increase when the tree gets larger.
# Measure also the max tree depth at the same sizes.
# We expect two plots (using matplotlib)
# showing look-up time vs tree size, and max depth vs tree size.
from matplotlib import pyplot as plt
from data_structure import BstMap as bst
import random
import time


def main():
    sizes, times, depths = measure_lookup()
    plot(sizes, times, depths)


# Reads file with OR without a limit to the number of words
def read_file(file_path, max_words=None):
    debug_msg = 'all' if not max_words else max_words
    print(f'Reading {debug_msg} word/s from {file_path} ...')
    txt_file = open(file_path, 'r', encoding='utf8')
    lst = list()
    if not max_words:  # If the function wasn't called with max words
        for line in txt_file:
            lst.extend(line.replace('\n', '').split('\n'))
    else:  # if we have max words, read words until we have the given words
        for line in txt_file:
            lst.extend(line.replace('\n', '').split('\n'))
            max_words -= 1
            if max_words <= 0:
                break
    txt_file.close()
    return lst


# Converts a list to a binary search tree map
def to_bst(lst):
    bmap = bst.BstMap()

    for i in lst:  # To measure time we don't care about the values
        bmap.put(i, None)
    return bmap


# Gets the mean time needed to search 'keys' in 'bst_map'
def time_lookup(keys, bst_map):
    start = time.time()

    for i in range(5):
        for key in keys:
            bst_map.get(key)

    elapsed = time.time() - start
    return round(elapsed/5, 3)


# Takes 20k random words from a file
def random_keys(path):
    all_words = read_file(path)
    num_of_words = len(all_words)
    words = []
    for i in range(20000):
        index = random.randint(0, num_of_words)
        words.append(all_words[index])
    return words


def measure_lookup():
    path = './words/unique_words.txt'
    keys = random_keys(path)
    print(len(keys))
    # The different sizes of BST
    sizes = [10, 100, 500, 1000, 5000, 10000, 30000, 65000, 80000, 90000, 100000]
    times = []
    depths = []
    for size in sizes:
        test_object = to_bst(read_file(path, size))
        elapsed = time_lookup(keys, test_object)
        times.append(elapsed)
        depths.append(test_object.max_depth())
    return sizes, times, depths


def plot(sizes, times, depths):
    plt.style.use('ggplot')
    fig, (size_time_plt, size_depth_plt) = plt.subplots(1, 2)

    # Size-Time Graph
    x = sizes
    y = times
    size_time_plt.plot(x, y)
    size_time_plt.set_title('BST Size vs Time')
    size_time_plt.set_xlabel('Size')
    size_time_plt.set_ylabel('Time (seconds)')

    # Size_Max-Depth Graph
    i = sizes
    j = depths
    size_depth_plt.set_title("BST Size vs BST Max-Depth")
    size_depth_plt.set_xlabel('Size')
    size_depth_plt.set_ylabel('Max Depth')
    size_depth_plt.plot(i, j)
    plt.tight_layout()

    plt.show()


main()

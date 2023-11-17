from data_structure import HashSet as hset
import matplotlib.pyplot as plt
import time


def main():
    path = './words/unique_words.txt'
    words = read_file(path)
    sizes, max_bucket, avg_time = measure_hset(words)
    for i in range(3):
        _, _, time = measure_hset(words)
        for j in range(len(avg_time)):
            avg_time[j] = avg_time[j] + time[j] / 2
    plot(sizes, max_bucket, avg_time)


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


def measure_hset(words):
    times = []
    max_bucket = []
    sizes = []
    i = 0
    hash_set = hset.HashSet()
    hash_set.init()
    start = time.time()
    for word in words:
        if i == 1000:
            elapsed = time.time() - start
            max_bucket.append(hash_set.max_bucket_size())
            sizes.append(hash_set.get_size())
            times.append(elapsed)
            i = 0
            start = time.time()
        hash_set.add(word)
        i += 1
    return sizes, max_bucket, times


def plot(sizes, max_bucket, avg_time):
    plt.style.use('ggplot')
    fig, (size_time_plt, size_max_plt) = plt.subplots(1, 2)

    # Size-AvgTime Graph
    x = sizes
    y = avg_time
    size_time_plt.plot(x, y)
    size_time_plt.set_title('HashSet Size vs Adding Time')
    size_time_plt.set_xlabel('Size')
    size_time_plt.set_ylabel('Time (seconds)')

    # Size_Max-Bucket Graph
    i = sizes
    j = max_bucket
    size_max_plt.set_title("HashSet Size vs Max Bucket Size")
    size_max_plt.set_xlabel('Size')
    size_max_plt.set_ylabel('Max Bucket Size')
    size_max_plt.plot(i, j)
    plt.tight_layout()

    plt.show()


main()

from trie import Trie


def get_trie():
    trie = Trie()
    with open("./test_dataset.txt", "r") as f:
        for line in f.readlines():
            data_line = line.split(',')
            trie.insert(
                data_line[0],
                {
                    'name': data_line[0],
                    'amount': data_line[1],
                    'gender': data_line[2],
                    'type': data_line[3]
                }
            )
    return trie


TRIE = get_trie()
print(1)


def suggest(letter):
    return TRIE.get_by_prefix_sort_desc_by(letter, 'amount')[:10]

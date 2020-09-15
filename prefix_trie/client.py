from .trie import Trie


def get_trie():
    """
    Load data to prefix trie

    Returns:
        (Trie): prefix trie with loaded data
    """
    trie = Trie()
    with open("./prefix_trie/test_dataset.txt", "r") as f:
        for line in f.readlines():
            data = line.split(',')
            trie.insert(
                data[0],
                {
                    'name': data[0],
                    'amount': data[1],
                    'gender': data[2],
                    'type': data[3]
                }
            )
    return trie


TRIE = get_trie()


def suggest(query: str, count: int):
    """
    Get suggestions by name prefix
    Args:
        query(str): name prefix
        count(int): max length of suggestion list

    Returns:
        list(dict): suggestions
    """
    return TRIE.get_by_prefix_sort_desc_by(query, 'amount')[:count]

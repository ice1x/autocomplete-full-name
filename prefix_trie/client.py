# -*- coding: utf-8 -*-
from .trie import Trie

GENDER_MAPPING = {'t': 'male', 'f': 'female', None: 'unknown'}
TYPE_MAPPING = {'t': 'firstname', 'f': 'middlename', '': 'lastname'}


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
                    'name': data[0].encode('utf-8'),
                    'amount': data[1],
                    'gender': data[2],
                    'type': data[3].strip()
                }
            )
    return trie


TRIE = get_trie()


def replace_placeholders(source_data):
    """
    Replace placeholders by user-friendly values
    Args:
        source_data(list): list of dict's with data from Trie

    Returns:
        (list): list of dict's with data from Trie with replaced placeholders

    """
    output = []
    for row in source_data:
        output_row = row.copy()
        output_row['type'] = TYPE_MAPPING.get(output_row['type'])
        output_row['gender'] = GENDER_MAPPING.get(output_row['gender'])
        output.append(output_row)
    return output


def suggest(query: str, count: int):
    """
    Get suggestions by name prefix
    Args:
        query(str): name prefix
        count(int): max length of suggestion list

    Returns:
        list(dict): suggestions
    """
    if count > 100:
        count = 100
    result = TRIE.get_by_prefix_sort_desc_by(query, 'amount')[:count]
    return replace_placeholders(result)


def parse(query: str):
    """
    Parse full name by text string

    Args:
        query(str): text string which may contain full name

    Returns:
        list(dict): full name parsed
    """
    words = query.split()
    result = []
    for word in words:
        word_parse_result = TRIE.get_by_word_and_query(word, {})
        if not word_parse_result:
            continue
        result.append(word_parse_result)
    return replace_placeholders(result)

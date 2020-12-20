import datetime
import unittest

from prefix_trie.client import TRIE


GENDER = {
    True: 'Male',
    False: 'Female',
    None: 'Unknown'
}
TYPE = {
    True: 'name',
    False: 'patronymic',
    None: 'surname'
}
TYPE_REVERSED = {v: k for k, v in TYPE.items()}
GENDER_REVERSED = {v: k for k, v in GENDER.items()}


class TestSmallTrieMethods(unittest.TestCase):
    def test_get_by_word_and_query_ivan(self):
        res = TRIE.get_by_word_and_query('иван', {'type': 't'})
        self.assertEqual(res, {'name': 'иван', 'amount': '25836', 'gender': 't', 'type': 't'})

    def test_get_by_word_and_query_anton(self):
        res = TRIE.get_by_word_and_query('антон', {'type': 't'})
        self.assertEqual(res, {'name': 'антон', 'amount': '20633', 'gender': 't', 'type': 't'})


if __name__ == '__main__':
    unittest.main()


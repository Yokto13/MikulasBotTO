import unittest
from db import DB

class DBTests(unittest.TestCase):
    def __init__(self):
        self.db = DB("", False)
        self.db._db = {1:2, "a":"b", "ca":["c", "d"]}
    def test_reverse(self):
        db._build_reversed()
        self.assertCount(db._rev, {2:1, "b":"a", "c":"ca", "d":"ca"})
        self.assertCount(db._db, {1:2, "a":"b", "ca":["c","d"]})

    def test_add_query(self):
        self.db.add_query("ca","1")
        self.assertCount(db._rev, {2:1, "b":"a", "c":"ca", "d":"ca",
            "1": "ca"})


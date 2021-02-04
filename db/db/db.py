from typing import Dict, Iterator, Tuple, List
import os
import json

class DB:
    def __init__(self, path: str, load: bool=True):
        self.path = path
        if load:
            self.load()
        else:
            self._db = {}
        # Reversed db.
        # Db is saved in Answer:Query format, because there are
        # multiple possible queries too each answer.
        self._rev = {}
        self.build_reversed()

    def build_reversed(self):
        self._rev = {}
        for ans, qs in self._db.items():
            for q in qs:
                self._rev[q] = ans

    def load(self):
        """ Loads db base of path given to the constructor. """
        if os.path.exists(self.path):
            self._load()
            self.build_reversed()
        else:
            self._db = {}

    def _load(self):
        self._db = json.load(open(self.path, 'rb'))

    def dumpdb(self):
        """ Saves the database. """
        json.dump(self._db, open(self.path, 'w'))

    def __getitem__(self, key: str) -> str:
        return self._rev[key]

    def __setitem__(self, key: str, new_val: List[str]):
        """ 
        Sets key equal to a value of list type. 

        Explicitly checks for the type of new_val and raises TypeError if its not
        a list.
        """

        if isinstance(new_val, list):
            self._db[key] = new_val
            self.build_reversed()
        else:
            raise TypeError

    def add_query(ans: str, query: str):
        """ Adds query given answer and query. 

            If the ans isn't in db creates the corresponding list.
        """
        if ans in self._db:
            self._db[ans].append(query)
        else:
            self.__setitem__(ans, [query])
        self.build_reversed()


    def __delitem__(self, key: str):
        """ Removes an object given its key (answer). """
        del self._db[key]
        self.build_reversed()

    def __iter__(self) -> Iterator[Dict[str, str]]:
        return iter(self._rev)

    def __len__(self) -> int:
        return len(self._rev)

    def __contains(self, key: str):
        print("Use .contains_answer or .contains_query")
        raise NotImplementedError

    def contains_answer(self, key: str) -> bool:
        return key in self._db

    def contains_query(self, key: str) -> bool:
        return key in self._rev

    def items(self):
        print("Use .answers or .queries or .answers_queries or.queries_answers")
        raise NotImplementedError

    def keys(self):
        print("Use .answers or .queries or .answers_queries or .queries_answers") 
        raise NotImplementedError

    def answers(self) -> Iterator[str]:
        return self._db.keys()

    def queries(self) -> Iterator[str]:
        return self._rev.keys()

    def answers_queries(self):
        return self._db.items()

    def queries_answers(self):
        return self._rev.items()

    def clear(self):
        """ Empties the whole database. """
        self._db = {}
        self.build_reversed()

#!/usr/bin/env python3

'''
module for returning pâage state
'''
import csv
import math
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    '''helper function that shows ranges to be used'''
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return  list of rows'''
        self.dataset()
        if self.__dataset is None:
            return []
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, en_idx = index_range(page, page_size)
        l_ds = len(self.__dataset)
        if(start_idx > l_ds):
            return []
        return self.__dataset[start_idx:en_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''return page info and data'''
        r = self.get_page(page, page_size)
        t_p = math.ceil(len(self.__dataset) / page_size)
        d = dict()
        d["page_size"] = page_size
        d["page"] = page
        d["data"] = r
        d["next_page"] = page + 1 if page + 1 < t_p else None
        d["prev_page"] = page - 1 if page - 1 > 1 else None
        d["total_page"] = t_p
        return d

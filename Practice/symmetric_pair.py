"""
Symmetric Pair
Input : list = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
Output : [[30, 40], [5, 10]]
"""
from typing import List, Tuple, Iterator
def symmetric_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    """

    :param pairs:
    :return:  symmetric pair
    解説
    1. ペアのリストをループで回す
    2. ペアのリストの要素をfirst, secondに代入する
    3. cacheにsecondがあるかどうかを確認する
    4. cacheにsecondがあれば、そのペアをyieldする
    5. cacheにsecondがなければ、cacheにfirstをkeyとしてsecondをvalueとして追加する
    6. 1から5を繰り返す
    """
    cache = {}  # cache = {11: 20, 30: 40, 5: 10}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second  # cacheにfirstをkeyとしてsecondをvalueとして追加する：{11: 20, 30: 40, 5: 10}
        elif value == first:  # cacheにsecondがあれば、そのペアをyieldする
            yield pair

if __name__ == "__main__":
    pairs = [(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]
    print(list(symmetric_pair(pairs)))
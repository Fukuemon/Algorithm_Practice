"""
bubble sort
日本語での説明
bubble sortの計算量：O(n^2)
bubble sortの安定性：安定

bubble sortは隣り合う要素を比較して、順番が逆であれば交換するという処理を繰り返すアルゴリズムです。

bubble sortは以下のようなアルゴリズムです。

1. 配列の先頭から隣り合う要素を比較する。
2. 順番が逆であれば交換する。
3. 配列の末尾まで1.と2.を繰り返す。
4. 1.から3.を配列の要素数分繰り返す。
"""

from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for i in range(20)]

    print(bubble_sort(nums))

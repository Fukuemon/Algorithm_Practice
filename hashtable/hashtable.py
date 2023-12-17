import hashlib


class HashTable(object):

    def __init__(self, size=10):
        self.size = size
        # ハッシュテーブルの作成
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        # ハッシュ値を求める
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        # ハッシュ値を求める
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key) -> any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")

            print()


    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add("car", "Tesla")
    hash_table.add("car", "Toyota")
    hash_table["pc"] = "mac"  # __setitem__が呼ばれる
    hash_table["sns"] = "YouTube"
    print(hash_table["sns"])  # __getitem__が呼ばれる
    hash_table.print()

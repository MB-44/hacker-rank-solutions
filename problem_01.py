if __name__ == "__main__":
    n = int(input())
    ints = tuple(map(int, input().split()))
    hash_value = hash(ints)
    positive_hash_value = hash_value & ((1 << 64) - 1)
    print(positive_hash_value)
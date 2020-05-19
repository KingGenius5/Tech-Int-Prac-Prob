def find_duplicates(list):
    rep = {}
    for item in list:
        if item in rep:
            return item
        else:
            rep[item] = 1


if __name__ == "__main__":
    list = [0,2,2,3,4,5,7]
    print(find_duplicates(list))
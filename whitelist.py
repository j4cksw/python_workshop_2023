def read_whitelist():
    whitelist = set()
    f = open("whitelist.txt", "r")
    for whitelist_item in f:
        whitelist.add(whitelist_item.strip("\n"))
    return whitelist
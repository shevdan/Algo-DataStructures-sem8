

def solve(t, dict):
    lst = [False for _ in range(len(t) + 1)]
    lst[len(t)] = True

    for i in range(len(t), -1, -1):
        for word in dict:
            if  (i + len(word) <= len(t) and t[i: i + len(word)] == word):
                lst[i] = lst[i + len(word)]
            if lst[i]:
                break
    return lst[0]

if __name__ == "__main__":
    t = "breaksandown"
    lst = ["breaks", "sand", "down"]
    print(solve(t, lst))
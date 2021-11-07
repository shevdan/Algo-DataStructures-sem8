def hashCode(str):
    hash = 0
    skip = max(1, len(str)//8)
    for i in range(0, len(str), skip):
        hash = (hash*37) + ord(str[i])
    
    return hash

if __name__ == "__main__":
    s1 = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooonggg"
    s2 = "loooooooooooooooooooooooooooooooofooooooaoooooooooooaoooonggg"
    print(hashCode(s1))
    print(hashCode(s2))


def solve(larger_str: str, sub_str: str):
    #O(len(substr) * len(larger_str))

    # memo[i][j] = num of substr[:i] in larger[:j]
    memo = [[0 for _ in range(len(larger_str) + 1)] for _ in range(len(sub_str) + 1)]

    # "" is a substr of any string
    for i in range(len(larger_str) + 1):
        memo[0][i] = 1
    
    for i in range(1, len(sub_str) + 1):
        for j in range(1, len(larger_str) + 1):
            if sub_str[i - 1] == larger_str[j - 1]:
                # if last characters are the same => num of substrings is
                #a number of substring of substr in larger[:j - 1] + num of substr[:i-1] in larger[:j - 1]
                memo[i][j] = memo[i][j - 1] + memo[i - 1][j - 1]
            
            else:
                #if last characters dont coincide => num of occurences is num of occurnces
                #of the same substr in larger[:j - 1]
                memo[i][j] = memo[i][j - 1]
            

    return memo[len(sub_str)][len(larger_str)]


if __name__ == "__main__":
    s = "rabbbit"

    t = "rabbit"

    print(solve(s, t))
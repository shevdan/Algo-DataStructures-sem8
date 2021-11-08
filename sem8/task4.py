

def solve(lst):
    #define the array of total time taken for each player. This will be the answer
    total_time_per_player = [0 for _ in range(len(lst))]

    # define the initial matrix containing time for each player
    
    end_time = [[0, 0, 0] for _ in range(len(lst))]
    for i in range(len(lst)):
        # define the initial time
        end_time[i][0] = lst[i][0]
        # total_time_per_player[i] = end_time[i][0]
        print(end_time, total_time_per_player)

        #update time of the endings per player
        for j in range(1, 3):
            # end time for j-th sport of the i-th player is time of the ending of j-1`th sport + time for j-th
            end_time[i][j] = end_time[i][j-1] + lst[i][j]

            total_time_per_player[i] += end_time[i][j]
    
    new_lst = list(zip(total_time_per_player, lst))
    print(new_lst)

    return sorted(new_lst, key=lambda x: x[0])





if __name__ == "__main__":
    lst = [[1,3,3], [2,3,4], [5,6,7]]

    print(solve(lst))

"""
_|||---
 __|||----
   _____||||||-------

"""
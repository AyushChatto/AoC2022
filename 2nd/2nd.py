score = 0
move_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6,
    'A': 1,
    'B': 2,
    'C': 3
}

def move(opp, res):
    if res == 0:
        ans = (opp - 1) % 3
    elif res == 3:
        ans = opp
    else:
        ans = (opp + 1) % 3
    
    return ans if ans > 0 else 3
    



with open("in.txt") as f:
    for row in f:
        opp, res = map(lambda x: move_scores[x], row.strip().split(' '))
        score += res
        score += move(opp, res)

    print(score)

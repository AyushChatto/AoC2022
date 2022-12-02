score = 0
move_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

def result(opp, you):
    #R1, P2, S3
    if opp == you:
        return 3
    elif opp - you == 1 or opp - you == -2:
        return 0
    else:
        return 6



with open("in.txt") as f:
    for row in f:
        opp, you = map(lambda x: move_scores[x], row.strip().split(' '))
        score += you
        score += result(opp, you)
    print(score)

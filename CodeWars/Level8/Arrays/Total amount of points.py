def points(games):
    sum = 0
    for i in range(0, len(games)):
        if games[i][0] > games[i][2]:
            sum += 3
        elif games[i][0] == games[i][2]:
            sum += 1
    return sum

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
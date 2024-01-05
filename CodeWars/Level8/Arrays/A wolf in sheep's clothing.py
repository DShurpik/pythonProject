def warn_the_sheep(queue):
    index = 0
    for i in range(0, queue.__len__()):
        if queue[i] == 'wolf': index = i + 1
    final_index = queue.__len__() - index
    if final_index != 0:
        return f"Oi! Sheep number {final_index}! You are about to be eaten by a wolf!"
    else:
        return "Pls go away and stop eating my sheep"



print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
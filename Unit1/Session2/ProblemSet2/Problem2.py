def average(scores):
    total = sum(scores)
    count = len(scores)
    return total/count

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)
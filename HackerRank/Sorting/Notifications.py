# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    from bisect import insort, bisect_left
    noti = 0
    stored = sorted(expenditure[0:0 + d])
    pre = expenditure[0]
    for i, e in enumerate(expenditure[d:]):
        if len(stored) % 2 == 0:
            median = (stored[len(stored) // 2] + stored[(len(stored) // 2) - 1]) / 2
        else:
            median = stored[len(stored) // 2]
        if e >= 2 * median:
            noti += 1
        insort(stored, e)
        del stored[bisect_left(stored, pre)]
        pre = expenditure[i + 1]
    return noti
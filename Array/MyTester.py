def create_queues(remain_passengers, picked_passengers):
    print(remain_passengers, 'remain')
    print(picked_passengers, 'pick')
    if remain_passengers == '':
        print(picked_passengers)

    else:
        for i, val in enumerate(remain_passengers):
            new_remain = remain_passengers[:i] + remain_passengers[i + 1:]
            new_picked = picked_passengers + [val]
            create_queues(new_remain, new_picked)


passengers_to_pick = []
picks = []
for token in input().split():
    passengers_to_pick.append(token)
print('All unique orderings:')
create_queues(passengers_to_pick, picks)
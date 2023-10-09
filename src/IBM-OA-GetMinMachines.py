start = [2, 1, 5, 5, 8]
end = [5, 3, 8, 6, 12]


def getMinMachines(start, end):
    # let start_time as +1 for adding new machine, end_time as -1 for removing previous machine
    events = [(start[i], 1) for i in range(len(start))] + [(end[i], -1) for i in range(len(end))]
    # sorted by start_time
    events.sort(key=lambda x: x[0])

    # count current task and return the max
    current_tasks = 0
    max_tasks = 0

    for _, e in events:
        current_tasks += e
        max_tasks = max(max_tasks, current_tasks)
    return max_tasks


if __name__ == '__main__':
    getMinMachines(start, end)

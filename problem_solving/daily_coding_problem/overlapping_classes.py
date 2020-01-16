# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def get_min_no_classes(schedules):
    """
    get the classes
    sort by starting time
    check overlapping with start time for each schedule with eachother schedules after that if not overlapping else move to next

    # for i in schedules:
    #     if overlap:
    #         pass
    start = 0
    # end = l
    end = 1
    while start < end: #  and start != end
        pass
    :param schedules:
    :return:
    """
    schedules.sort(key=lambda x: x[0])
    for i in range(0, len(schedules)):
        for j in range(i + 1, len(schedules)):
            print(schedules[i], schedules[j])
            if True:
                pass
        print("***")


get_min_no_classes([(30, 75), (0, 50), (60, 150)])

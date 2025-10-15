from typing import List


def js(d: List[int], J: List[int], n: int):
    d[0] = J[0] = 0
    J[1] = 1
    k = 1
    for i in range(2, n):
        r = k
        dl_till = d[J[r]]
        current_dl = d[i]
        while dl_till > current_dl and dl_till != r:
            r -= 1
        if (dl_till <= current_dl) and (current_dl > r):
            J[r + 1] = i
            for q in range(k, r, -1):
                J[q + 1] = J[q]
                J[r + 1] = i
                k += 1
    return k


from typing import List, Tuple


def job_sequencing(deadlines: List[int], profits: List[int]) -> Tuple[List[int], int]:
    n = len(deadlines)

    # Step 1: Sort jobs by profit in descending order
    jobs = sorted(zip(deadlines, profits, range(n)), key=lambda x: x[1], reverse=True)

    max_deadline = max(deadlines)  # Find the maximum deadline
    schedule = [-1] * (max_deadline + 1)  # Job slot array (-1 means empty)

    total_profit = 0

    # Step 2: Assign jobs based on deadline constraints
    for deadline, profit, job_id in jobs:
        for slot in range(min(deadline, max_deadline), 0, -1):  # Find a free slot
            if schedule[slot] == -1:  # If slot is free, assign job
                schedule[slot] = job_id
                total_profit += profit
                break

    # Step 3: Extract scheduled jobs (ignoring empty slots)
    scheduled_jobs = [job for job in schedule if job != -1]

    return scheduled_jobs, total_profit


# Example Usage
deadlines = [2, 1, 2, 1]
profits = [100, 10, 15, 27]

scheduled_jobs, max_profit = job_sequencing(deadlines, profits)

print("Scheduled Job Indices:", scheduled_jobs)
print("Total Maximum Profit:", max_profit)

# print(js([100, 15, 10, 27], [2, 2, 1, 1], 5))

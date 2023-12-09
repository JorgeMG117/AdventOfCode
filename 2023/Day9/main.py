

"""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
# Read the file
with open('input.txt', 'r') as f:
    lines = f.readlines()
    sum_extrapolated = 0
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        nums = line.split(' ')
        nums = [int(num) for num in nums]
        #print(nums)

        report = []
        report.append(nums)

        exit = False
        while not exit:
            i = 0
            differences = []

            all_zero = True
            for i in range(len(nums) - 1):
                differences.append(nums[i + 1] - nums[i])
                if differences[i] != 0:
                    all_zero = False

            if all_zero:
                # First to extrapolate
                differences.append(0)
                exit = True

            nums = differences
            report.append(differences)

        # Loop report backwards, len - 1 to 1
        for i in range(len(report) - 1, 0, -1):
            # Get last element of i
            last = report[i][-1]
            # Get last of i + 1
            last_next = report[i - 1][-1]
            extrapolated = last + last_next

            report[i - 1].append(extrapolated)

        sum_extrapolated += report[0][-1]

        print(report)
    print(sum_extrapolated) 





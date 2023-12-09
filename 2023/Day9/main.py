

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
                # First to extrapolate, append 0 at begginning
                differences.insert(0, 0)
                exit = True

            nums = differences
            report.append(differences)

        # Loop report backwards, len - 1 to 1
        for i in range(len(report) - 1, 0, -1):
            # Get first element of i
            first = report[i][0]
            # Get last of i + 1
            first_next = report[i - 1][0]
            extrapolated = first_next - first

            report[i - 1].insert(0, extrapolated)

        sum_extrapolated += report[0][0]

        print(report)
    print(sum_extrapolated) 





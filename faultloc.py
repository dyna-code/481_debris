import sys
import math
import functools

def my_parse(filename):
    with open(filename) as f:
        lines = f.readlines()
    coverage = {}
    for i in lines:
        i = i.strip()
        if i.startswith("#####") or i.startswith("-") or i.startswith("="):
            continue
        splitting = i.split(":")
        coverage[int(splitting[1].strip())] = int(splitting[0].strip())
    return coverage

def computation(passed, failed, total_fail):
    denominator = math.sqrt(total_fail * (passed + failed))
    if denominator == 0:
        return -1.0
    elif failed == 0:
        return 0.0
    else:
        return failed / denominator

def fine(a, b):
    if a[1] == b[1] and a[0] < b[0]:
        return 1
    else:
        return 0


def ochiai(total_fail, passed_coverage, failed_coverage):
    suspiciousness = []
    my_tuple = ()
    lineSet = []
    for line in passed_coverage:
        lineSet.append(line)
    for line in failed_coverage:
        if line not in lineSet:
            lineSet.append(line)
    #print(lineSet)
    for line in lineSet:
        passed = passed_coverage.get(line, 0)
        failed = failed_coverage.get(line, 0)
        score = computation(passed, failed, total_fail)
        if score != -1.0:
            my_tuple = (line, score)
            suspiciousness.append(my_tuple)
        #suspiciousness[line] = computation(passed, failed, total_fail)
    new_sorted = sorted(suspiciousness, key=lambda x: (-x[1], x[0]))
    #new_sorted = sorted(suspiciousness, key=lambda sort: sort[1], reverse=True)
    #new_sorted = sorted(new_sorted, key=functools.cmp_to_key(fine))
    return new_sorted[:100]



if __name__ == "__main__":
    pass_files = [filename for filename in sys.argv[1:] if "pass" in filename]
    fail_files = [filename for filename in sys.argv[1:] if "fail" in filename]
    total_fail = len(fail_files)
    passed_coverage = {}
    for i in pass_files:
        coverage = my_parse(i)
        for line in coverage:
            if passed_coverage.get(line) == None:
                passed_coverage[line] = 1
            else:
                passed_coverage[line] += 1

    failed_coverage = {}
    for j in fail_files:
        coverage = my_parse(j)
        for line in coverage:
            if failed_coverage.get(line) == None:
                failed_coverage[line] = 1
            else:
                failed_coverage[line] += 1

    result = ochiai(total_fail, passed_coverage, failed_coverage)
    print(result)
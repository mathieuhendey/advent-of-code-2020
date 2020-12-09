def get_input_lines():
    input_groups = open("input").read().strip().split("\n\n")
    return [line.split() for line in input_groups]


def yes_answers_anyone(input_line):
    for group in input_line:
        yield len(set.union(*(set(s) for s in group)))


def yes_answers_everyone(input_line):
    for group in input_line:
        yield len(set.intersection(*(set(s) for s in group)))


if __name__ == "__main__":
    input_lines = get_input_lines()
    anyone_answered_yes = sum(yes_answers_anyone(input_lines))
    everyone_answered_yes = sum(yes_answers_everyone(input_lines))
    print("Part1: %d" % anyone_answered_yes)
    print("Part2: %d" % everyone_answered_yes)

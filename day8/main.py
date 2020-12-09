instructions = []
accumulator = 0
possibly_corrupt_indices = []
corrupt_map = {"jmp": "nop", "nop": "jmp"}


def prepare_part_1():
    with open("input") as f:
        for operation, argument in map(lambda x: x.split(), f):
            instructions.append((operation, int(argument)))


def prepare_part_2():
    global instructions
    instructions = []
    with open("input") as f:
        for operation, argument in map(lambda x: x.split(), f):
            if operation != "acc":
                possibly_corrupt_indices.append(len(instructions))
            instructions.append((operation, int(argument)))


def find_value_in_accumulator():
    seen_indices = set()
    global accumulator
    accumulator = 0
    index = 0
    while index not in seen_indices:
        seen_indices.add(index)
        operation, argument = instructions[index]
        if operation == "jmp":
            index += argument
            continue
        if operation == "acc":
            accumulator += argument
        index += 1
    return accumulator


def find_value_in_accumulator_before_termination():
    for corrupt_index in possibly_corrupt_indices:
        corrupt_operation, corrupt_argument = instructions[corrupt_index]
        instructions[corrupt_index] = corrupt_map[corrupt_operation], corrupt_argument
        seen_indices = set()
        global accumulator
        accumulator = 0
        index = 0
        while index not in seen_indices and index < len(instructions):
            seen_indices.add(index)
            operation, argument = instructions[index]
            if operation == "jmp":
                index += argument
                continue
            if operation == "acc":
                accumulator += argument
            index += 1
        if index == len(instructions):
            break
        instructions[corrupt_index] = corrupt_operation, corrupt_argument
    return accumulator


if __name__ == "__main__":
    prepare_part_1()
    print("Part 1: %d" % find_value_in_accumulator())
    prepare_part_2()
    print("Part 2: %d" % find_value_in_accumulator_before_termination())

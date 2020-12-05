def find_highest_seat_id():
    return sorted(
        [
            int(line.translate(str.maketrans("FBLR", "0101")), 2)
            for line in open("input")
        ]
    )


def find_id_of_your_seat(sorted_seats):
    seat_set = set(range(sorted_seats[0], sorted_seats[-1]))
    [your_seat_id] = seat_set - set(sorted_seats)
    return your_seat_id


if __name__ == "__main__":
    part_1_answer = find_highest_seat_id()
    print("Part 1: %d" % max(part_1_answer))
    part_2_answer = find_id_of_your_seat(part_1_answer)
    print("Part 2: %d" % part_2_answer)

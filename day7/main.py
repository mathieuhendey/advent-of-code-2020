import re
from collections import defaultdict
from typing import Set, List, DefaultDict, Tuple

enclosing_bags_dict: DefaultDict[str, List[str]] = defaultdict(lambda: [])
enclosed_bags_dict: DefaultDict[str, Tuple[Tuple[int, str]]] = defaultdict(
    lambda: tuple()
)


def prepare_part_1():
    for line in open("input"):
        enclosing_bag = line.split(" bags contain ")[0]
        enclosed_bags: List[str] = re.findall(r"\d ([\w ]+) bag", line)

        for enclosed_bag in enclosed_bags:
            enclosing_bags_dict[enclosed_bag].append(enclosing_bag)


def prepare_part_2():
    for line in open("input"):
        enclosing_bags = line.split(" bags contain ")[0]
        enclosed_bag: List[Tuple[str, str]] = re.findall(r"(\d+) ([\w ]+) bag", line)
        enclosed_bags_dict[enclosing_bags] = tuple((int(a), b) for a, b in enclosed_bag)


def find_enclosing_bags(bag: str) -> Set[str]:
    return set().union(
        enclosing_bags_dict[bag],
        *(
            find_enclosing_bags(enclosing_bag)
            for enclosing_bag in enclosing_bags_dict[bag]
        ),
    )


def count_enclosed_bags(bag: str) -> int:
    return sum(
        enclosed_bag_count * (1 + count_enclosed_bags(enclosed_bag))
        for enclosed_bag_count, enclosed_bag in enclosed_bags_dict[bag]
    )


if __name__ == "__main__":
    prepare_part_1()
    print("Part 1: %d" % len(find_enclosing_bags("shiny gold")))
    prepare_part_2()
    print("Part 2: %d" % count_enclosed_bags("shiny gold"))

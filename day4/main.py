import re

regexes = {
    "byr": r"(19[2-8][0-9]|199[0-9]|200[0-2])",
    "iyr": r"(201[0-9]|2020)",
    "eyr": r"(202[0-9]|2030)",
    "hgt": r"((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)",
    "hcl": r"#([0-9]|[a-f]){6}",
    "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
    "pid": r"\d{9}",
    "cid": r".*",
}

required_values = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def count_valid_passports():
    count = 0
    passports_file_lines = open("input.txt", "r").read().split("\n\n")
    i = 0
    kv_dict = [{}]
    while i < len(passports_file_lines):
        passport_file_line: str = passports_file_lines[i].replace("\n", " ")
        passport = re.split(r" | \n", passport_file_line)
        passport.sort()
        passport = " ".join(passport)
        if not all(x in passport for x in required_values):
            passports_file_lines.pop(i)
        i += 1

    for passport_file_line in passports_file_lines:
        passport_file_line: str = passport_file_line.replace("\n", " ")
        passport = re.split(r" | \n", passport_file_line)
        passport.sort()
        passport = " ".join(passport)
        if all(x in passport for x in required_values):
            count += 1
            kv_dict.append(
                {k: v for k, v in [i.split(":", 1) for i in passport.split(" ")]}
            )
        while {} in kv_dict:
            kv_dict.remove({})
    print("Part 1: %d" % count)

    count = -1
    match = []
    for passport_dict in kv_dict:
        for required_value in required_values:
            match.append(
                bool(re.search(regexes[required_value], passport_dict[required_value]))
            )
        if all(match):
            count += 1
        match = []
    print("Part 2: %d" % count)


if __name__ == "__main__":
    count_valid_passports()

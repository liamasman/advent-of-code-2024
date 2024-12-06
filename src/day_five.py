from functools import cmp_to_key


def part_one(raw_input):
    rules, updates = parse_input(raw_input)
    return sum([get_middle_number(update) for update in
                get_valid_updates(rules, updates)])


def parse_input(raw_input):
    rules, updates = raw_input.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in
               updates.split("\n")]
    return rules, updates


def process_rules(rules):
    '''
    Generate a mapping of numbers to a set of numbers that must not occur
    after it
    '''
    rule_map = {}
    for rule in rules:
        restricted_numbers = set() if rule_map.get(rule[1]) is None else \
        rule_map[rule[1]]
        restricted_numbers.add(rule[0])
        rule_map[rule[1]] = restricted_numbers

    return rule_map


def is_valid_update(rules_map, update):
    seen_numbers = set()
    for number in update[::-1]:
        if rules_map.get(number) is not None:
            if seen_numbers.intersection(rules_map[number]):
                return False
        seen_numbers.add(number)
    return True


def get_middle_number(update):
    return update[len(update) // 2]


def get_valid_updates(rules, updates):
    rules_map = process_rules(rules)
    for update in updates:
        if is_valid_update(rules_map, update):
            yield update


def get_invalid_updates(must_not_occur_after_rules, updates):
    for update in updates:
        if not is_valid_update(must_not_occur_after_rules, update):
            yield update


def create_sort_function(must_not_occur_after_rules):
    def sort_function(a, b):
        if must_not_occur_after_rules.get(a) is not None and b in \
                must_not_occur_after_rules[a]:
            return 1
        elif must_not_occur_after_rules.get(b) is not None and a in \
                must_not_occur_after_rules[b]:
            return -1
        return 0

    return cmp_to_key(sort_function)


def correct_invalid_update(invalid_update, sort_function):
    invalid_update.sort(key=sort_function)
    return invalid_update


def correct_invalid_updates(must_not_occur_after_rules, updates):
    sort_function = create_sort_function(must_not_occur_after_rules)
    for invalid_update in get_invalid_updates(must_not_occur_after_rules,
                                              updates):
        yield correct_invalid_update(invalid_update, sort_function)


def part_two(raw_input):
    rules, updates = parse_input(raw_input)
    rules_map = process_rules(rules)
    return sum([get_middle_number(update) for update in
                correct_invalid_updates(rules_map, updates)])


if __name__ == "__main__":
    with open("../resources/Day5Input.txt", "r", encoding="UTF-8") as f:
        puzzle_input = f.read()
    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}")
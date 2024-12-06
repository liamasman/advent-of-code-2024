def part_one(raw_input):
    rules, updates = parse_input(raw_input)
    return sum([get_middle_number(update) for update in get_valid_updates(rules, updates)])

def parse_input(raw_input):
    rules, updates = raw_input.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]
    return rules, updates

def process_rules(rules):
    '''
    Generate a mapping of numbers to a set of numbers that must not occur after it
    '''
    rule_map = {}
    for rule in rules:
        restricted_numbers = set() if rule_map.get(rule[1]) is None else rule_map[rule[1]]
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


def part_two(raw_input):
    pass


if __name__ == "__main__":
    with open("../resources/Day5Input.txt", "r", encoding="UTF-8") as f:
        puzzle_input = f.read()
    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}")
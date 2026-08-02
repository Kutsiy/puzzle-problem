from pathlib import Path
import sys
import time


def find_longest_chain(number, begin_elements, used_numbers):
    best_answer = number
    end = number[-2:]

    for next_number in begin_elements.get(end, ()):

        if next_number in used_numbers:
            continue

        used_numbers.add(next_number)

        chain = find_longest_chain(
            next_number,
            begin_elements,
            used_numbers
        )

        candidate_length = len(number) + len(chain) - 2

        if candidate_length > len(best_answer):
            best_answer = number + chain[2:]

        used_numbers.remove(next_number)

    return best_answer


def find_answers(numbers, begin_elements):
    used_numbers = set()
    answers = []

    for number in numbers:
        used_numbers.clear()
        used_numbers.add(number)

        answers.append(
            find_longest_chain(
                number,
                begin_elements,
                used_numbers
            )
        )

    return answers


def load_numbers(filename):
    with Path(filename).open(encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def build_graph(numbers):
    begin_elements = {}

    for number in numbers:
        begin_elements.setdefault(number[:2], []).append(number)

    return begin_elements


def choose_file():
    if len(sys.argv) > 1:
        return sys.argv[1]

    filename = input("File (Enter = source.txt): ").strip()

    if not filename:
        filename = "source.txt"

    return filename


def main():
    start = time.perf_counter()

    filename = choose_file()

    numbers = load_numbers(filename)
    begin_elements = build_graph(numbers)

    answers = find_answers(numbers, begin_elements)

    print("Longest chain:")
    print(max(answers, key=len))

    print(f"Execution time: {time.perf_counter() - start:.3f} sec")


if __name__ == "__main__":
    main()
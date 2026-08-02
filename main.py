def find_longest_chain(number, begin_elements, used_numbers):
    end_element = f"{number[-2]}{number[-1]}"

    best_answer = number

    if end_element not in begin_elements:
        return best_answer

    if end_element in begin_elements:
        for next_number in begin_elements[end_element]:

            if next_number in used_numbers:
                continue

            used_numbers.append(next_number)

            chain = find_longest_chain(next_number, begin_elements, used_numbers)

            if len(number + chain[2:]) > len(best_answer):
                best_answer = number + chain[2:]

            used_numbers.remove(next_number)

    return best_answer

def find_answers(numbers, begin_elements):
    answer = ''
    answers = []
    used_numbers = []

    for num in numbers:

        used_numbers.clear()

        used_numbers.append(num)

        answer = find_longest_chain(num, begin_elements, used_numbers)

        answers.append(answer)


    return answers
    


def main():
    numbers = []
    begin_elements = {}

    with open("source.txt", "r", encoding="utf-8") as file:
        numbers = [line.strip() for line in file]

    for num in numbers:
        first_element = f"{num[0]}{num[1]}"

        if first_element  not in begin_elements:
            begin_elements[first_element] = []
        begin_elements[first_element].append(num)

    answers = find_answers(numbers, begin_elements)
    print(max(answers, key=len))

if __name__ == "__main__":
    main()

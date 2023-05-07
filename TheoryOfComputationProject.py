from collections import deque, Counter
from time import sleep


def print_table(table):
    for row in table:
        print(f"{row[0]:<15} {row[1]}")
    print()


def main():
    print("\nWelcome to our program!")
    print("\nIf you want to exit the loop please use 'q' as your input string")
    print(
        "This Pushdown Automata can recognize the CFL L={a^n b^n|n>=0} Please input a string to start: "
    )

    while True:
        step_counter = 0
        stack = []
        rule = ""
        ruleNumber = ""
        current_state = "p"
        string = input(f"Enter String Here: ")
        string = string.lower()

        if "q" in string:
            exit(f"Program finished!")

        # Queue of all the Elements in the Input String
        queue = deque(string)

        # validating the string (number of a's must equal number of b's)
        curr = Counter(string)
        if string and (curr["a"] != curr["b"] or "a" not in curr or "b" not in curr):
            print("This is an invalid string for L={a^n b^n|n>=0} Try Again!")
            continue

        print(f"========Table for: {string} ========\n")
        if queue:
            while queue or stack:
                # Rule 0
                if current_state == "p":
                    ruleNumber = "#0"
                    current_state = "q"
                    stack.append("s")
                    rule = "(p, e, e) → (q, S)"
                # Rule 1
                elif current_state == "q" and queue[0] == "$":
                    ruleNumber = "#1"
                    current_state = "q$"
                    queue.popleft()
                    rule = "(q, $, e) → (q$, e)"
                    queue.append("e")
                    stack.append("e")
                    break
                # Rule 2
                elif current_state == "q":
                    ruleNumber = "#2"
                    queue.popleft()
                    current_state = "qa"
                    rule = "(q, a, e) → (qa, e)"

                # Rule 3
                elif current_state == "q" and queue[0] == "b":
                    ruleNumber = "#3"
                    queue.popleft()
                    current_state = "qb"
                    rule = "(q, b, e) → (qb, e)"

                # Rule 4
                elif current_state == "qa" and stack[-1] == "a":
                    ruleNumber = "#4"
                    current_state = "q"
                    stack.pop()
                    rule = "(qa, e, a) → (q, e)"
                # Rule 5
                elif current_state == "qa" and stack[-1] == "s":
                    ruleNumber = "#5"
                    stack.pop()
                    stack.append("b")
                    stack.append("s")
                    stack.append("a")
                    rule = "(qa, e, S) → (qa, aSb)"

                # Rule 6
                elif current_state == "qb" and stack[-1] == "b":
                    ruleNumber = "#6"
                    stack.pop()
                    current_state = "q"
                    rule = "(qb, e, b) → (q, e)"
                # Rule 7
                elif current_state == "qb" and stack[-1] == "s":
                    ruleNumber = "#7"
                    stack.pop()
                    rule = "(qb, e, S) → (qb, e)"

                # Rule 8
                elif current_state == "q$" and stack[-1] == "s":
                    ruleNumber = "#8"
                    stack.pop()
                    rule = "(q, $, e) → (q$, e)"
                # Rule 9
                elif current_state == "q$":
                    ruleNumber = "#9"
                    rule = "(q$, e, S) → (q$, e)"

                # Generating a list to print the table after doing a step
                table = [
                    ["Step:", step_counter],
                    ["State:", current_state],
                    ["Unread Input:", "".join(list(queue))],
                    ["Stack:", "".join(list(stack[::-1]))],
                    ["Rule number:", ruleNumber],
                    ["Rule:", rule],
                ]
                print_table(table)
                step_counter += 1

            # Generating a list to print the table once the remaining string is empty
            table = [
                ["Step:", step_counter],
                ["State:", current_state],
                ["Unread Input:", "".join(list(queue))],
                ["Stack:", "".join(list(stack[::-1]))],
                ["Rule number:", ruleNumber],
                ["Rule:", rule],
            ]
            print_table(table)
        else:
            # Generating a list to print the table if the inputed string was an empty string
            if not string:
                queue.append("e")
                stack.append("e")
                current_state = "q"
                rule = "empty"
                table = [
                    ["Step:", step_counter],
                    ["State:", current_state],
                    ["Unread Input:", "".join(list(queue))],
                    ["Stack:", "".join(list(stack[::-1]))],
                    ["Rule number:", ruleNumber],
                    ["Rule:", rule],
                ]
                print_table(table)


if __name__ == "__main__":
    main()

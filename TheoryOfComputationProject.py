"""
Rules used in our program:

0. (p, e, e) → (q, S) 
1. (q, a, e) → (qa, e) 
2. (q, b, e) → (qb, e)
3. (qa, e, a) → (q, e)
4. (qa, e, S) → (qa, aSb)
5. (qb, e, b) → (q, e)
6. (qb, e, S) → (qb, e)
7. (q, $, e) → (q$, e)

"""
from collections import deque, Counter
from time import sleep


def print_table(table):
    print(
        f"{table[0][0]:<10} {table[0][1]:<10} {table[0][2]:<15} {table[0][3]:<15} {table[0][4]:<10}"
    )
    print("-" * 60)
    for row in table[1:]:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<15} {row[3]:<15} {row[4]:<10}")
    print()


def main():
    print("\nWelcome to our program!")
    print("\nIf you want to exit the loop please use 'q' as your input string")
    print("This PDA can recognize L={a^n b^n|n>=0}. Put a string to start: ")

    while True:
        step_counter = 0
        stack = []
        ruleNumber = ""
        current_state = "p"
        string = input(f"Enter String Here: ")
        string = string.lower()

        if "q" in string:
            exit(f"Program finished!")

        queue = deque(string)

        curr = Counter(string)
        if string and (curr["a"] != curr["b"] or "a" not in curr or "b" not in curr):
            print("This string is invalid!")
            continue

        if step_counter == 0 and len(string) > 0:
            table = [
                ["Step", "State", "Unread Input", "Stack", "Rule number"],
                [
                    step_counter,
                    "p",
                    "".join(list(queue)),
                    "".join(list(stack[::-1])),
                    "n/a",
                ],
            ]
            step_counter += 1

        if queue:
            while queue or stack:
                if current_state == "p":
                    ruleNumber = "#0"
                    current_state = "q"
                    stack.append("s")

                elif current_state == "q" and queue[0] == "a":
                    ruleNumber = "#1"
                    queue.popleft()
                    current_state = "qa"

                elif current_state == "q" and queue[0] == "b":
                    ruleNumber = "#2"
                    queue.popleft()
                    current_state = "qb"

                elif current_state == "qa" and stack[-1] == "a":
                    ruleNumber = "#3"
                    current_state = "q"
                    stack.pop()

                elif current_state == "qa" and stack[-1] == "s":
                    ruleNumber = "#4"
                    stack.pop()
                    stack.append("b")
                    stack.append("s")
                    stack.append("a")

                elif current_state == "qb" and stack[-1] == "b":
                    ruleNumber = "#5"
                    stack.pop()
                    current_state = "q"

                elif current_state == "qb" and stack[-1] == "s":
                    ruleNumber = "#6"
                    stack.pop()

                elif current_state == "q" and queue[0] == "$":
                    ruleNumber = "#7"
                    current_state = "q$"
                    queue.popleft()

                    queue.append("e")
                    stack.append("e")
                    break

                table.append(
                    [
                        step_counter,
                        current_state,
                        "".join(list(queue)),
                        "".join(list(stack[::-1])),
                        ruleNumber,
                    ]
                )
                step_counter += 1

            table.append(
                [
                    step_counter,
                    current_state,
                    "".join(list(queue)),
                    "".join(list(stack[::-1])),
                    ruleNumber,
                ]
            )
            print_table(table)
        else:
            if not string:
                queue.append("e")
                stack.append("e")
                current_state = "q"

                table = [
                    ["Step", "State", "Unread Input", "Stack", "Rule number"],
                    [
                        step_counter,
                        current_state,
                        "".join(list(queue)),
                        "".join(list(stack[::-1])),
                        ruleNumber,
                    ],
                ]
                print_table(table)


if __name__ == "__main__":
    main()

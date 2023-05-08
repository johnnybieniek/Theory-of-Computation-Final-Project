from collections import deque, Counter
from time import sleep

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


# function to print a table row
def print_table(table):
    for row in table:
        print(f"{row[0]:<15} {row[1]}")
    print("-------------------------")
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

        if step_counter == 0 and len(string) > 0:
            print(f"========Table for: {string} ========\n")
            table = [
                ["Step:", step_counter],
                ["State:", "p"],
                ["Unread Input:", "".join(list(queue))],
                ["Stack:", "".join(list(stack[::-1]))],
                ["Rule number:", "n/a"],
            ]
            print_table(table)
            print("-------------------------")
            step_counter += 1

        if queue:
            while queue or stack:
                # Rule 0
                if current_state == "p":
                    ruleNumber = "#0"
                    current_state = "q"
                    stack.append("s")

                # Rule 1
                elif current_state == "q" and queue[0] == "a":
                    ruleNumber = "#1"
                    queue.popleft()
                    current_state = "qa"

                # Rule 2
                elif current_state == "q" and queue[0] == "b":
                    ruleNumber = "#2"
                    queue.popleft()
                    current_state = "qb"

                # Rule 3
                elif current_state == "qa" and stack[-1] == "a":
                    ruleNumber = "#3"
                    current_state = "q"
                    stack.pop()

                # Rule 4
                elif current_state == "qa" and stack[-1] == "s":
                    ruleNumber = "#4"
                    stack.pop()
                    stack.append("b")
                    stack.append("s")
                    stack.append("a")

                # Rule 5
                elif current_state == "qb" and stack[-1] == "b":
                    ruleNumber = "#5"
                    stack.pop()
                    current_state = "q"

                # Rule 6
                elif current_state == "qb" and stack[-1] == "s":
                    ruleNumber = "#6"
                    stack.pop()

                # Rule 7
                elif current_state == "q" and queue[0] == "$":
                    ruleNumber = "#7"
                    current_state = "q$"
                    queue.popleft()

                    queue.append("e")
                    stack.append("e")
                    break

                # Generating a list to print the table after doing a step
                table = [
                    ["Step:", step_counter],
                    ["State:", current_state],
                    ["Unread Input:", "".join(list(queue))],
                    ["Stack:", "".join(list(stack[::-1]))],
                    ["Rule number:", ruleNumber],
                ]
                print_table(table)
                print("-------------------------")
                step_counter += 1

            # Generating a list to print the table once the remaining string is empty
            table = [
                ["Step:", step_counter],
                ["State:", current_state],
                ["Unread Input:", "".join(list(queue))],
                ["Stack:", "".join(list(stack[::-1]))],
                ["Rule number:", ruleNumber],
            ]
            print_table(table)
            print("-------------------------")
        else:
            # Generating a list to print the table if the inputed string was an empty string
            if not string:
                queue.append("e")
                stack.append("e")
                current_state = "q"

                table = [
                    ["Step:", step_counter],
                    ["State:", current_state],
                    ["Unread Input:", "".join(list(queue))],
                    ["Stack:", "".join(list(stack[::-1]))],
                    ["Rule number:", ruleNumber],
                ]
                print_table(table)


if __name__ == "__main__":
    main()

    

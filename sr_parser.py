# Grammar
productions = {
    "S": [["S", "+", "S"], ["id"]]
}

# Input string
input_string = ["id", "+", "id"]
stack = []

print("STACK\t\tINPUT\t\tACTION")

while True:
    # Shift if input remains
    if input_string:
        stack.append(input_string.pop(0))
        print(stack, "\t", input_string, "\t Shift")

    # Try Reduce
    reduced = True
    while reduced:
        reduced = False
        for head, bodies in productions.items():
            for body in bodies:
                if stack[-len(body):] == body:
                    stack = stack[:-len(body)]
                    stack.append(head)
                    print(stack, "\t\t", input_string, "\t\t Reduce:", head, "->", body)
                    reduced = True
                    break
            if reduced:
                break

    # Accept condition
    if stack == ["S"] and not input_string:
        print("\nString Accepted!")
        break
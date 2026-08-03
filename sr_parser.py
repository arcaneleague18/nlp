# Grammar
productions = {
    "S": [["S", "+", "S"], ["id"]]
}

def shift_reduce_parse(input_string):
    """
    Simple shift-reduce parser for grammar S -> S + S | id.
    Args:
        input_string (list): List of tokens (e.g., ['id', '+', 'id'])
    Returns:
        bool: True if string is accepted, False otherwise
    """
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
                    if len(stack) >= len(body) and stack[-len(body):] == body:
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
            return True
        # Error condition: cannot reduce and cannot shift
        if not input_string and not reduced and stack != ["S"]:
            print("\nString Rejected!")
            return False

if __name__ == "__main__":
    # Example parse
    result = shift_reduce_parse(["id", "+", "id"])

    def test_shift_reduce():
        assert shift_reduce_parse(["id"]) == True
        assert shift_reduce_parse(["id", "+", "id"]) == True
        assert shift_reduce_parse(["id", "+", "+"]) == False
        print("All shift-reduce parser tests passed.")

    test_shift_reduce()

def binary_search(arr) -> int:
    """
    Binary search algorithm template.
    Idea: Minimize k such that condition(k) is True.
    Adaptations:
    - Correctly initialize the boundary variables left and right: Set up the boundary to include all possible elements;
    - Decide return value: return left or return left - 1? Fact: after exiting the while loop, left is the minimal k satisfying the condition function;
    - Design the condition function.
    Another note: maximal k satisfying !condition(k) == (minimal k satisfying condition(k) - 1)
    """

    def condition(k) -> bool:
        pass

    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

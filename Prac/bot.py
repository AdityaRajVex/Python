# Robot starts at [0, 0] every time
# You are given an input: str, which is shows the actions that robot makes.
# if you find a U in input, move the robot up by 1, "D" down by 1, "L" left by 1, "R" right by 1.
# sample inputs: "ULDR", "GO TWO UP, THREE LEFT, SEVEN DOWN, x5 RIGHT"

def solution(A):
    # IMPLEMENT THIS FUNCTION
    x = 0
    y = 0
    if A:
        for i in A:
            if i == "U":
                y += 1
            elif i == "L":
                x -= 1
            elif i == "D":
                y -= 1
            elif i == "R":
                x += 1
    return (x,y)

# YOU CAN DEFINE TEST CASES BELOW, AND TEST
test1 = "uldr"
test2 = "GO TWO UP, THREE LEFT, SEVEN DOWN, x5 RIGHT"
test3 = "U"
test4 = "L"
test5 = "D"
test6 = "R"
test7 = None

print(solution(test1))
print(solution(test2))
print(solution(test3))
print(solution(test4))
print(solution(test5))
print(solution(test6))
print(solution(test7))

 (AERT)
# Data Structures - Unit 1 Assignment



# PART A: Stack ADT


class StackADT:
    def __init__(self):
        self.data = [] 

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty, nothing to pop!")
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def display(self):
        print("Stack (top -> bottom):", self.data[::-1])



# PART B: Factorial (Recursive)


def factorial(n):
    if n < 0:
        print("Invalid Input")
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)



 #PART B: Fibonacci - Naive Version


naive_call_count = 0

def fib_naive(n):
    global naive_call_count
    naive_call_count += 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_naive(n - 1) + fib_naive(n - 2)



#PART B: Fibonacci - Memoized Version


memo_call_count = 0

def fib_memo(n, memo={}):
    global memo_call_count
    memo_call_count += 1

    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


 #PART C: Tower of Hanoi



hanoi_moves_stack = StackADT()

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        hanoi_moves_stack.push(move)
        return
    hanoi(n - 1, source, destination, auxiliary)
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    hanoi_moves_stack.push(move)
    hanoi(n - 1, auxiliary, source, destination)


 #PART D: Recursive Binary Search


def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, key, mid + 1, high)
    else:
        return binary_search(arr, key, low, mid - 1)



#MAIN FUNCTION - runs all test cases


def main():
    print("=" * 60)
    print("   ALGORITHMIC EFFICIENCY & RECURSION TOOLKIT (AERT)")
    print("=" * 60)

    print("\n--- Part A: Stack ADT Demo ---")
    s = StackADT()
    s.push(10)
    s.push(20)
    s.push(30)
    print("After pushing 10, 20, 30:")
    s.display()
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("After pop:")
    s.display()
    print("Size:", s.size())
    print("Is empty?", s.is_empty())

    print("\n--- Part B: Factorial (Recursive) ---")
    for n in [0, 1, 5, 10]:
        result = factorial(n)
        print(f"  factorial({n}) = {result}")

    print("\n  Testing invalid input:")
    factorial(-3)


    print("\n--- Part B: Fibonacci (Naive vs Memoized) ---")
    print(f"{'n':<6} {'Result':<15} {'Naive Calls':<18} {'Memo Calls':<15}")
    print("-" * 55)

    test_vals = [5, 10, 20, 30]
    for n in test_vals:
        # reset counters before each test
        global naive_call_count, memo_call_count
        naive_call_count = 0
        memo_call_count = 0

        # clear memo dict for fair count
        fib_memo.__defaults__ = ({},)

        r1 = fib_naive(n)
        nc = naive_call_count

        fib_memo.__defaults__ = ({},)
        memo_call_count = 0
        r2 = fib_memo(n)
        mc = memo_call_count

        print(f"  {n:<4} {r1:<15} {nc:<18} {mc:<15}")

    # Part C: Tower of Hanoi
    print("\n--- Part C: Tower of Hanoi (N = 3) ---")
    hanoi(3, 'A', 'B', 'C')
    print(f"\n  Total moves stored in stack: {hanoi_moves_stack.size()}")

    # Part D: Binary Search 
    print("\n--- Part D: Recursive Binary Search ---")
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(f"  Array: {arr}")

    searches = [7, 1, 13, 2]
    for key in searches:
        idx = binary_search(arr, key, 0, len(arr) - 1)
        if idx != -1:
            print(f"  Search {key}: Found at index {idx}")
        else:
            print(f"  Search {key}: Not found (returned -1)")

    # empty list test
    print("\n  Empty list test:")
    empty_result = binary_search([], 5, 0, -1)
    print(f"  Search 5 in []: Returned {empty_result}")

    print("\n" + "=" * 60)
    print("   All test cases completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
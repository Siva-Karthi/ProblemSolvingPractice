def minimize_maximum(arr):
    """
    Minimizes the maximum value in an array where you can only shift values
    to the left (from index i to i-1).

    Time Complexity: O(N) where N is the length of the array.
    Space Complexity: O(1)
    """
    ans = 0
    prefix_sum = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Calculate the number of elements processed so far (1-based index equivalent)
        k = i + 1

        # Calculate the ceiling of (prefix_sum / k)
        # We use integer arithmetic: ceil(A/B) is equivalent to (A + B - 1) // B
        current_avg = (prefix_sum + k - 1) // k

        # The answer must be at least the ceiling average of any prefix we encounter
        if current_avg > ans:
            ans = current_avg

    return ans


if __name__ == "__main__":
    # Test with the provided example
    input_array = [1, 5, 7, 6]
    result = minimize_maximum(input_array)

    print(f"Input Array: {input_array}")
    print(f"Minimized Maximum: {result}")

    # Additional Test Cases
    assert minimize_maximum([10, 1]) == 10  # Can't move 10 to the right
    assert minimize_maximum([3, 7, 1, 6]) == 5  # (3+7)=10/2=5, (3+7+1)=11/3=4, (3+7+1+6)=17/4=5

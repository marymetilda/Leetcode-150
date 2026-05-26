def solution(nums):
    seen_numbers = set()

    for num in nums:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    
    return False

print(solution([1, 2, 3, 4, 3, 6]))
print(solution([1, 2, 3, 4, 6]))
print(solution([1, 2, 3, 4, 8, 8]))
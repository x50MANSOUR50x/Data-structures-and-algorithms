from collections import defaultdict

def bucket_sort(nums:list[int]) -> list[int]:
    number_count_hashmap = defaultdict(int)
    
    for number in nums:
        number_count_hashmap[number] += 1
    
  # the index is the count of the number and the number is stored in a list at the same index  
    count_number_list = [[] for _ in range(len(nums) + 1)]
    # count_number_list = [[]] * (len(nums) + 1)

    for number, count in number_count_hashmap.items():
        count_number_list[count].append(number)
    
    return count_number_list

print(bucket_sort([1, 2, 3, 4, 5, 6, 6, 4, 2, 1, 4, 3]))
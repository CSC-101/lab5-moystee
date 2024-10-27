import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.
   # Purpose: Compare if both inputs are equal to each other.
# Part 2
   # The function for Part 2 should be within the class in data.py.
   #Purpose: Delivers a string consisting of the time, hour, and second.
# Part 3
def time_add(time1: data.Time, time2: data.Time) -> data.Time:
    total_seconds = time1.second + time2.second
    total_minutes = time1.minute + time2.minute + total_seconds // 60
    total_hours = time1.hour + time2.hour + total_minutes // 60
    seconds = total_seconds % 60
    minutes = total_minutes % 60
    hours = total_hours % 24
    return data.Time(hours, minutes, seconds)
#Purpose: Add two time values by adding the hours, minutes, and seconds
# Part 4
def is_descending(j: list[float]) -> bool:
    if len(j) < 2:
        return True
    for i in range(len(j) - 1):
        if j[i] > j[i + 1]:
            return False
    return True
#Purpose: Determine if the list is descending or not with a True or False
# Part 5
def largest_between(nums: list[int], idx1: int, idx2: int) -> int:
    if idx1 > idx2 or idx1 < 0 or idx2 >= len(nums):
        return None # -> str
    biggest = idx1
    for i in range(idx1, idx2 + 1):
        if nums[i] > nums[biggest]:
            biggest = i
    return biggest
#[2,4,1],0,2
#Purpose: To find the largest index within two lower/upper bounds within an inputted list
# Part 6
def furthest_from_origin(points: list[data.Point]) -> [int]:
    if not points:
        return None
    max_distance = -1
    furthest_index = -1
    for i in range(len(points)):
        point = points[i]
        distance = (point.x ** 2 + point.y ** 2) ** 0.5
        if distance > max_distance:
            max_distance = distance
            furthest_index = points[i]
    return furthest_index
#Purpose: Returns the index of the point that is furthest away from the origin (0,0)

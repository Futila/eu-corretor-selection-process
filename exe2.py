def merge_intervals(intervals: list) -> list:

    if not intervals:
        return []
    
    # Sort intervals based on their start values
    intervals.sort(key=lambda x: x[0])
    
    # Initialize merged list with first interval
    merged_list = [intervals[0]]
    
    # Iterate through remaining intervals
    for current_interval in intervals[1:]:
        last_merged_interval = merged_list[-1]  # Get the last merged interval
        
        # Check for overlap between current and last merged interval
        if current_interval[0] <= last_merged_interval[1]:
            #Merge intervals by updating the end of the last interval
            merged_list[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
        else:
            #There is no overlap - add current interval to merged list
            merged_list.append(current_interval)
    
    return merged_list



#For testing purposes
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output must be: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))                     # Output must be: [[1, 5]]
print(merge_intervals([[1,2],[3,4],[5,6]]))                  # Output must be: [[1,2], [3,4], [5,6]]

def merge_sort(array):
    """Sorts the given array in ascending order using the merge sort algorithm.

    The merge sort algorithm follows the divide-and-conquer approach, dividing the input array
    into smaller subarrays, sorting those, and then merging them back together.

    Args:
        array: A list of elements to be sorted.

    Returns:
        A sorted list of elements.
    """
    
    if len(array) <= 1:
        return array  # An array of zero or one element is already sorted.

    # Divide the array into two halves.
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # Merge the two sorted halves.
    return merge(left_half, right_half)


def merge(left_half, right_half):
    """Merges two sorted lists into a single sorted list.

    This function takes two sorted lists and combines them into a single sorted list
    by repeatedly comparing the smallest elements from each list.

    Args:
        left_half: A sorted list of elements.
        right_half: A sorted list of elements.

    Returns:
        A sorted list of elements.
    """
    
    merged_list = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_list.append(left_half[i])
            i += 1
        else:
            merged_list.append(right_half[j])
            j += 1

    # Append any remaining elements from the left half.
    merged_list.extend(left_half[i:])  # Efficiently adds the rest of the left half.

    # Append any remaining elements from the right half.
    merged_list.extend(right_half[j:])  # Efficiently adds the rest of the right half.

    return merged_list


# Example usage:
if __name__ == "__main__":
    # Sample array to be sorted
    array = [5, 3, 2, 1, 4]
    
    # Sort the array using merge_sort function
    sorted_array = merge_sort(array)

    # Display the sorted array
    print("Sorted Array:", sorted_array)

def merge_sort(array):
  """Sorts the given array in ascending order using the merge sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  if len(array) <= 1:
    return array

  # Divide the array into two halves.
  mid = len(array) // 2
  left_half = merge_sort(array[:mid])
  right_half = merge_sort(array[mid:])

  # Merge the two sorted halves.
  return merge(left_half, right_half)


def merge(left_half, right_half):
  """Merges two sorted lists into a single sorted list.

  Args:
    left_half: A sorted list of elements.
    right_half: A sorted list of elements.

  Returns:
    A sorted list of elements.
  """

  merged_list = []
  i = 0
  j = 0
  while i < len(left_half) and j < len(right_half):
    if left_half[i] <= right_half[j]:
      merged_list.append(left_half[i])
      i += 1
    else:
      merged_list.append(right_half[j])
      j += 1

  # Add any remaining elements from the left half of the array.
  while i < len(left_half):
    merged_list.append(left_half[i])
    i += 1

  # Add any remaining elements from the right half of the array.
  while j < len(right_half):
    merged_list.append(right_half[j])
    j += 1

  return merged_list


# Example usage:

array = [5, 3, 2, 1, 4]

sorted_array = merge_sort(array)

print(sorted_array)

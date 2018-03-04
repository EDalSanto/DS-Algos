class BinarySearch
  # NOTE: assumes sorted list
  def self.iterative(list, item)
    left = 0
    right = list.size - 1

    while left <= right
      mid = (left + right) / 2
      current = list[mid]

      if current == item
        return true
      elsif current > item
        # Look at bottom half of list
        right = mid - 1
      else # current < item
        # Look at top half of list
        left = mid + 1
      end
    end

    return false
  end

  def self.recursive(list, item, left, right)
    return false if left > right

    # left + ((right - left) / 2) avoids potential for overflow
    mid = (left + right) / 2

    if list[mid] == item
      return true
    elsif item < list[mid]
      # First half of list not including midpoint
      return recursive(list, item, left, mid - 1)
    else
      # Second half of list not including midpoint
      return recursive(list, item, mid + 1, right)
    end
  end

  def self.matrix(matrix, item)
    matrix.any? { |sub_list| iterative(sub_list, item) }
  end
end

class BinarySearch
  # NOTE: assumes sorted list
  #
  def self.iterative(list, item)
    right = list.size - 1
    left = 0

    while left <= right
      mid = (right + left) / 2
      current = list[mid]

      if current == item
        return true
      elsif current > item
        # Look at bottom half of list
        right = mid - 1
      else
        # Look at bottom half of list
        left = mid + 1
      end
    end

    return false
  end

  def self.recursive(list, item)
    return false if list.empty?

    mid = list.size / 2

    if list[mid] == item
      return true
    elsif item < list[mid]
      # First half of list not including midpoint
      return recursive(list[0...mid], item)
    else
      # Second half of list not including midpoint
      return recursive(list[(mid + 1)...list.size], item)
    end
  end

  def self.matrix(matrix, item)
    return false if matrix[0].empty?

    right = matrix.size - 1
    left = 0

    while left <= right
      mid = (right + left) / 2
      sub_list = matrix[mid]

      if item.between?(sub_list.min, sub_list.max)
        return iterative(sub_list, item)
      elsif item == sub_list.min || item == sub_list.max
        return true
      elsif item < sub_list.min
        # Look at bottom half of list
        right = mid - 1
      else
        # Look at bottom half of list
        left = mid + 1
      end
    end

    return false
  end
end

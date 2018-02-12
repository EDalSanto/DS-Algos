class BinarySearch
  # NOTE: assumes sorted list
  def self.iterative(list, item)
    max = list.size - 1
    min = 0

    while min != max
      mid = (max + min) / 2
      current = list[mid]

      if current == item
        return true
      elsif current > item
        # Look at bottom half of list
        max = mid
      else
        # Look at bottom half of list
        min = mid + 1
      end
    end

    return false
  end

  def self.recursive(list, item)
    if list.empty?
      return false
    end

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
end

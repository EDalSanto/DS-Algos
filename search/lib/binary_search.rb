class BinarySearch
  def initialize(list)
    @list = list
  end

  def search(item)
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

  private

  attr_reader :list
end

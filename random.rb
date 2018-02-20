# Balanced parenthesis

# ex. ((())))
def balanced_parens?(expression)
  stack = []
  opening_parens = "("
  closing_parens = ")"

  expression.chars.each do |parens|
    if parens == opening_parens
      stack.push(parens)
    else
      return false if stack.empty?
      stack.pop
    end
  end

  stack.empty?
end

#puts balanced_parens?("(") == false
#puts balanced_parens?(")") == false
#puts balanced_parens?("((") == false
#puts balanced_parens?("()") == true
#puts balanced_parens?("(((())))") == true
#puts balanced_parens?("(()()))") == false
#puts balanced_parens?("(()()())") == true

# Perfect Square => exists a number N that N times itself equals target
# Use binary search and instead current * current will match target
def perfect_square?(target)
  high = target / 2
  low  = 1

  while low <= high
    current = (high + low) / 2

    if current * current == target
      return true
    elsif current * current < target
      low = current + 1
    else
      high = current - 1
    end
  end

  false
end

#puts perfect_square?(25) == true
#puts perfect_square?(125) == false
#puts perfect_square?(100) == true
#puts perfect_square?(3) == false

# Raise base to power
def exp(n , p)

end

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

puts balanced_parens?("(") == false
puts balanced_parens?(")") == false
puts balanced_parens?("((") == false
puts balanced_parens?("()") == true
puts balanced_parens?("(((())))") == true
puts balanced_parens?("(()()))") == false
puts balanced_parens?("(()()())") == true

# Recursive Backtracking Search
## Pseudo
```
function Backtracking-Search(csp) returns a solution, or failure
  return Recursive-Backtracking({}, csp)

function Recursive-Backtracking(assignment, csp) returns a solution or failure
  if assignment is complete then return assignment
  var <- select-unassigned-variable(variables[csp], assignment, csp)
  for each value in order-domain-values(var, assignment, csp) do
    if value is consistent with assignment according to Constraints[csp] then
      add { var = value } to assignment
      result <- Recursive-Backtracking(assignment, csp)
      if result != failure then return result
      remove { var = value } from assignment
   return failure
```
## Plain English
* Define Base Case
* Iterate through all possible states
* Explore some path if valid path
* If path leads to solved result
* Else backtrack
* Return negative results if no state works out

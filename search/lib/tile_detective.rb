class TileDetective
  TILE = [
    [ true, true ],
    [ false, true ]
  ]

  # Given a square and a missing point in the square
  def self.solve(square, missing_point)
    # Base case:
    #   square.size is equal to 2
    #   rotate tile until fit
    #     fit => all trues in square
    #       if already true, leave it
    #   place tile
    #
    # otherwise, divide square into 4 equal subsquares of the same problem
    #   place tile in center such that each subsquare now has a missing point => you now have 4 identical subproblems
    #   recursively call solve on:
    #     square_size / 2, p1
    #     square_size / 2, p2
    #     square_size / 2, p3
    #     square_size / 2, p4
    #
  end

  def self.rotate_tile
    # Figure out how to rotate matrix by 90 degrees
  end
end

class TileDetective

  def self.new_tile
    [
      [ true, true ],
      [ false, true ]
    ]
  end

  # Given a square and a missing point in the square
  def self.solve(square, missing_point)
    ## Not super optimized

    n = square.size

    # Base case: square.size is equal to 2
    if n == 2
      tile = new_tile

      # rotate tile until fit
      while (tile[missing_point[0]][missing_point[1]] == true) do
        rotate(tile)
      end

      # place tile in right place
      for i in (0...2)
        for j in (0...2)
          # Skip filled in 1
          next if [i, j] == missing_point

          square[i][j] = tile[i][j]
        end
      end
    else # divide square into 4 equal subsquares of the same problem
      # place tile in center
      y = ((n / 2) - 1)
      center_square = [
        [ y, y ],
        [ y, y + 1 ],
        [ y + 1, y ],
        [ y + 1, y + 1]
      ]
      filled_quadrant = if missing_point[0] >= n /  2
        #...
                        end
    end

    #   place tile in center such that each subsquare now has a missing point => you now have 4 identical subproblems
    #   recursively call solve on:
    #     square_size / 2, p1
    #     square_size / 2, p2
    #     square_size / 2, p3
    #     square_size / 2, p4
    #
  end

  # Rotate matrix in place
  def self.rotate(tile)
    # Exchange top rows
    tile.reverse!

    # Swap corresponding rows
    for i in (0...tile.length)
      for j in ((i + 1)...tile[i].length)
        tile[i][j], tile[j][i] = tile[j][i], tile[i][j]
      end
    end
  end
end

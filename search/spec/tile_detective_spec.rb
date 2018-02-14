require "tile_detective"

describe TileDetective do
  describe ".solve" do
    it "returns a finished 2 x 2 board" do
      square = [
                 [ false, false ],
                 [ false, true ]
              ]

      described_class.solve(square, [1, 1])

      expect(square).to eq(
        [
          [true, true],
          [true, true]
        ]
      )
    end

    it "returns a finished board" do
      square = [
                 [ false, false ],
                 [ false, true ],
                 [ false, false ],
                 [ false, false ]
              ]
      expect described_class.solve(square, [1, 1]).to eq(
        [
          [ true, true ],
          [ true, true ],
          [ true, true ],
          [ true, true ]
        ]
      )
    end
  end

  describe ".rotate" do
    it "rotates a matrix" do
      matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
      ]

      described_class.rotate(matrix)

      expect(matrix).to eq(
        [
          [ 7, 4, 1 ],
          [ 8, 5, 2 ],
          [ 9, 6, 3 ]
        ]
      )
    end
  end
end

require "tile_detective"

describe TileDetective do
  it "returns a finished board" do
    square = [
               [ false, false ],
               [ false, true ]
            ]
    expect described_class.solve(square, [1, 1]).to eq(
      [
        [true, true],
        [true, true]
      ]
    )
  end

  it "returns a finished board" do
    square = [
               [ false, false ],
               [ false, true ]
               [ false, false ],
               [ false, false ]
            ]
    expect described_class.solve(square, [1, 1]).to eq(
      [
        [ true, true ],
        [ true, true ]
        [ true, true ],
        [ true, true ]
      ]
    )
  end
end

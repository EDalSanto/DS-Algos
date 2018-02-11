require "binary_search"

describe BinarySearch do
  describe "#search" do
    context "even number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
        @binary_detective = BinarySearch.new(@nums)
      end
      it "returns true if a number is found in the list" do
        expect(@binary_detective.search(2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(@binary_detective.search(5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(@binary_detective.search(30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(@binary_detective.search(11)).to eq(false)
      end
    end

    context "odd number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        @binary_detective = BinarySearch.new(@nums)
      end
      it "returns true if a number is found in the list" do
        expect(@binary_detective.search(2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(@binary_detective.search(5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(@binary_detective.search(30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(@binary_detective.search(11)).to eq(false)
      end
    end
  end
end

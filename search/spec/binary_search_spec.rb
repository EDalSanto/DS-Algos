require "binary_search"

describe BinarySearch do
  describe ".iterative" do
    context "even number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.iterative(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.iterative(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.iterative(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.iterative(@nums, 11)).to eq(false)
      end
    end

    context "odd number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.iterative(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.iterative(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.iterative(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.iterative(@nums, 11)).to eq(false)
      end
    end
  end

  describe ".recursive" do
    context "even number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.recursive(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.recursive(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.recursive(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.recursive(@nums, 11)).to eq(false)
      end
    end

    context "odd number list length" do
      before do
        @nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.recursive(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.recursive(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.recursive(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.recursive(@nums, 11)).to eq(false)
      end
    end
  end

  describe ".matrix" do
    context "even number list length" do
      before do
        @nums = [
                  [ 1, 2, 3 ],
                  [ 4, 5, 6 ],
                  [ 7, 8 ]
                ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.matrix(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.matrix(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.matrix(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.matrix(@nums, 11)).to eq(false)
      end
    end

    context "odd number list length" do
      before do
        @nums = [
                  [ 1, 2, 3 ],
                  [ 4, 5, 6 ],
                  [ 7, 8, 9 ]
                ]
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.matrix(@nums, 2)).to eq(true)
      end

      it "returns true if a number is found in the list" do
        expect(BinarySearch.matrix(@nums, 5)).to eq(true)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.matrix(@nums, 30)).to eq(false)
      end

      it "returns false if not found in the list" do
        expect(BinarySearch.matrix(@nums, 11)).to eq(false)
      end
    end
  end
end

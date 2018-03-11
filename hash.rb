# How Ruby Implements a Hash Iteration

class LinearHash
  attr_reader :table

  def initialize
    @table = []
  end

  def [](key)
    # entries look like [key, value]
    find(key).last
  end

  def find(key)
    # Enumerable#find here will return the first entry that makes
    # our block return true, otherwise it returns nil.

    table.find do |entry|
      entry.first == key
    end
  end

  def []=(key, value)
    entry = find(key)

    if entry
      # If we already have it, just change value
      entry[1] = value
    else
      # Otherwise add a new entry
      @table << [key, value]
    end
  end
end


# nearly 4000 times slower than Hash with linear search
# pairing numbers to index would give us a fast way for lookup but hash can't be limited to number keys => need way to turn keys into numbers in a consistent way
# Object#hash => hash function return unique(ish) integers for any object in Ruby
  # hash values are huge and sometimes negative, so mod by small number to find index for element in table
  # creates issue where much smaller range of buckets for entries, meaning much, much more likely to have collision
  # solution: instead of entries being stored directly in table, we'll put them inside arrays called "bins"
    # each bin will end up having multiple entries but much faster than traversing entire table


class BinsHash
  NUM_BINS = 11

  def initialize
    # we know array will always have index between 0 and 10
    # so initialize with num_bins array
    @table = Array.new(NUM_BINS) { [] }
  end

  def [](key)
    # entries look like [key, value]
    find(key).last
  end

  def []=(key, value)
    entry = find(key)

    if entry
      # If we already have it, just change value
      entry[1] = value
    else
      # Otherwise add a new entry to bin
      bin_for(key) << [key, value]
    end
  end

  private

  attr_reader :table

  def find(key)
    # Enumerable#find here will return the first entry that makes
    # our block return true, otherwise it returns nil.

    bin_for(key).find do |entry|
      entry.first == key
    end
  end

  def bin_for(key)
    table[index_for(key)]
  end

  def index_for(key)
    key.hash % NUM_BINS
  end
end

# using bins descreased time for insert/serach by 90%
# still, we have 10_000 items and only 11 bins whichs means bins are becoming quite full
# increasing bin size spreads out items in bucket and improves performance by anoth 25%
# don't need to use prime numbers anymore for bucket size with good hash function

# ruby stdlib hash
  # default max density size (number of entries in bin)
    # number of entries to allow before rehashing: choosing the next largest power of 2 and recreating the hash table with new, larger size
  # default init_bin_size

class RehashHash
  STARTING_BINS = 16
  MAX_DENSITY = 5

  def initialize
    @entry_count = 0
    @bin_count = STARTING_BINS
    @table = Array.new(@bin_count) { [] }
  end

  def [](key)
    # entries look like [key, value]
    find(key).last
  end

  def []=(key, value)
    entry = find(key)

    if entry
      # If we already have it, just change value
      entry[1] = value
    else
      grow if full?

      # Otherwise add a new entry to bin
      bin_for(key) << [key, value]
      @entry_count += 1
    end
  end

  private

  attr_reader :table

  def grow
    # use bit shifting to get the next power of 2 to resize table
    @bin_count = @bin_count << 1

    # create a new table with a much larger number of bins
    new_table = Array.new(@bin_count) { [] }

    # copy each of the existing entries into the new table at their new location
    # using the index_of(key) => rehashing
    table.flatten(1).each do |entry|
      new_table[index_for(entry.first)] << entry
    end

    # Overwrite existing table with new
    @table = new_table
  end

  def full?
    # our bins / table are full when the number of entries surpasses MAX_DENSITY times number of entries
    @entry_count > MAX_DENSITY * @bin_count
  end

  def find(key)
    # Enumerable#find here will return the first entry that makes
    # our block return true, otherwise it returns nil.

    bin_for(key).find do |entry|
      entry.first == key
    end
  end

  def bin_for(key)
    table[index_for(key)]
  end

  def index_for(key)
    # use @bin_count now because it resizes whole table
    key.hash % @bin_count
  end
end

require "benchmark"

legacy = Hash.new
rehash_hash = RehashHash.new
bins_hash = BinsHash.new
linear_hash = LinearHash.new

n = 10_000

def set_and_find(target, key)
  target[key] = rand
  target[key]
end

Benchmark.bm do |x|
  x.report("Hash: ") { n.times { |t| set_and_find(legacy, t) } }
  x.report("Rehash: ") { n.times { |t| set_and_find(rehash_hash, t) } }
  x.report("Bins: ") { n.times { |t| set_and_find(bins_hash, t) } }
  x.report("Linear: ") { n.times { |t| set_and_find(linear_hash, t) } }
end

#           user     system      total      real
# Hash:   0.000000   0.000000   0.000000 (0.002318)
# Rehash: 0.020000   0.000000   0.020000 (0.024466)
# Bins:   0.800000   0.010000   0.810000 (0.794712)
# Linear: 8.610000   0.010000   8.620000 (8.613498)

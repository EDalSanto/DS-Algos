class PrimeHashFunction
  def self.call(input_string)
    hash = 0
    prime_number = 31

    input_string.chars.each do |char|
      hash = (prime_number * hash) + char.ord
    end

    hash
  end
end

class HashItem
  attr_reader :key, :vaue, :next, :previous

  def initialize(key, value)
    @key = key
    @value = value
    @next = nil
    @previous = nil
  end
end

class LinkedList
  attr_reader :head, :tail, :size

  def initialize
    @head = nil
    @tail = nil
    @size = 0
  end

  def add_node(new_hash_item)
    if @size == 0
      # Initialize list
      @head = new_hash_item
      @tail = new_hash_item
    elsif existing_node_for(new_hash_item.key)
      # update value
      existing_node_for(new_hash_item.key).value = new_hash_item.value
    else
      # add new hash item as tail
      old_tail = @tail
      old_tail.next = new_hash_item
      new_hash_item.previous = old_tail
      @tail = new_hash_item
    end

    @size += 1
  end

  def remove_node(key)
    node = search_node(key)

    # no node for key in list
    return nil unless node

    # if head node, shift head to current head next
    if node == @head
      @head = node.next
    end

    # if not last node, next previous points at node previous
    if node.next
      node.next.previous = node.previous
    end

    # if not first node, previous next points at node next
    if node.previous
      node.previous.next = node.next
    end

    @size -= 1
  end

  def search_node(key)
    current = @head

    while current
      if current.key == key
        return current
      else
        current = current.ext
      end
    end

    return nil
  end
end

class LinearHash
  attr_reader :table

  def initialize
    @table = []
  end

  def search(key)
    # entries look like [key, value]
    find(key).last
  end

  def insert(key, value)
    entry = find(key)

    if entry
      # If we already have it, just change value
      entry[1] = value
    else
      # Otherwise add a new entry
      @table << [key, value]
    end
  end

  def delete(key, value)
    @table.delete([key, value])
  end

  private

  def find(key)
    # Enumerable#find here will return the first entry that makes
    # our block return true, otherwise it returns nil.

    table.find do |entry|
      entry.first == key
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
    @table = Array.new(NUM_BINS) { LinkedList.new }
  end

  def search(key)
    # entries are nodes in linked list in specific bin
    find(key)
  end

  def insert(key, value)
    list = bin_for(key)
    entry = list.search_node(key)

    if entry
      # If we already have it, just change value
      entry.value = value
    else
      # Otherwise add a new entry to end of list
      list.add_node(HashItem.new(key, value))
    end
  end

  def delete(key)
    list = bin_for(key)
    list.remove_node(key)
  end

  private

  attr_reader :table

  def find(key)
    list = bin_for(key)
    list.search_node(key)
  end

  # Returning list
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
    @table = Array.new(@bin_count) { LinkedList.new }
  end

  def search(key)
    # entries are nodes in linked list in specific bin
    find(key)
  end

  def insert(key, value)
    list = bin_for(key)
    entry = list.search_node(key)

    if entry
      # If we already have it, just change value
      entry.value = value
    else
      grow if full?

      # Otherwise add a new entry to end of list
      list.add_node(HashItem.new(key, value))
      @entry_count += 1
    end
  end

  def delete(key)
    list = bin_for(key)
    list.remove_node(key)
  end

  private

  attr_reader :table

  def grow
    # use bit shifting to get the next power of 2 to resize table
    @bin_count = @bin_count << 1

    # create a new table with a much larger number of bins
    new_table = Array.new(@bin_count) { LinkedList.new }

    # copy each of the existing entries into the new table at their new location
    # using the index_of(key) => rehashing
    table.each do |list|
      new_table[index_for(list.key)] << list
    end

    # Overwrite existing table with new
    @table = new_table
  end

  def full?
    # our bins / table are full when the number of entries surpasses
    # MAX_DENSITY * number_of_entries
    @entry_count > MAX_DENSITY * @bin_count
  end

  def find(key)
    list = bin_for(key)
    list.search_node(key)
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

# Open Addressing
hash = {a: 10, b: 20, c: 30, d: 40}
# Ruby creates 2 arrays
entries = [
  [hash_value_a,:a,10],
  [hash_value_b,:b,20],
  [hash_value_c,:c,30],
  [hash_value_d,:d,40]
]

# Maps key to index in entries array
bins = [
  3,
  nil,
  nil,
  nil,
  1,
  nil,
  nil,
  nil,
  5,
  0,
  nil,
  nil,
  nil,
  nil,
  2,
  nil
]

# example add new entry
hash[:e] = 42
# Find hash using ruby's internal hash function
hash_of_e = e.hash
# append entry to entries array and notes index where stored
entries << [hash_of_e, :e, 42]
entries_index = entries.size - 1
# finds bin location for key-index reference corresponding to entry in entries array
bin_index = find_bin_for(hash_of_c)
# takes index and looks up entry
bins[bin_index] = entries_index

# example lookup
hash[:e]
# Find hash using ruby's internal hash function
hash_of_e = e.hash
# finds bin location for key-index reference
bin_index = find_bin_for(hash_of_e)
# looks up index in bins
entries_index = bins[bin_index]
# takes index and looks up entry
entry = entries[entries_index]
# can find value
entry.last => 42

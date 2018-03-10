/**
   Another "non-cryptographic" hash -- instead of bit shifting we multiply
   by a small prime number then uses a bitwise or to coerse the output to
   a 32bit integer.
 */
const DEFAULT_HASH_FUNCTION = function(inputString) {
  let hash = 0;
  let primeNumber = 31;
  for (let i = 0; i < inputString.length; i++) {
    let charCode = inputString.charCodeAt(i)
    hash = (primeNumber * hash) + charCode;
    hash |= 0; //Cast to 32 bits, significantly improves collision rate
    // ?
  }

  return hash;
}

// Store a HashItem at each location... why?
// - keep track of keys
// - helps to resolve collisions because we can compare the key values to tell
//   if a collision is data at the SAME key or just a hash collision..
// - update key value in list

class HashItem {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.next = null;
    this.previous = null;
  }
}

class List {
  constructor() {
    this.__head = null;
    this.__tail = null;
    this.size = 0;
  }

  addNode(hashItem) {
    let existingNode = this.findNodeFor(hashItem.key)

    if (this.emptyList()) {
      this.__head = hashItem;
      this.__tail = hashItem;
    } else if (existingNode) {
      // Update value for key
      existingNode.value = hashItem.value;
    } else {
      // new hash item is new tail
      let oldTail = this.__tail;
      oldTail.next = hashItem;
      hashItem.previous = oldTail;
      this.__tail = hashItem;
    }

    this.size++;
  }

  findNodeFor(key) {
    let current = this.__head;

    while (current) {
      if (current.key === key) {
        return current;
      } else {
        current = current.next;
      }
    }

    // Key does not exist
    return undefined;
  }

  removeNode(key) {
    let node = this.findNodeFor(key);

    // No node for key in list
    if (node === undefined) { return undefined; }

    // Shift head node if head
    if (node === this.__head) {
      this.__head = node.next;
    }

    // If not LAST node
    if (node.next) {
      node.next.previous = node.previous;
    }

    // If not FIRST node
    if (node.previous) {
      node.previous.next = node.next;
    }

    this.size--;
  }

  emptyList() {
    return this.size === 0;
  }
}

class HashTable {

  /**
    Constructs a new HashTable with a fixed size. This

    @param {integer} size - the size of HashTable
    @param {Function} hashFunction - a function which accepts string input and returns an integer
  */
  constructor(size = 32, hashFunction = DEFAULT_HASH_FUNCTION) {
    // Tests rely on the name this.__array being the location used for storage.
    this.__array = new Array(size);
    this.size = size;
    this.hashFunction = hashFunction;
  }


  /**
    set any data to the HashTable, storing the passed value at the passed key.

    @param {string} key
    @param {any} value
  */
  set(key, value) {
    let hashItem = new HashItem(key, value);

    // compute hash and mod by size get index
    let index = this.indexFor(key);

    // check if list already allocated at current index
    let list = this.__array[index];

    if (list) {
      list.addNode(hashItem);
    } else {
      list = new List();
      list.addNode(hashItem);
      this.__array[index] = list;
    }
  }

  /**
  setetrieve the value stored at the passed key. If the key contains no data, return undefined.

    @param {string} key
  */
  get(key) {
    let index = this.indexFor(key);
    let list = this.__array[index];

    if (list) {
      let node = list.findNodeFor(key);

      if (node) {
        return node.value;
      } else { // Key doesn't exist in list
        return undefined;
      }
    } else { // No list at that index yet
      return undefined;
    }
  }

  /**
    Remove the item associated with the passed key by setting the associated value to undefined.

    @param {string} key
  */
  remove(key) {
    let index = this.indexFor(key);
    let list = this.__array[index];

    if (list) {
      list.removeNode(key);
    } else {
      return undefined;
    }
  }

  indexFor(key) {
    return this.hashFunction(key) % this.size;
  }
}

module.exports = HashTable;

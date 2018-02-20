class Trie {
  constructor(character = '', isWord = false) {
    this.character = character; // The character this node represents
    this.isWord = isWord;       // Marks the path to this node as a word path
    this.children = {};         // Maps characters to Tries
  }

  /*
    Given a word, add it to the this trie
  */
  addWord(word) {

  }

  /*
    Given a word as a string, determine if that word is in this trie
  */
  containsWord(word) {

  }

  /*
    Given a prefix as a string, return a list of all words that start
    with this prefix
  */
  autoComplete(prefix, currentPath = '') {

  }
}

// Main... simple simple tests
let words = ['cat', 'car', 'camera', 'dog', 'domain']
let dictionary = new Trie();

for(let word of words) {
  dictionary.addWord(word);
}

let allFound = true;
for(let word of words) {
  let found = dictionary.containsWord(word);
  if(!found) {
    allFound = false;
    console.log(`Failed to find: ${word}`);
  }
}

if(allFound) {
  console.log("add and contains seems to work!");
}

console.log(dictionary.autoComplete('c'))
console.log(dictionary.autoComplete('b'))
console.log(dictionary.autoComplete('dom'))

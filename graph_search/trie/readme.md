# Implement a Trie

In this exercise you'll be implementing a simple Trie in Javascript. The Trie interface has 3 functions:

* `addWord(word)` which should make a series of new Trie objects and connect them appropriately such that `word` is now a member of the Trie.
* `containsWord(word)` which should return true if the Trie in question has had `word` added to it previously.
* `autoComplete(prefix)` which should return an array of all the words in the Trie beginning with `prefix`.

In this implementation, each node in the Trie should also be an instance of a Trie. A simple "test suite" has been provided -- to run it simply:

```
node trie-incomplete.js

# Initially the tests should tell you:
Failed to find: cat
Failed to find: car
Failed to find: camera
Failed to find: dog
Failed to find: domain
undefined
undefined
undefined

# A working solution:
add and contains seems to work!
[ 'cat', 'car', 'camera' ]
[]
[ 'domain' ]
```

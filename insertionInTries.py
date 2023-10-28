def insert_key(root, key): 
	# Initialize the currentNode pointer 
	# with the root node 
	currentNode = root 

	# Iterate across the length of the string 
	for c in key: 
		# Check if the node exist for the current 
		# character in the Trie. 
		if currentNode.childNode[ord(c) - ord('a')] == None: 
			# If node for current character does not exist 
			# then make a new node 
			newNode = TrieNode() 

			# Keep the reference for the newly created 
			# node. 
			currentNode.childNode[ord(c) - ord('a')] = newNode 

		# Now, move the current node pointer to the newly 
		# created node. 
		currentNode = currentNode.childNode[ord(c) - ord('a')] 

	# Increment the wordEndCount for the last currentNode 
	# pointer this implies that there is a string ending at 
	# currentNode. 
	currentNode.wordCount += 1

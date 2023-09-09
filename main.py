# Import TreeNode class and story_data from respective files
from tree_node import TreeNode
from story_data import story_data

def main():
    # Create the root node with the initial story piece
    story_root = TreeNode(story_data[0][0], story_data[0][1])

    # Print the initial story piece
    print("Once upon a time...")
    print(story_root.story_piece)

    # Begin the story traversal
    story_root.traverse()

# Check if this file is being run directly
if __name__ == "__main__":
    main()

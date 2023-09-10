# Import TreeNode class and story_data from respective files
from story_data import story_data
from tree_node import TreeNode

def main():
    # Create the root node with the initial story piece
    story_root = TreeNode(story_data.story_piece, story_data.choices)

    # Print the initial story piece
    print("Once upon a time...")
    print(story_root.story_piece)

    # Begin the story traversal
    story_root.traverse()

# Check if this file is being run directly
if __name__ == "__main__":
    main()
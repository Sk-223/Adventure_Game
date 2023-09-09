# Define a class called TreeNode to represent nodes in the story tree
class TreeNode:
    # Constructor method to initialize a node with a story piece and choices
    def __init__(self, story_piece, choices=[]):
        self.story_piece = story_piece
        self.choices = choices

    # Method to add a child node (choice) to the current node
    def add_child(self, node):
        self.choices.append(node)

    # Method to traverse the story tree based on user input
    def traverse(self):
        story_node = self
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ["1", "2"]:
                print("Invalid choice. Try again.")
            else:
                chosen_index = int(choice) - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child

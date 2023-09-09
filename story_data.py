# Define the story data as a list of tuples, each containing a story piece and choices
story_data = [
    ("""
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!
    Do you: 
    1 ) Roar back!
    2 ) Run to the left...
    """, [
        ("""
        The bear returns and tells you it's been a rough week. After making peace with
        a talking bear, he shows you the way out of the forest.

        YOU HAVE ESCAPED THE WILDERNESS.
        """, []),
        ("""
        The bear returns and tells you that bullying is not okay before leaving you alone
        in the wilderness.

        YOU REMAIN LOST.
        """, [])
    ]),
    ("""
    The bear is startled and runs away.
    Do you:
    1 ) Shout 'Sorry bear!'
    2 ) Yell 'Hooray!'
    """, [
        ("""
        The bear returns and tells you it's been a rough week. After making peace with
        a talking bear, he shows you the way out of the forest.

        YOU HAVE ESCAPED THE WILDERNESS.
        """, []),
        ("""
        The bear returns and tells you that bullying is not okay before leaving you alone
        in the wilderness.

        YOU REMAIN LOST.
        """, [])
    ]),
    ("""
    You come across a clearing full of flowers. 
    The bear follows you and asks 'what gives?'
    Do you:
    1 ) Gasp 'A talking bear!'
    2 ) Explain that the bear scared you.
    """, [
        ("""
        The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

        YOU REMAIN LOST.
        """, []),
        ("""
        The bear understands and apologizes for startling you. Your new friend shows you a 
        path leading out of the forest.

        YOU HAVE ESCAPED THE WILDERNESS.
        """, [])
    ])
]

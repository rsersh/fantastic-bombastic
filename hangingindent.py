"""Bite 54. In this Bite you complete print_hanging_indents to print 
a poem (or text) in a nicer way.
For example calling it on (part of) Christina Rosetti's Remember it 
should convert:
            Remember me when I am gone away,
            Gone far away into the silent land;
            When you can no more hold me by the hand,

            Nor I half turn to go yet turning stay.

            Remember me when no more day by day
            You tell me of our future that you planned:
            Only remember me; you understand

to:

Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand

print the resulting poem (don't return it)! The tests include another 
text snippet from Shakespeare. Have fun!

                        
"""

INDENTS = 4
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

def print_hanging_indents(poem):
    buf = ' ' * INDENTS
    marker = False
    linelist = [line.strip() for line in poem.split('\n')]
    for line in linelist:
        if line == '':
            marker = True  
            continue
        elif marker == True:
            print(line)
            marker = False
        else:
            print(buf + line)

print_hanging_indents(shakespeare_unformatted)

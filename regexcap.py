#Bite 234


lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor!
Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat?
Sed viverra tellus in hac habitasse platea dictumst vestibulum.
Morbi tempus iaculis urna id volutpat.
Enim blandit volutpat maecenas volutpat.
Morbi tristique senectus et netus!
Massa tincidunt nunc pulvinar sapien?
Nunc aliquet bibendum enim facilisis gravida neque convallis a.
Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.
Id diam maecenas ultricies mi eget mauris?
Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare!
Gravida in fermentum et sollicitudin ac orci phasellus!
Ut diam quam nulla porttitor massa id neque aliquam.
Sit amet dictum sit amet justo donec enim diam vulputate.
Risus sed vulputate odio ut?
Justo eget magna fermentum iaculis eu non!
At auctor urna nunc id.
At erat pellentesque adipiscing commodo elit at imperdiet!
Molestie nunc non blandit massa enim nec dui?
Lorem donec massa sapien faucibus et molestie ac feugiat.
""".strip().splitlines()

text1 = lorem_ipsum[:5]
text2 = lorem_ipsum[5:13]
text3 = lorem_ipsum[13:]

import re

def capitalize_sentences(text: str) -> str:
    pattern = re.compile(r'\w[\w,\s]+[.?!]')
    text_as_list = pattern.findall(text)
    return ' '.join([ x[0].upper() + x[1:] for x in text_as_list])

text_as_string = ' '.join(text1) 
#print(text_as_string.lower())
#text_as_list = text_as_string.split(' ')
#text_as_string = ''.join(text2) 
#text_as_string = ''.join(text3) 
result = capitalize_sentences(text_as_string.lower())
print(result)
 

from exmp_7_9 import tag

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'scr': 'sunset.jpg', 'class': 'framed'}
print(tag(**my_tag))
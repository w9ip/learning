from exmp_7_9 import tag

print(tag)
from functools import partial

picture = partial(tag, 'img', class_='pic-frame')
picture(scr='wumpus.jpeg')
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)

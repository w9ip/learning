from operator import methodcaller


s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hypenate = methodcaller('replace', ' ', '-')
print(hypenate(s))
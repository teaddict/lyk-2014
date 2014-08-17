# _*_ coding:utf-8 _*_
__author__ = 'schwappkopf'

your_name= 'xxxx'
your_age= 35
your_eyes='brown'
your_hair='black'

print "hey your name is %s" % your_name
print "your age is %d" % your_age
print "your eyes are %s" % your_eyes
print "your hair are %s" % your_hair


my_country= 'turkey'
print "my country is %s" % my_country # "a nicely printable representation of an object"
print "my country is %r" % my_country # "a printable representation of an object"

answer = False
ask = "Is it funny? : %r"
print ask % answer                    # %r ile okudu ve gösterdi

text1 = "sol taraf.."
text2 = "..sağ taraf"

print text1+text2                      #textobjeleri birleştirdi direk

print "." * 25                         # 25 tane nokta koydu !
print "you" *1000
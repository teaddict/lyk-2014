# coding=utf-8
__author__ = 'schwappkopf'



list = [1,2,3,4,5,6,7,8,9]
list_c = ["a","b","c","d","e"]


print "List 2.object to 7.object",list[2:7:1]

del list[4]; #4.eleman silindi

print "List 2.object to 7.object",list[2:7:1]

list.append(10);

print "appended: ",list[8]

deger=cmp(list,list_c);

print deger

max= max(list)
min= min(list)

print "max: %d and min: %d" % (max,min)

#list.insert(index, obj)
#Inserts object obj into list at offset index
list.insert(3,6)
print list[3]

#list.count(obj)
#Returns count of how many times obj occurs in list
print list.count(6)

#list.sort([func])
#Sorts objects of list, use compare func if given
list.sort()
print list


#list.pop(obj=list[-1])
#Removes and returns last object or obj from list

list.pop(list[8])
print list

sayilar = [[1,2,3],[4,5,6],[7,8,9]]
for sayi in sayilar:
    for item in sayi:
        print item



#tuple içeriği her zaman sabittir.
#Yanlışlıkla da olsa değerinin değiştirilmesini istemediğiniz bir değişkene gereksiniminiz varsa tüpleri kullanırsınız.

tuple = ('a','b','c')
print tuple

tuple= (1,2,3,4)
print tuple
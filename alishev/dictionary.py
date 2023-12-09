# type() function return type of value, like key:value
dic = {'Alex' : 25, 'John' : 31}

print(dic)

# add new value
dic['Kate'] = 20

print(dic)

print(dic['Kate'])
print('Getting value on key', dic.get('Alex'))

# for cycle in dictionary
for k, v in dic.items():
    print('Key: ' + str(k) + ", Value " + str(v))
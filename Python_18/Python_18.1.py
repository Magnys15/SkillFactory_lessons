import  requests
import json


r = requests.get("https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html") #HTML код
print(r.content)
print(r.status_code)


r1 = requests.get("https://baconipsum.com/api/?type=meat-and-filler") #JSON ответ (словари и списки в пайтон)
print(r1.content)
print(r1.status_code)
texts1 = json.loads(r1.content)
print(type(texts1))
for letters in texts1:
    print(letters, "\n")


r3 = requests.get('https://api.github.com')
print(r3.content)
d3 = json.loads(r3.content)
print(type(d3))
print(d3['authorizations_url'])


r4 = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
print(r4.content)


data = {'key': 'value'}
r5 = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост запрос,
# но только в этот раз тип передаваемых данных будет JSON
print(r5.content)


print('____________')

r6 = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
print(r6.content)

r6 = json.loads(r6.content)
print(r6[0])

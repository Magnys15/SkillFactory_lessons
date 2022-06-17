import json

# with open('222.txt', encoding='utf8') as g:
#     print(g.read())


# with open('json_.json', encoding='utf8') as f:
# #метод load получает объект файла и возвращвет словарь
#     templates = json.load(f)

with open('json_.json', encoding='utf8') as f:
#метод loads (load string) получает данные в виде строки хранящиеся в "strfile" и возвращвет словарь
    strfile = f.read()
    templates = json.loads(strfile)

print(templates)
print(type(templates))


with open('to_json_.json', 'w', encoding='utf8') as f:
    json.dump(templates, f, ensure_ascii=False, indent=4)

with open('to_json_.json', encoding='utf8') as f:
    print(f.read())

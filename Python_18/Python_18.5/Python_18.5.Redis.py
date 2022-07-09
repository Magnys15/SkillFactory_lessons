import redis
import json


red = redis.Redis(
    host="redis-18196.c302.asia-northeast1-1.gce.cloud.redislabs.com", # ваш хост, если вы поставили Redis к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=18196, # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегд разный, поэтому его надо копировать оттуда же, что и host.
    password="DBYNkAXDTH8eP6VCL71dSTyvXiU0chHI" # для локальной машины пароль не требуется (если вы устанавливали Redis к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password.
)

# red.set('var_1', 'value_1')
# red.set('var_2', 'value_2')

dict1 = {'key1': 'value1', 'key2': 'value2'}
red.set('dict1', json.dumps(dict1))
print(red.get('dict1'))

converted_dict = json.loads((red.get('dict1')))
print(converted_dict)
print(type(converted_dict))
print('____')

red.delete('dict1')  # удаляются ключи с помощью метода .delete()


print(red.get('var_1'))
print(red.get('var_2'))
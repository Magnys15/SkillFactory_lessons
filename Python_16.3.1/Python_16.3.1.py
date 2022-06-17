class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def list_atributs(self):
        return self.timestamp, self.type, self.session_id
# позволит напрямую выводить атрибуты при обращении к экземпляру функции
    # def __str__(self):
    #     return "timestamp: " + str(self.timestamp) + " type: " + self.type + " session_id: " + self.session_id

events = [
    {
     "timestamp": 150,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpppp",
    },
    {
     "timestamp": 160,
     "type": "itemView",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLmmmm",
    },
    {
     "timestamp": 170,
     "type": "item",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLcccc",
    },
]

sp = []
sp_akz = []

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    event_obj.list_atributs()

    print(event_obj) # вывод наименования участк апамяти с экземпляром (если в классе присутствует def __str__(self):
# то будет вывод атрибутов экземпляра при аналогичном обращении )
    # print(event_obj.timestamp)
    sp.append(event_obj.list_atributs()) # добавление атрибутов экземпляра в список через функцию
    sp_akz.append(event_obj) #добавление самих экзепляров в список

# обращение напрямую атрубуту экземпляра
print(sp_akz[1].timestamp)
# print(sp)
# print(sp[1])
#

print()
for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)

print(isinstance(sp_akz, Event))
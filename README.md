---
---

## Postman

---

index = 0 o 1
emisor = 0 o 1
receptor = 0 o 1

http://127.0.0.1:5000/ methods=['GET']

Result:
[
{
"cantidad": 1100,
"cuenta": "123-456-678-123",
"nombre": "Jean Pierre",
"retiros": 0,
"transferencias": 0
},
{
"cantidad": 900,
"cuenta": "987-654-321-123",
"nombre": "Luicito Miguel",
"retiros": 0,
"transferencias": 1
}
]

http://127.0.0.1:5000/Luicito Miguel methods=['GET']

Result:

{
"cantidad": 900,
"cuenta": "987-654-321-123",
"nombre": "Luicito Miguel",
"retiros": 0,
"transferencias": 1
}

(http://127.0.0.1:5000/trans/<int:cantidad>/<int:emisor>/<int:receptor>) methods=['PUT']
http://127.0.0.1:5000/trans/100/1/0

Result:
{
"cantidad": 800,
"cuenta": "987-654-321-123",
"nombre": "Luicito Miguel",
"retiros": 0,
"transferencias": 2
}

(http://127.0.0.1:5000/retiro/<int:cantidad>/<int:index>) methods=['PUT']
http://127.0.0.1:5000/retiro/100/1
# cajero_prueba

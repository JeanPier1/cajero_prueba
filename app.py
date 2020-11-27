from flask import Flask, jsonify, request

app = Flask(__name__)


# Requerimientos: Como cliente debo poder ver mi estado de cuenta, realizar transferencias y hacer retiros, mi estado de cuenta inicial es de 1000 soles. No es necesario implementar una base de datos.
cuentas = [
    {
        "nombre": "Jean Pierre",
        "cuenta": "123-456-678-123",
        "cantidad": 1000,
        "retiros": 0,
        "transferencias": 0
    },
    {
        "nombre": "Luicito Miguel",
        "cuenta": "987-654-321-123",
        "cantidad": 1000,
        "retiros": 0,
        "transferencias": 0
    }
]


@app.route('/', methods=['GET'])
def cuentas_repor():
    return jsonify(cuentas)


@app.route('/<nombre>', methods=['GET'])
def ver_user(nombre):
    if (nombre == "Jean Pierre"):
        return jsonify(cuentas[0]), 200
    elif(nombre == "Luicito Miguel"):
        return jsonify(cuentas[1]), 200
    else:
        print("No existe nombre")
    return "", 200


def pasar_transferencia(receptor, cantidad):
    cuentacantidad = cuentas[receptor]['cantidad']
    aumento = cuentacantidad+cantidad
    cuenta = jsonify(
        {
            "cantidad": aumento,
            "cuenta": cuentas[receptor]['cuenta'],
            "nombre": cuentas[receptor]['nombre'],
            "retiros": cuentas[receptor]['retiros'],
            "transferencias": cuentas[receptor]['transferencias']
        }
    )
    cuentas[receptor] = cuenta.get_json()
    return "ok"


@app.route('/trans/<int:cantidad>/<int:emisor>/<int:receptor>', methods=['PUT'])
def transfere(cantidad, emisor, receptor):
    if(emisor != receptor):
        cuentacantidad = cuentas[emisor]['cantidad']
        if(cuentacantidad >= cantidad):
            restante = cuentacantidad-cantidad
            cuenta = jsonify(
                {
                    "cantidad": restante,
                    "cuenta": cuentas[emisor]['cuenta'],
                    "nombre": cuentas[emisor]['nombre'],
                    "retiros": cuentas[emisor]['retiros'],
                    "transferencias": cuentas[emisor]['transferencias']+1
                }
            )
            cuentas[emisor] = cuenta.get_json()
            # Transferencia sumada
            pasar_transferencia(receptor, cantidad)
            return jsonify(cuentas[emisor]), 200
        return "Cantidad excede a la cuenta de ahorro", 200
    return "Debe haber diferencia en el receptor y emisor", 200


@app.route('/retiro/<int:cantidad>/<int:index>', methods=['PUT'])
def retirosCuentas(cantidad, index):
    print("validacion")
    cuentareal = cuentas[index]['cantidad']
    if(cuentareal > cantidad):
        restante = cuentareal-cantidad
        cuenta = jsonify(
            {
                "cantidad": restante,
                "cuenta": cuentas[index]['cuenta'],
                "nombre": cuentas[index]['nombre'],
                "retiros": cuentas[index]['retiros']+1,
                "transferencias": cuentas[index]['transferencias']
            }
        )
        cuentas[index] = cuenta.get_json()
        return jsonify(cuentas[index]), 200
    return "Cantidad excede a la cuenta de ahorro", 200


@app.route('/arreglo/<int:index>', methods=['PUT'])
def update_cuentas(index):
    cuenta = request.get_json()
    cuentas[index] = cuenta
    return jsonify(cuentas[index]), 200


app.run(debug=True)

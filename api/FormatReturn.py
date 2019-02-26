from flask import jsonify


def success(obj):
    return jsonify({
        "flag": True,
        "res": obj
    })

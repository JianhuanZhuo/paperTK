from os.path import isfile, join
from flask import request
from flask import Flask, url_for, send_from_directory, jsonify
import os
from os import listdir
from flask_cors import CORS

from api.FormatReturn import success
from api.NativeOperation import open_file_locally, show_in_exploror, move_file

app = Flask("paperTK")
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/file/ls')
def file_ls():
    directory = request.args.get("p")
    for d in listdir(directory):
        print(d if isfile(join(directory, d)) else d + "/")

    return success([
        {
            "name": d,
            "type": "file" if isfile(join(directory, d)) else "folder",
            "path": join(directory, d)
        } for d in listdir(directory)])


@app.route('/file/get', methods=['GET'])
def file_subpath():
    file = request.args.get("f")
    return send_from_directory(os.path.dirname(file), filename=os.path.basename(file))


@app.route('/file/open', methods=['GET'])
def file_open():
    file = request.args.get("p")
    open_file_locally(file)
    return success({})


@app.route('/file/show', methods=['GET'])
def file_show():
    file = request.args.get("p")
    show_in_exploror(file)
    return success({})


@app.route('/file/move', methods=['GET'])
def file_move():
    source = request.args.get("s")
    destination = request.args.get("t")
    move_file(source, destination)
    return success({})


@app.route('/files', methods=['GET'])
def file_examples():
    return "file_subpath"


@app.route('/path/<path:subpath>', methods=['GET'])
def show_subpath(subpath):
    # show the subpath after /path/
    # return 'Subpath %s' % subpath
    return url_for('static', filename='haha.html', _external=True)  # 返回的是相对地址，比如: /


if __name__ == '__main__':
    app.run()

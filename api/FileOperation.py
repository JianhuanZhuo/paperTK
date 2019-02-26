from flask import Flask, url_for, send_from_directory

app = Flask("paperTK")

print("file op", __name__)


@app.route('/file/<path:subpath>', methods=['GET'])
def file_subpath(subpath):
    return send_from_directory('k:/', filename=subpath)


@app.route('/file', methods=['GET'])
def file_example():
    return "file_subpath"

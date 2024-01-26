from flask import Flask, request, jsonify, render_template
import shortuuid
import json
from urllib.parse import urlparse
from flask_limiter import Limiter
import markdown.extensions.fenced_code
import os
from markupsafe import Markup


tools = Flask(__name__)
limiter = Limiter(app=tools, key_func= lambda: 'global', default_limits=['2 per second'])

# Creating a dictionary to keep track of the data
URL_LIST = {}


def get_tld(url):
    '''Get top level domain/information from url

    Args:
        url (string): url to parse

    Returns:
        string : top level information of an url ... eg: https://www.yahoo.com
    '''
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    hostname = parsed_url.hostname
    tld = scheme+'://'+hostname
    return tld


def remove_unicode_chars(input_str):
    string_encode = input_str.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    string_decode.strip
    return string_decode


@tools.route('/')
def index():
    try:
        readme_file = open("README.md", "r")
    except:
        readme_file = open("../README.md", "r")
    return render_template("index.html",
        markdown=Markup(markdown.markdown(readme_file.read(), extensions=["fenced_code"]))
    )


@tools.route('/cleanup', methods=['POST', 'GET'])
def cleanup():
    try:
        if request.method == 'POST':
            data = json.loads(request.data)
            clean = remove_unicode_chars(data["string"])
            print(clean)
            return jsonify({'cleanup': clean})

    except Exception as e:
        return jsonify({'message':'Exception', 'error': e})


@tools.route('/replace', methods=['POST'])
def replace(chars, replacewith):
    try:
        data = json.loads(request.data)
        for i in chars:
            if replacewith:
                data = data.replace(i, replacewith)
            else:
                data = data.replace(i, "")

        return jsonify({'replace': data})

    except Exception as e:
        return jsonify({'message':'Exception', 'error': e})


    # Needed for VSCode debugger
if __name__ == '__main__':
    tools.run(use_debugger=False, use_reloader=False, passthrough_errors=True)

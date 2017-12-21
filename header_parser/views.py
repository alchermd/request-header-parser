import re

from flask import jsonify, render_template, request

from . import app


@app.route('/')
def index():
    return render_template('index.j2')


@app.route('/api/whoami')
def whoami():
    # The User-Agent string is quite lengthy, and we only need the 'software'
    # part. So we'll use the re library to parse the string with regular expressions.
    software_regex = re.compile(r"\(.+?\)")
    software = software_regex.search(request.user_agent.string).group()[1:-1]

    return jsonify({
        'ipaddress': request.access_route[0],
        'language': request.accept_languages[0][0],
        'software': software,
    })

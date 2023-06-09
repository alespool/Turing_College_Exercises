from bottle import *
from pprint import pprint
import time
import algebra_module
import os

path = '/Sprint 1/congress_data'


# we use a decorator to attach a route/path
@route('/')
def welcome():
    response.set_header('Vary', 'Accept')  # tell that if they get 2 diff accept headers, they neeed to vary
    # this is done to help website not confuse the caching
    pprint(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'hello'


@route('/now')
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=1')  # this is caching, stores the response
    return time.ctime()


# dynamic routes are marked with angle brackets, it captures the word and sends to our service
@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text.plain'
    return word.upper()


# secret phrase to avoid users from forging cookies
secret = 'Average life expectancy of a stark or targaryen is short'


@route('/area/circle')
def circle_area_service():
    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'The last visit was {last_visit}')
    response.set_header('Vary', 'Accept')
    # setting new cookie. but remember cookies have low level of trust (user see them, and change them)
    response.set_cookie('last-visit', time.ctime(), secret=secret)
    # print(dict(request.query))  # add with ?radius = 10 to make a header

    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]  # instead of f string, this gives the error

    area = algebra_module.area_circle(radius)
    # make content negotiation for curl. if want html, give html. else give JSON

    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p> The area is <em> {area} </em> </p>'

    return dict(radius=radius, area=area, service=request.path)  # response for curl, using dict and making json


## File Server #######################################################

file_template = '''\
<h1> list of files in <em> Congress Data </em> directory </h1>
<hr>
<ol>
    % for file in files:
        <li> <a href= "files/{{file}}"> {{file}} </a> </li>
    % end
</ol>
'''


@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir(path)
    print(files)

    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files=files)

    return template(file_template, files=files)


@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, path + '/congress_data')

if __name__ == '__main__':
    run(host='localhost', port=8080)

# content negotiation: the user makes request, server decides on it
# diff users get diff responses
# most REST APIs do something dynamic

# 500 errors are when smth goes wrong with the app

[alessio-pc@fedora ~]$ python3
Python 3.11.3 (main, Apr  5 2023, 00:00:00) [GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> import time
>>> x = 10; print('Done')
Done
>>> time.sleep(5);print('Done')
Done
>>> time.time()
1685025980.8449287
>>> time.ctime()
'Thu May 25 16:46:23 2023'
>>> import hashlib
>>> hashlib.md5('The tale of two cities')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Strings must be encoded before hashing
>>> hashlib.md5('The tale of two cities'.encode('utf-8')).digest()
b'\x83S\xb0,<\xd3u\xba\x8d\xa2-\xdd~O"\xfa'
>>> hashlib.md5('The tale of two cities'.encode('utf-8')).hexdigest()
'8353b02c3cd375ba8da22ddd7e4f22fa'
>>> hashlib.sha1('The tale of two cities'.encode('utf-8')).hexdigest()
'40d7238a320003ef2f1ab881741792d3735427e6'
>>> hashlib.sha256('The tale of two cities'.encode('utf-8')).hexdigest()
'b37e58d6cbc67229c3184eeb249899ad0fa0164a27c33b79fffdd14173ab9812'
>>> hashlib.sha512('The tale of two cities'.encode('utf-8')).hexdigest()
'bbd0129997233fc6aec15b969c98d84fee6573281009caed5870bf97c9a1249b7a5366ba76dfed2578bb881ffef962fdc3fad31359dccceadd323746badd52c9'
>>> #how to slow down the hashlib
>>> b = 'The tale of two cities'
>>> b = hashlibsha512(b.encode('utf-8'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hashlibsha512' is not defined
>>> b = hashlibsha512(b).encode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hashlibsha512' is not defined
>>> b = hashlib.sha512(b).encode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Strings must be encoded before hashing
>>> b = hashlib.sha512(b).digest()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Strings must be encoded before hashing
>>> b = hashlib.sha512(b).digest()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Strings must be encoded before hashing
>>> b = 'The tale of two cities'.encode('utf-8')
>>> b = hashlib.sha512(b).digest()
>>> b = hashlib.sha512(b).digest()
>>> b = hashlib.sha512(b).digest()
>>> b = hashlib.sha512(b).digest()
>>> b = hashlib.sha512(b).digest()
>>> b
b'\te!"6Nm\x8f^Tj\x89\xd0D\xec\x9d\x95U\xa8\xa6V\xf0l\xd3E\x03\xadg\xe4\xec\xfe\xb8_\\\xf8\x19t\x91\x94\xabN\xf4\xffe8\xf5\xd0\xa1\xe3&\xc8\x8cP\xedFw\xa6\xf6\x95\xc3\xb5\xdc\x94\xa4'
>>> p = 'The tale of two cities'.encode('utf-8')
>>> h = hashlib.pbkdf2_hmac('sha256', p, 'some phrase', 10000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a bytes-like object is required, not 'str'
>>> h = hashlib.pbkdf2_hmac('sha256', p, b'some phrase', 10000)
>>> h
b"\x18\xe7\x1e\x11\x94\xd7\xdc*\xd8\xe4<3\x9dG\x0e\x0e\xbd\x01#=6?\x95'\xfc\x15\x1a:3/}\x15"
>>> hashlib.pbkdf2_hmac('sha256', p, b'some other phrase', 10000)
b'\xeb\xb2\x8fTl\xeacb\xca[\xaf{\xf1\xa8\xf4\xe9\xd3\x9bka[\xd6O9\xa7\xf7\xb4\x9d\t=\x80\xd2'
>>> s = 'The quick'
>>> t = 'brown fox'
>>> s + t
'The quickbrown fox'
>>> s = 'the quick brown'
>>> t = 'fox'
>>> s + t
'the quick brownfox'
>>> s = 'the quick'
>>> t = 'brown fox'
>>> repr((s,t))
"('the quick', 'brown fox')"
>>> 
>>> s = 'the quick'
>>> s = 'the quick brown'
>>> t = ' fox'
>>> repr((s,t))
"('the quick brown', ' fox')"
>>> los =['raymond', 'hettinger', 'likes', 'python']
>>> ' '.join(los)
'raymond hettinger likes python'
>>> ''.join(los)
'raymondhettingerlikespython'
>>> 38/5
7.6
>>> 38//5
7
>>> # Ternary operator == conditional expression
>>> score= 70
>>> 'pass' if score >= 70 else 'fail'
'pass'
>>> score= 69
>>> 'pass' if score >= 70 else 'fail'
'fail'
>>> # <posres> if <cond> else <negres>
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> # short circuiiting operators
>>> 3 < 10 and 10 < 20
True
>>> bool('hello')
True
>>> len('hello')
5
>>> # if len of str > 0 is True
>>> 'hello' and True
True
>>> True and 'hello'
'hello'
>>> # why returns the value instead of true? 
>>> bool('')
False
>>> '' and 'hello'
''
>>>  def f(x,s= None):
  File "<stdin>", line 1
    def f(x,s= None):
IndentationError: unexpected indent
>>> def f(x,s= None):
...     s = s or 'default'
...     print(x,s)
... 
>>> f(10, 'some value')
10 some value
>>> f(10)
10 default
>>> # normalize unicode strings used as dictionary keys
>>> #named tuples make tuples self-describing
>>> # bisect searches sorted lists, for looking specific items use hashtable
>>> # bisect is good for searching ranges
>>> # merge creates an iterator to combine multiple sorted inputs
>>> # can use islice and next to partially consume iterators. if u have large lists, 
>>> # use merge islice, thats better
>>> # intern saves memory for frequentyl used strings
>>> # random.expovariate simulates arrival times
>>> # time.sleep works by making a delay, time.time and ctime gives us the times
>>> # base hashlibs are not secure, they use sha256 adn sha512 but theyt are too fast so they use the weird name to iterate over them a lot
>>> # we also got ternary operators
>>> # and and or returns the value the caused the expression to be true or false
>>> 

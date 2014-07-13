#!/usr/bin/python

import os

f0 = open("template.txt", "r")
template1 = f0.read()
f0.close

f1 = open("titles.txt", "r")
titles1 = f1.readlines()
f1.close

pos = 0
while True:
  l = titles1[pos]
  l = l.strip()
  template2 = template1
  images = ""
  ins = 0
  p = 0
  for file in os.listdir("."):
    if file.startswith(l + "_"):
      t1 = file.split('.')
      # print t1[0] #+ t2[len(t2) - 1]
      images = images + '<div><img alt="' +  t1[0].replace("_", " ") + '" src="' + file + '"/></div>\n'
      if ins == 0:
        images = images + "[[advert]]\n"
        ins = 1
      if ins == 1 & p == 1:
        images = images + "[[controls]]\n"
        ins = 2
      p = p + 1
  if ins == 1:
    images = images + "[[controls]]\n"
    ins = 2

  template2 = template2.replace("[[title]]", "Gnomophobia:" + l.replace("_", " "))
  template2 = template2.replace("[[images]]", images)
  c = ""
  if pos == 0:
    prev = titles1[0]
  else:
    prev = titles1[pos - 1]
  c = c + '<div><span class="button1"><a href="' + prev + '.html">< previous</a></span>'
  c = c + '<span class="button1">[index]</span> '
  if pos == (len(titles1) - 1):
    nxt = titles1[len(titles1) - 1]
  else:
    nxt = titles1[pos + 1]
  c = c + '<span class="button1"><a href="' + nxt + '.html">next ></a></span></div>'

  template2 = template2.replace("[[controls]]", c)
  template2 = template2.replace("[[advert]]", '<div><img alt="advertisement" src="advertisement.png"></div>')

  #l = l.rstrip('\n')
  #print(images)
  f2 = open(l + ".html", "w")
  f2.write(template2)
  f2.close()
  pos = pos + 1
  if pos == len(titles1):
    break
 

f1.close()



#!/usr/bin/python

import os

f0 = open("template.txt", "r")
template1 = f0.read()
f0.close

f1 = open("titles.txt", "r")
titles1 = f1.readlines()
f1.close

# write web pages
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

  template2 = template2.replace("[[title]]", l.replace("_", " "))
  template2 = template2.replace("[[images]]", images)
  c = ""
  if pos == 0:
    prev = titles1[0]
  else:
    prev = titles1[pos - 1]
  #c = c + '<div id="t0">\n'
  c = c + '<a href="' + prev + '.html"><img src="btnLeft1.png"/></a>\n'
  c = c + '<a href="toc.html"><img src="btnIndex1.png"/></a>\n '
  if pos == (len(titles1) - 1):
    nxt = titles1[len(titles1) - 1]
  else:
    nxt = titles1[pos + 1]
  c = c + '<a href="' + nxt + '.html"><img src="btnRight1.png"/></a>\n'
  #c = c + '</div>\n'

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

# write index
template2 = template1
template2 = template2.replace("[[title]]", "Gnomophobia Index")
anchors = ""
episodes = ""
num_eps = 25

pos = 0
while True:
  l = titles1[pos]
  l = l.strip()
  episodes = episodes + '<p><a href="' + l + '.html">' + l.replace("_"," ") + '</a></p>\n'
  if (pos % num_eps) == 0 & pos > 0:
    anchors = anchors + '<p><a href="#season' + str(pos/num_eps) + '">Season ' + str(pos/num_eps) + '</a></p>\n'
    episodes = episodes + '<p><a name="season' + str(pos/num_eps) + '">Season ' + str(pos/num_eps) + '</a></p>\n'
  pos = pos + 1
  if pos == len(titles1):
    break

template2 = template2.replace("[[images]]", '<div id="toc">' + anchors + '<br/><br/>' + episodes + '</div>')

f2 = open("toc.html", "w")
f2.write(template2)
f2.close()


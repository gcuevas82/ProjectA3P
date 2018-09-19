top_template = open('/home/gingerc/homework/templates/top.html').read()
bottom_template = open('/home/gingerc/homework/templates/bottom.html').read()

# Read in index HTML code
content = open('/home/gingerc/homework/docs/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('/home/gingerc/homework/docs/index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
content = open('/home/gingerc/homework/docs/index2.html').read()
music_html = top_template + content + bottom_template
open('/home/gingerc/homework/docs/index2.html', 'w+').write(music_html)

# And again, this time with art HTML code
content = open('/home/gingerc/homework/docs/index3.html').read()
contact_html = top_template + content + bottom_template
open('/home/gingerc/homework/docs/index.html', 'w+').write(contact_html)

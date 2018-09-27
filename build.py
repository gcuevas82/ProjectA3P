# 2.1 Phase1 - Using a 'Main' function

print('HW Phase 1')

def main():
    top = open("build.py").read()
   
if __name__ == "__main__":
    main() 
    
# 2.2 Phase 2 List
    pages = [
{
"filename": "templates/A3Pcreativeindex.html",
"output": "docs/A3Pcreativeindex.html",
"title": "Art3mis Prime",
},
{
"filename": "docs/index2.html",
"output": "docs/index2.html",
"title": "A3P Music",
},
{
"filename": "docs/index3.html",
"output": "docs/index3.html",
"title": "Contact Me",
},

]
# template time! adding the template items here
# I'm having trouble understanding this part but I think
# it is due to the way my files were saved previously

main = open("docs/A3Pcreativeindex.html").read()
music = open("docs/index2.html").read()
contact = open("docs/index3.html").read()

finished_index_page = main + music + contact
open("docs/base.html", "w+").write(finished_index_page)

# moving on to section 2.4

def apply_template(content):
    
    return (base.html)
def main():
    content = open("docs/base.html")
    finished_index_page = apply_template(content)

zag = input()
art = input()
comm = input()
x = []

while comm != "end of comments":
    x.append(comm)
    comm = input()

print("<h1>")
print("\t" + zag)
print("</h1>")
print("<article>")
print("\t" + art)
print("</article>")
for i in x:
    print("<div>")
    print("\t" + i)
    print("</div>")

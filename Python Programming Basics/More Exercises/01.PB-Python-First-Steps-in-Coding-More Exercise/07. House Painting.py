x=float(input())
y=float(input())
h=float(input())
lice_steni=(2*x*y+2*x*x)-2*1.2-2*1.5*1.5
lice_pokriv=2*x*y+x*h
litra_zeleno=lice_steni/3.4
litra_cherveno=lice_pokriv/4.3
print(f'{litra_zeleno:.2f}')
print(f'{litra_cherveno:.2f}')
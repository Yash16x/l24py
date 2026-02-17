class parrot:
    sp="bird"
    def _init_(self, n,a):
        self.n=n
        self.a=a

c=parrot("cherry",6)
t=parrot("tommy",5)

print("cherry and Tom are ", c.sp)
print("{} is {} year old".format(c.n, c.a) )
print("{} is {} year old".format(t.n, t.a) )
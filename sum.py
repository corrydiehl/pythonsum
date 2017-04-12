import ptvsd
ptvsd.enable_attach(secret='my_secret',address = ('0.0.0.0', 3000))
ptvsd.wait_for_attach()
ptvsd.break_into_debugger()

num1 = 23422435
num2 = 239797249875
sum = num1 + num2
print("hello from python")
print(sum)
exit()
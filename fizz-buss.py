#Python Fizz-Buzz

mod1 = 15
mod1msg = 'Fizzbuzz'
mod2 = 3
mod2msg = 'Fizz'
mod3 = 5
mod3msg = 'Buzz'
for i in range(1,101):
    if i % mod1 == 0: print(mod1msg)
    elif i % mod2 == 0: print(mod2msg)
    elif i % mod3 == 0: print(mod3msg)
    else: print('i=',i)
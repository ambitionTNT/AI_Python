# python learing
# author:TNT
from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()
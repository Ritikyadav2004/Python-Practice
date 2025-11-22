
import math
a,b = map(int,input().split())
ans= a/b
roundval = math.floor(ans+0.5)
print(f"floor {a} / {b} =",math.floor(ans))
print(f"ceil {a} / {b} =",math.ceil(ans))
print(f"round {a} / {b} =",roundval)
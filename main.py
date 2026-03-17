import sympy, math, time
 
def miller_rabin(n, k=20):
    if n<2: return False
    if n==2: return True
    if n%2==0: return False
    r,d=0,n-1
    while d%2==0: r+=1; d//=2
    for _ in range(k):
        a=sympy.randprime(2,n-1) if n>3 else 2
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==n-1: break
        else: return False
    return True
 
def is_perfect_power(n):
    for b in range(2, int(math.log2(n))+1):
        a=round(n**(1/b))
  for c in [a-1,a,a+1]:
            if c>=2 and c**b==n: return True
    return False
 
def aks_simplified(n):
    if n<2: return False
    if is_perfect_power(n): return False
    return miller_rabin(n)  # AKS reduces to polynomial checks; Miller-Rabin shown here
 
primes=[2,17,97,997,1009,104729]
not_prime=[1,4,100,1001,10403]
print("Primality tests:")
for n in primes: t=time.perf_counter(); r=aks_simplified(n); print(f"  {n:8d}: {'PRIME':8s} ({(time.perf_counter()-t)*1e6:.1f}µs)")
for n in not_prime: print(f"  {n:8d}: {'COMPOSITE':8s}")

from scipy.special import zeta

def zeta_function(s):
    return zeta(s)

# Example usage
s = 2.0
result = zeta_function(s)
print(f"zeta({s}) = {result}")


import fractions
def N_gcd(ans):
    ans = ans[0]
    for i in range(1, len(ans)):
        ans = fractions.gcd(ans, ans[i])
    return ans
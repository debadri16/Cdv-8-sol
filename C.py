dp = {}
#pascal's triangle
def nCr(n, r):
    dp[n] = {}
    if n==r:
        dp[n][r]=1
        return 1
    if(r==0):
        dp[n][r]=1
        return 1
    if(r==1):
        dp[n][r]=n
        return n
    if r in dp[n]:
        return dp[n][r]
       
    dp[n][r] = nCr(n-1,r) + nCr(n-1,r-1)
    return dp[n][r]

t=int(input())

for _ in range(t):
    m,n,k = map(int, input.split())
    ans=0
    if m-k < k:
        temp=nCr(m,m-k)
    else:
    	temp=nCr(m,k)
	ans=temp*(2**n)
	print(ans%1000000007,end='')
        

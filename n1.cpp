#include<iostream>
using namespace std;
// Returns value of Binomial Coefficient C(n, k) 
long long int binomialCoeff(long long int n, long long int k) 
{ 
    long long int res = 1; 
  
    // Since C(n, k) = C(n, n-k) 
    if ( k > n - k ) 
        k = n - k; 
  
    // Calculate value of [n * (n-1) *---* (n-k+1)] / [k * (k-1) *----* 1] 
    for (long long int i = 0; i < k; ++i) 
    { 
        res *= (n - i); 
        res /= (i + 1); 
    } 
  
    return res; 
} 
  
int main(){
	int t,m,n,k;
	long long int temp,ans,bc;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>m>>n>>k;
		ans=0;
		temp=binomialCoeff(m,k);
		for(int j=0;j<=n/2;j++){
			bc=binomialCoeff(n,j);
			ans+=2*temp*bc;
		}
		if(n%2 == 0)
			ans-=temp*bc;
		
	}
	cout<<(ans%1000000007);
	return(0);
}

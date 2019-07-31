#include<iostream>
#include<bits/stdc++.h> 
#include<math.h>
using namespace std;
// Returns value of Binomial Coefficient C(n, k) 
long long int binomialCoeff(long long int n, long long int k) 
{ 
    long long int C[k+1]; 
    memset(C, 0, sizeof(C)); 
  
    C[0] = 1;  // nC0 is 1 
  
    for (long long int i = 1; i <= n; i++) 
    { 
        // Compute next row of pascal triangle using 
        // the previous row 
        for (long long int j = min(i, k); j > 0; j--) 
            C[j] = C[j] + C[j-1]; 
    } 
    return C[k]; 
} 
  
int main(){
	int t,m,n,k;
	long long int temp,ans,bc;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>m>>n>>k;
		ans=0;
		if(m-k < k)
			temp=binomialCoeff(m,m-k);
		else
			temp=binomialCoeff(m,k);
//		for(int j=0;j<=n/2;j++){
//			bc=binomialCoeff(n,j);
//			ans+=2*temp*bc;
//		}
//		if(n%2 == 0)
//			ans-=temp*bc;
		ans=temp*pow(2,n);
		cout<<(ans%1000000007);	
	}
	return(0);
}

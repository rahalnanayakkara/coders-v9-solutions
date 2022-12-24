#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
using vecl = vector<ll>;
using pll = pair<ll, ll>;
using vecpl = vector<pll>;
using mapll = map<ll,ll>;

#define LIMIT 1'00'000+10

int main()
{
    #ifdef DEBUG_PRAVEEN
        freopen("Sample.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    #endif
    bitset<LIMIT> s;
    int N;
    cin >> N;
    int c=0;
    for(int i=0;i<N;i++){
        cin >>c;
        s[c]=1;
    }
    bitset<LIMIT> r;
    ll ans=0;
    for(int k=1;k<LIMIT;k++){
        r = s & (s << k);
        if(r.any()) ans++;
    }
    cout << ans << endl;
    return 0;
}

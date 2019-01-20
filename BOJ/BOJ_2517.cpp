#include <cstdio>

int n;
struct info {
	int idx, power;
};
info p[500001], tmp[500001];
int A[500001];

void merge(int left, int mid, int right){
	int l,r,i;
	l = left;
	r = mid+1;
	i = left;
	
	while(l<=mid && r<=right){
		if(p[l].power > p[r].power){
			tmp[i++] = p[l++];
		} else {
			A[p[r].idx] -= (mid-l+1);
			tmp[i++] = p[r++];
		}
	}
	
	
	if(l>mid) {
		for(int j=r;j<=right;j++){
			tmp[i] = p[j];
			i++;
		}
	} else {
		for(int j=l;j<=mid;j++){
			tmp[i] = p[j];
			i++;
		}
	}
	
	for (int m = left; m <= right; m++) {
        p[m] = tmp[m];
    }
	
	
}


void merge_sort(int left, int right){
	int mid;
	if(left<right){
		mid = (left+right)/2;
		merge_sort(left,mid);
		merge_sort(mid+1, right);
		merge(left, mid, right);
	}
	
}


int main() {
	scanf("%d", &n);
	
	for(int i=1;i<=n;i++){
		scanf("%d", &p[i].power);
		p[i].idx = A[i] = i;
	}
	merge_sort(1,n);
	for(int i=1;i<=n;i++)printf("%d\n",A[i]);
	
	return 0;
}

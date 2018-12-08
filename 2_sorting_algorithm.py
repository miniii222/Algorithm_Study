list1 = [4,2,7,8,-3,0]

n = len(list1) #length of list

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
###from the smallest to the biggest

#%% Selection sort
list1_sorted = list1.copy()

def select_sort (alist) :    #alist : 정렬할 리스트
    n = len(alist)
    
    for j in range(n) :
        min_index = j #index를 이용하여 바꿀 element 지정.
    
        for i in range(j+1,n) :
            if alist[min_index] >= alist[i] :
                min_index = i #min_index보다 작은 값을 갖는 element의 index 저

        swap(alist,j, min_index)
        #list1_sorted[j],list1_sorted[min_index] = list1_sorted[min_index],list1_sorted[j]
    return(alist)
    
select_sort(list1_sorted)
#%%
"""
#C lnaguage ver.
void selectionSort(int list[], int n) {
        int i, j, min;
        
        for (i=0; i<n-1; i++) {
                min = i;
                for (j=i+1;j<n;j++)
                    if (list[j]<list[min]) min=j;
                    swap(&list[i], &list[min]);
                    
}
}
"""


#%% Bubble sort
list1_sorted = list1.copy()

def bubble_sort(alist) :
    n = len(alist)
    flag = True
    
    while flag :        #flag True이면 계속 반복
        
        flag = False    #처음에 False로 만들어주고
        
        for i in range (n-1):
            if alist[i] > alist[i+1] :
                swap(alist,i,i+1)
                #list1_sorted[i],list1_sorted[i+1] = list1_sorted[i+1], list1_sorted[i]
                flag = True     #if절을 만족해야만 flag를 다시 True로
            
    return(alist)
    
bubble_sort(list1_sorted)
#%%       
"""
#C lnaguage ver.
void bubbleSort(int list1[], int n) {
        int i, j, flag=TRUE ;
        j = 0;

    while ((j<n-1) && flag) {
            flag = FALSE;
            for (i=n-1; i>j; i--){
                if (list[i]<list[i-1]) {
                        swap(&list[i], &list[i-1]);
                        flag = TRUE;
                        }
        j++;
}
}
}
"""
#%% insert sort
list1_sorted = list1.copy()

def insert_sort(alist) : 
    n = len(alist)
    for i in range(1,n) :
        insert_element = alist[i] #삽입할 숫자
     
        for j in range(i-1,-1,-1) :
            if insert_element < alist[j]:
                alist[j+1] = alist[j] #다음 칸으로 이동
                alist[j] = insert_element#삽입
    return(alist)
    
insert_sort(list1_sorted)
#%%
"""
void insertionSort(int list[], int n) {
        int i, j, next;
        for (i=1; i<n; i++) {
                next = list[i];
                for(j=i-1; j>=0 && next<list[j]; j--){
                list[j+1] = list[j];
                list[j+1] = next;
                }
}
}

"""
#%% merge sort
list1_sorted = list1.copy()

def merge_sort(alist) :
    
    if len(alist) <=1 :
        return(alist)
    
    mid = len(alist)//2 #split index
    left = alist[:mid]
    right = alist[mid:]
    
    left=merge_sort(left)
    right=merge_sort(right)

    result = []
    
    while len(left)>0 or len(right)>0 :
        
        if len(left)>0 and len(right)>0 :
            if left[0]<=right[0] :
                result.append(left[0])
                left = left[1:]
            else :
                result.append(right[0])
                right = right[1:]
                
        elif len(left)>0 :
            result.append(left[0])
            left = left[1:]
            
        else :
            result.append(right[0])
            right = right[1:]
            
    return(result)
       
merge_sort(list1_sorted)

#%%
"""
#define MAX_SIZE 1000
typedef struct { int key; } element;
element list[MAX_SIZE], sorted[MAX_SIZE];
void merge(element list[], element sorted[], int i, int m, int n) {
        int i, k, t;
        j=m+1; k=i;
        while (i<=m && j<=n) {
                if (list[i].key <= list[j].key)
                    sorted[k++].key = list[i++].key;
                else sorted[k++].key = list[j++].key;
                }
        if (i>m) for (t=j; t<=n; t++) sorted[k+t-j].key = list[t].key;
        else for (t=i; t<=m; t++) sorted[k+t-i].key = list[t].key;
}
        
void mergeSort(int first, int last) {
        int mid, i;
        if (first < last) {
                mid = (first+last)/2;
                mergeSort(first, mid);
                mergeSort(mid+1, last);
                merge(list, sorted, first, mid, last);
            for (i=first; i<=last; i++) list[i].key=sorted[i].key;
}
}
        
"""
#%% quick sort
list1_sorted = list1.copy()

def partition(a_list, first, last) :    #first 첫번째 index, last 마지막 index
    pivot = a_list[first]
    
    l=first+1; r = last
    
    while(l<r) :
        while a_list[l]<pivot and l<r :
            l=l+1
        while a_list[r]>pivot and l<r :
            r=r-1
    
        swap(a_list, l,r)
        
    swap(a_list,l-1,first)
    p= l-1
    
    return(p) #partition index return


def quick_sort(a_list,first,last) : #first : 첫번째 index, last : 마지막 index
    if first<last :
        p=partition(list1_sorted,first,last) #partition index return
        
        quick_sort(a_list,first,p-1)
        quick_sort(a_list,p+1,last)
        
    return(a_list)
    
quick_sort(list1_sorted, 0, n-1)
    
#%%
"""
void quickSort(int list[], int left, int right) {
        int i, j, pivot;
        if (left < right) {
                i = left; j = right+1;
                pivot = list[left];
                do {
                        do { i++; } while (i <= right && list[i] < pivot);
                        do { j--; } while (list[j] > pivot);
                        if (i<j) swap(&list[i], &list[j]);
                        } while (i<j);
                
                swap(&list[left], &list[j]);
                quickSort(list, left, j-1);
                quickSort(list, j+1, right);
}
}
"""
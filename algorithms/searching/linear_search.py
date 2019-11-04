# from collections import Counter
"""
Given a List of N number a1,a2,a3........an, You have to find smallest number from the List that is repeated in the List exactly K number of times.

Input Format

First Line of Input Contain Single Value N, Size of List
Second Line of Input Contain N Space Separated Integers
Third Line of Input Contain Single Value K

Output Format

Smallest Integer Value That is Repeated Exactly K Number of Time

Constraints

0 < N < 100001
0 <= K < 100001
0 <= ai < 100001
NOTE
There Will Be Atleast One Variable Which Is Repeated K Times

SAMPLE INPUT

5
2 2 1 3 1
2

SAMPLE OUTPUT
1
"""


def find_min(arr):
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_


def repeated_k_times(arr, k):
    elm_count = {}
    elmnts_matching_k_times = []

    for i in arr:
        try:
            elm_count[i] = elm_count[i] + 1
        except KeyError:
            elm_count[i] = 1
    for key_, val_ in elm_count.items():
        if val_ == k:
            elmnts_matching_k_times.append(key_)
    return find_min(elmnts_matching_k_times)


N = input()
elements = input()
elements = elements.split(" ")
elements = [int(i) for i in elements]
K = input()

print(repeated_k_times(elements, int(K)))

# interesting
"""
without dict and with just list

also there is no 2 times iteration and no min logic ..

#include<stdio.h>
int main()
{
    int  n,a[100000],b[100000],i,k;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    scanf("%d",&k);
   for(i=0;i<n;i++)
   {
       b[a[i]-1]++;
   }
   /*for(i=0;i<n;i++)
    {
        printf("%d",b[i]);
    }*/
   for(i=0;i<n;i++)
   {
       //printf("%d %d\n",b[i],i+1);
       if(b[i]==k)
       {
           printf("%d",i+1);
           break;
       }
   }
   return 0;
}

"""

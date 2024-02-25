int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    *returnSize=numsSize;
    int *squares=(int *)malloc(numsSize*sizeof(int));
    int m=0,n=numsSize-1,count=numsSize-1;
    while(m<=n)
    {
       int l=nums[m]*nums[m];
       int  r=nums[n]*nums[n];
        if(l>=r)
        {
            squares[count--]=l;
            m++;
           // printf("%d\n",*(returnSize+count*4));
        }
        else
        {
            squares[count--]=r;
            // printf("%d\n",*(returnSize+count*4));
            n-- ;
        }


    }
    return squares;
}
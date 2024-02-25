class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
       long int rem=0,div=0,num=x,rev_num=0;
        while(num!=0)
        {
            rem=num%10;
            rev_num=rem+rev_num*10;
            num=num/10;
        }
        if(rev_num==x)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
};
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //int i=0;
        vector<int> new_vector;
        for(int i:nums)
        {
            if(find(new_vector.begin(),new_vector.end(),i)==new_vector.end())
            {
                new_vector.push_back(i);
            }
        }
        nums=new_vector;
        return nums.size();

        
    }
};
/*

NOTE : This is the O(n^2) time solution to the problem. I wanted to submit this as well.

*/



class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // We need to find the product of all the subarrays
        // A subarray is nums[i] * nums[i+1] where 0<=i<n
        // the product array will always have n-1 products
        int n = nums.size();
        int max = 0;
        if(n > 1)
        {
        vector<int> product(n-1);
        
        for(int i = 0; i < n-1; i ++)
        {
            product[i] = nums[i] * nums[i+1];
            
        }
        // now we have our array, we have to find the biggest number
        
        max = nums[0];

        for(int i = 0; i<n ; i++){
            if(nums[i]>max)
            {
                max = nums[i];
            }
        }

        for(int j = 0; j < n-1; j ++)
        {
            if(product[j]>max){
                max = product[j];
            }
        }
        }

        else{
            max = nums[0];
        }
        // now that we have the position of the biggest product, returning the subarray should be easy.
        return max;
    }
};
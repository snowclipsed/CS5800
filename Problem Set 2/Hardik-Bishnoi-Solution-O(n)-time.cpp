/*

This is implemented in O^n.

*/


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Ther exist 3 cases
        // 1. The entire array is +ve
        // 2. The array has even negatives
        // 3. The array has odd negatives     
        

        /*

        In both case 1. and 2. the max product is the entire array

        In case 3. the max product subarray is the subarray with an even number of 
        negatives or no negatives.

        So the problem is simplified to searching for this condition from both the start and end of the array.


        */


        int maxprod = INT_MIN;        // initialize our max counter to the minimal integer
        int product = 1;             // initialize product var as 1 to multiply with subarray elements
        int n = nums.size();        // store the size of the array 
        
        for(int i = 0; i < n; i++)
        {
            product *= nums[i]; // calculating the product of the array incrementing through the elements so 
                                // as to produce an increasing window

            cout<<product<<"\n"; // std::out for debugging purpose

            maxprod = max(maxprod,product); // max() returns the bigger number of the two.
            if(product == 0)
            {
                product = 1;
            }
        }

        product = 1;

        for(int j = n-1; j>=0; j--) // doing the same as the above loop 
                                    // but this time from the end of the array.
        {
            product *= nums[j];
            cout<<product<<"\n";
            maxprod = max(maxprod,product);
            if(product == 0)
            {
                product = 1;
            }
        }

        return maxprod; // return the maximum product of the subarray.
    }
};
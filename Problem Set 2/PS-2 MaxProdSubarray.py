class Solution:
    def maxProduct(self, a):
        return self.maxprodcalc(a, 0, len(a) - 1)

    def maxprodcalc(self, a, left, right):
        if right == left:
            return a[right]

        mid = (left + right) // 2

        maxleft = a[mid]
        minleft = a[mid]
        maxright = a[mid + 1]
        minright = a[mid + 1]
        i = mid - 1
        tmp = a[mid]
        while i >= left:
            tmp *= a[i]
            maxleft = max(maxleft, tmp)
            minleft = min(minleft, tmp)
            i -= 1

        i = mid + 2
        tmp = a[mid + 1]
        while i <= right:
            tmp *= a[i]
            maxright = max(maxright, tmp)
            minright = min(minright, tmp)
            i += 1

        middleprod = max(maxleft * maxright, minleft * minright)
       
        leftprod = self.maxprodcalc(a, left, mid)
        
        rightprod = self.maxprodcalc(a, mid + 1, right)
        
        return max(leftprod, rightprod, middleprod)

def maxArea(heights): 
        def waterVolume(bar1, bar2): 
            return min(heights[bar1], heights[bar2])*abs(bar1-bar2)

        maxVolume = 0
        n = len(heights)
        l = 0
        r = n - 1

        while l < r: 
            print("left, right", l, r)
            print("heights: ", heights[l], heights[r])
            print("wVolume", waterVolume(l, r))

            maxVolume = max(maxVolume, waterVolume(l, r))

            if heights[r] > heights[l]: 
                l += 1
            else: 
                r -= 1
            
        return maxVolume

height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
print(maxArea(height))
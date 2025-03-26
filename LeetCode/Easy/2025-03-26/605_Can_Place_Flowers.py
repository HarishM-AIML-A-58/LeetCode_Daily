class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    n -= 1
                    flowerbed[i] = 1  # Plant a flower
                    if n == 0:  # Early exit
                        return True
                    i += 1  # Skip next index since adjacent planting isn't allowed

            i += 1  # Move to next spot
        
        return n <= 0
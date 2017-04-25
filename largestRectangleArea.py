#!/usr/bin/env python
#encoding=utf-8

def largestRectangleArea(heights):
        stack = []
        heights.append(0)
        maxArea = 0
        
        for i in range(0, len(heights)):
            if len(stack) == 0:
                maxArea = max(heights[i], maxArea)
                stack.append(i)
            else:
                while (len(stack) > 0 and heights[i] <= heights[stack[len(stack) - 1]]):

                    #print i
                    #print stack

                    highest = stack.pop()
                    left = 0
                    
                    if len(stack) > 0:
                        left = stack[len(stack) - 1]
                    else:
                        left = -1
                    
                    maxArea = max(maxArea, (i - left - 1) * heights[highest])
                    #print maxArea
                
                stack.append(i)
        
        return maxArea


print "### %d" % largestRectangleArea([1,1])
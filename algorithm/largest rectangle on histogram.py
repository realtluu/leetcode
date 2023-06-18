def largestRectangleArea(heights):
    stack = [-1]
    maxArea = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            lastElementIndex = stack.pop()
            maxArea = max(maxArea, heights[lastElementIndex] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] != -1:
        lastElementIndex = stack.pop()
        maxArea = max(maxArea, heights[lastElementIndex] * (len(heights) - stack[-1] - 1))

    return maxArea


heights = (2, -3, 4, 3, 2, 5, 3, 4, 3, 2, 2, 3, 4, 3, 2, 2, 3, 4, 8, 2, 2, 3, 4, 3, 2, -5, 3, 4, 3, 2, 2, 3, 4, 3, 2, 2, 3, 4, 8, 2)
print(largestRectangleArea(heights))
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if abs(asteroid) > stack[-1]:
                        stack.pop()
                    elif abs(asteroid) == stack[-1]:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)

        print(stack, "stack")


s = Solution()
s.asteroidCollision([5, 10, -5])
s.asteroidCollision([8, -8])
s.asteroidCollision([-2, -2, 1, -1])
s.asteroidCollision([1, -2, -2, -2])
s.asteroidCollision([-2, -1, 1, 2])
s.asteroidCollision([-2, -2, 1, -2])

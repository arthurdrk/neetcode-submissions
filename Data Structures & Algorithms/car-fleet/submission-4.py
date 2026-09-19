class Solution:
    def carFleet(self, target, position, speed):
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
 '''
 A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
 '''
 
 
 class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:   

        n, s, e, w = True, False, False, False
        obstacles = set([tuple(x) for x in obstacles]) # init
        destination, output = [0, 0], 0         
        
        for command in commands: # loop to do
            _n, _s, _e, _w = n, s, e, w
            if command == -1:
                n, s, e, w = True if _w else False, True if _e else False, True if _n else False, True if _s else False
            elif command == -2:
                n, s, e, w = True if _e else False, True if _w else False, True if _s else False, True if _n else False
            else:
                current = command
                step, index = (1, 1) if n else ((-1, 1) if s else ((1, 0) if e else (-1, 0)))
                while current:
                    destination[index] += step
                    if tuple(destination) in obstacles:
                        destination[index] -= step #???????
                        break
                    current -= 1
                output = max(output, destination[0] * destination[0] + destination[1] * destination[1])
        return output
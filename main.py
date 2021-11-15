# Maze solver AI using DFS

import sys
from PIL import Image, ImageDraw, ImageFont


dead = []


class Stack:
    def __init__(self):
        self.stack=[]
    def append(self, data):
        self.stack.append(data)
    def remove(self):
        self.stack.pop(-1)
    def dead_end(self):
        if len(self.stack)>=2 and self.stack[-1]==self.stack[-2]:
            return True
        return False


class AI:
    def __init__(self):
        """Initializing the maze array"""
        with open(sys.argv[1], 'r') as f:
            grid = f.read()
        start=0
        self.length=grid.index("\n")
        self.maze=[]
        self.height=len(grid)//self.length

        # x -> self.height & y -> self.length

        for i in range(len(grid)//self.length):
            add = list(grid[start:start+self.length])
            self.maze.append(add)
            start += self.length+1

    def get_start_and_end(self):
        """Returns the co-ordinates of start and end"""
        x=y=xi=yi=None
        for i in range(self.height):
            a=self.maze[i].count("#")
            b=self.maze[i].count(" ")
            if a+b!=self.length:
                if "A" in self.maze[i]:
                    y=self.maze[i].index("A")
                    x=i
                if "B" in self.maze[i]:
                    yi=self.maze[i].index("B")
                    xi=i
        return x,y,xi,yi


    def solve(self):
        """Main AI that solves the maze using Depth First Search"""
        current_x, current_y, dest_x, dest_y = self.get_start_and_end()

        path = Stack()
        path.append([current_x, current_y])
        
        while current_x!=dest_x or current_y!=dest_y:
            # up
            if current_x!=0 and (self.maze[current_x-1][current_y]=="B" or self.maze[current_x-1][current_y]==" ") and [current_x-1, current_y] not in path.stack:
                current_x -= 1
            # down
            elif current_x!=self.height-1 and (self.maze[current_x+1][current_y]=="B" or self.maze[current_x+1][current_y]==" ") and [current_x+1, current_y] not in path.stack:
                current_x += 1
            # left
            elif current_y!=0 and (self.maze[current_x][current_y-1]=="B" or self.maze[current_x][current_y-1]==" ") and [current_x, current_y-1] not in path.stack:
                current_y -= 1
            # right
            elif current_y!=self.length-1 and (self.maze[current_x][current_y+1]=="B" or self.maze[current_x][current_y+1]==" ") and [current_x, current_y+1] not in path.stack:
                current_y += 1
            path.append([current_x, current_y])

            

            # depth first search main implementation
            # check if dead end
            if path.dead_end():
                global dead
                path.remove()
                stack = path.stack
                dead.append(stack[-1])
                index = len(stack)
                while index>=0:
                    index -= 1
                    x,y = stack[index]

                    # up
                    if x!=0 and (self.maze[x-1][y]=="B" or self.maze[x-1][y]==" ") and ([x-1, y] not in stack) and ([x-1, y] not in dead):
                        x -= 1
                        break
                    # down
                    elif x!=self.height-1 and (self.maze[x+1][y]=="B" or self.maze[x+1][y]==" ") and ([x+1, y] not in stack) and ([x+1, y] not in dead):
                        x +=1
                        break
                    # left
                    elif y!=0 and (self.maze[x][y-1]=="B" or self.maze[x][y-1]==" ") and ([x, y-1] not in stack) and ([x, y-1] not in dead):
                        y-=1
                        break
                    # right
                    elif y!=self.length-1 and (self.maze[x][y+1]=="B" or self.maze[x][y+1]==" ") and ([x, y+1] not in stack) and ([x, y+1] not in dead):
                        y+=1
                        break
                    else:
                        dead.append([x,y])
                    
                current_x = x
                current_y = y
                stack = stack[:index+1]
                stack.append([current_x, current_y])
                path.stack=stack
        
        return path



    def generateImage(self):
        """Generating an Image to display the output"""
        img = Image.new('RGB', size=(self.length*100,(self.height)*100), color=(255,255,255))
        draw = ImageDraw.Draw(img)
        
        # font
        font = ImageFont.truetype("ARIAL.woff", 70)

        # plotting
        for i in range(self.height):
            for j in range(self.length):
                if self.maze[i][j]=="#":
                    draw.rectangle(([(j*100,i*100),((j+1)*100,(i+1)*100)]), fill=(120,120,120))
                else:  
                    draw.text((j*100+25, i*100+10),self.maze[i][j],(0,0,0),font=font)
        
        # plotting the solution path
        path = self.solve()
        for i,j in path.stack:
            draw.rectangle(([(j*100,i*100),((j+1)*100,(i+1)*100)]), fill=(255,255,0))

        # plotting A and B
        xa,ya,xb,yb = self.get_start_and_end()
        draw.rectangle(([(ya*100,xa*100),((ya+1)*100,(xa+1)*100)]), fill=(200,30,50))
        draw.rectangle(([(yb*100,xb*100),((yb+1)*100,(xb+1)*100)]), fill=(0,200,0))
        draw.text((ya*100+25, xa*100+10),"A",(0,0,0),font=font)
        draw.text((yb*100+25, xb*100+10),"B",(0,0,0),font=font)

        for i in range(self.length):
            draw.line([(100*i,0),(100*i,100*self.height)], fill=0, width=3)
        for i in range(self.height):
            draw.line([(0,100*i),(100*self.length,100*i)], fill=0, width=3)


        img.show()
        img.save('maze.png')






maze = AI()
maze.solve()
maze.generateImage()


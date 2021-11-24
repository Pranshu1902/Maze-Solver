# Maze solver AI using BFS

import sys
from PIL import Image, ImageDraw, ImageFont


dead = []
all_visited=[]


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
        """Main AI that solves the maze using Breadth First Search"""
        current_x, current_y, dest_x, dest_y = self.get_start_and_end()


        path=[[[current_x, current_y]]]

        global all_visited

        end=False

        while True:
            for ind,p in enumerate(path):

                up=[]
                down=[]
                left=[]
                right=[]

                x=p[-1][0]
                y=p[-1][1]

                # end
                if dest_x==x and dest_y==y:
                    end=True
                    break


                if x!=0 and self.maze[x-1][y]!="#" and [x-1,y] not in p:
                    up=[x-1,y]
                    all_visited.append([x-1,y])
                if x!=self.height-1 and self.maze[x+1][y]!="#" and [x+1,y] not in p:
                    down=[x+1,y]
                    all_visited.append([x+1,y])
                if y!=0 and self.maze[x][y-1]!="#" and [x,y-1] not in p:
                    left=[x,y-1]
                    all_visited.append([x,y-1])
                if y!=self.length-1 and self.maze[x][y+1]!="#" and [x,y+1] not in p:
                    right=[x,y+1]
                    all_visited.append([x,y+1])

                # adding to path

                if len(up)!=0 or len(down)!=0 or len(left)!=0 or len(right)!=0:
                    previous = p[:]
                    path.pop(ind)
                    
                    if up!=[]:
                        previous.append(up)
                        path.append(previous[:])
                        previous.pop()
                    if down!=[]:
                        previous.append(down)
                        path.append(previous[:])
                        previous.pop()
                    if left!=[]:
                        previous.append(left)
                        path.append(previous[:])
                        previous.pop()
                    if right!=[]:
                        previous.append(right)
                        path.append(previous[:])
                        previous.pop()

            if end:
                break

        for i in path:
            if i[-1]==[dest_x, dest_y]:
                return i





    def generateImage(self):
        """Generating an Image to display the output"""
        img = Image.new('RGB', size=(self.length*100,(self.height)*100), color=(255,255,255))
        draw = ImageDraw.Draw(img)
        
        # font
        font = ImageFont.truetype("ARIAL.woff", 70)

        # path
        path = self.solve()

        # plotting
        for i in range(self.height):
            for j in range(self.length):
                if self.maze[i][j]=="#":
                    draw.rectangle(([(j*100,i*100),((j+1)*100,(i+1)*100)]), fill=(120,120,120))
                else:  
                    draw.text((j*100+25, i*100+10),self.maze[i][j],(0,0,0),font=font)
        
        

        # plotting the dead ends(visited paths)
        for i,j in all_visited:
            draw.rectangle(([(j*100,i*100),((j+1)*100,(i+1)*100)]), fill=(255,0,0))
        

        # plotting the solution path
        for i,j in path:
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


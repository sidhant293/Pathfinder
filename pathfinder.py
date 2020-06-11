from tkinter import *
from tkinter import ttk as ttk
import tkinter.messagebox as mb
import time

def calpath(sx,sy,fx,fy):
    m=10000
    i,j=0,0
    stack=[]
    while(fx!=sx or fy!=sy):
        if fx-1>=0 and dist[fx-1][fy]!=0 and dist[fx-1][fy]<m:
            m=dist[fx-1][fy]
            i,j=fx-1,fy
        if fx+1<17 and dist[fx+1][fy]!=0 and dist[fx+1][fy]<m:
            m=dist[fx+1][fy]
            i,j=fx+1,fy
        if fy-1>=0 and dist[fx][fy-1]!=0 and dist[fx][fy-1]<m:
            m=dist[fx][fy-1]
            i,j=fx,fy-1
        if fy+1<size and dist[fx][fy+1]!=0 and dist[fx][fy+1]<m:
            m=dist[fx][fy+1]
            i,j=fx,fy+1
        fx,fy=i,j
        t=(fx,fy)
        stack.append(t)
        #print(t)
    #print(stack)
    while(len(stack)!=0):
        s=stack.pop(-1)
        btn[s[0]][s[1]].config(bg="green")
        root.update()
        time.sleep(0.03)

def caldist(event):
    global sx,sy,ex,ey,fx,fy
    s=(sx,sy)
    e=(ex,ey)
    queue=[]
    queue.append(s)
    vis[s[0]][s[1]]=1
    while(len(queue)!=0):
        q=queue.pop(0)
        if q==e:
            fx=q[0]
            fy=q[1]
            dist[sx][sy]=-1
            calpath(sx,sy,fx,fy)
            #print(dist[fx][fy])
            return
        
        btn[q[0]][q[1]].config(bg="yellow")
        if btn[sx][sy]['bg']=='yellow':
            btn[sx][sy].config(bg="white")
            

        if q[0]-1>=0 and vis[q[0]-1][q[1]]==0:
            t=(q[0]-1,q[1])
            dist[q[0]-1][q[1]]=1+dist[q[0]][q[1]]
            queue.append(t)
            vis[q[0]-1][q[1]]=1

        if q[0]+1<17 and vis[q[0]+1][q[1]]==0:
            t=(q[0]+1,q[1])
            dist[q[0]+1][q[1]]=1+dist[q[0]][q[1]]
            queue.append(t)
            vis[q[0]+1][q[1]]=1

        if q[1]-1>=0 and vis[q[0]][q[1]-1]==0:
            t=(q[0],q[1]-1)
            dist[q[0]][q[1]-1]=1+dist[q[0]][q[1]]
            queue.append(t)
            vis[q[0]][q[1]-1]=1

        if q[1]+1<size and vis[q[0]][q[1]+1]==0:
            t=(q[0],q[1]+1)
            dist[q[0]][q[1]+1]=1+dist[q[0]][q[1]]
            queue.append(t)
            vis[q[0]][q[1]+1]=1
        root.update()
        time.sleep(0.02)
    return

    

def color_change(x,y):
    global flag,sx,sy,ex,ey
    #s=str(x)+' '+str(y)
    vis[x][y]=1
    #btn[x][y].config(text=s)
    btn[x][y].config(bg="black")
    if  flag==1:
        vis[x][y]=0
        ex,ey=x,y
        flag=2
        btn[x][y].config(bg="red")
    if flag==0:
        vis[x][y]=0
        sx,sy=x,y
        flag=1
        btn[x][y].config(bg="white")
        
    
def draw():
    
    x,y = 0,0 # starting position

    for x in range(17):
        for y in range(size):
            btn[x][y]=Button(w,text=' ',fg='white',bg='grey',font='forte 15 ',width=3)   
            btn[x][y].config(command=lambda x1=x,y1=y:color_change(x1,y1))
            btn[x][y].grid(column=y,row=x)



size=35
fx,fy=-1,-1
sx,sy=0,0
ex,ey=0,0
flag=0

btn = [ [0]*size  for n in range(17)] 
vis=[ [0]*size  for n in range(17)]
dist=[ [0]*size  for n in range(17)]

root=Tk()
root.title("Path Finder")
root.geometry("1504x700")
root.resizable(False,False)
root.config(background="grey")

butt1=Button(root,text='Start',fg='white',bg='grey',font='forte 15 ',width=8)
butt1.bind('<Button>',caldist)
butt1.pack()
w=Canvas(root,width=1504,height=700)
w.pack()



        
draw()



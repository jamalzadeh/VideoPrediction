# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:25:43 2020

@author: Milad
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
import seaborn as sns
import pandas as pd

#Static variables
NumberofBalls=2 #max=6
GroundLength=432.0
GroundWidth=288.0
BallRadius=30.0
Speed=80 #pixels/second
FPS=30 #frames/second
NumberofEpisodes=40
EpisodeDuration=2 #seconds
FrameNumbers=int(FPS*EpisodeDuration)
BallColors=['black','red','green','blue','gray','yellow']

NumberOfFrames=2000
XandY=np.random.rand(NumberOfFrames,4)
print(XandY.shape)
XandY=XandY[((XandY[:,0]-XandY[:,1])*GroundLength)**2+((XandY[:,2]-XandY[:,3])*GroundWidth)**2>(2*BallRadius)**2] #x1 x2 y1 y2
print(XandY.shape)
XandY=XandY[XandY[:,0]>BallRadius/GroundLength]
print(XandY.shape)
XandY=XandY[XandY[:,0]<1-(BallRadius/GroundLength)]
print(XandY.shape)
XandY=XandY[XandY[:,1]>BallRadius/GroundLength]
print(XandY.shape)
XandY=XandY[XandY[:,1]<1-(BallRadius/GroundLength)]
print(XandY.shape)

XandY=XandY[XandY[:,2]>BallRadius/GroundWidth]
print(XandY.shape)
XandY=XandY[XandY[:,2]<1-(BallRadius/GroundWidth)]
print(XandY.shape)
XandY=XandY[XandY[:,3]>BallRadius/GroundWidth]
print(XandY.shape)
XandY=XandY[XandY[:,3]<1-(BallRadius/GroundWidth)]
print(XandY.shape)
XandY[:,0]=XandY[:,0]*GroundLength
XandY[:,1]=XandY[:,1]*GroundLength
XandY[:,2]=XandY[:,2]*GroundWidth
XandY[:,3]=XandY[:,3]*GroundWidth


def RunAnimation():    
    fig = plt.figure()
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    ax = plt.axes(xlim=(0, GroundLength), ylim=(0, GroundWidth))
    ax.set_facecolor('white')
    plt.axis('off')
    ##creating list of patches
    Balls = []
    for n in range(NumberofBalls):
        Balls.append(mpl.patches.Circle((XandY[0,n], XandY[0,n+2]), radius = BallRadius, color = BallColors[n], lw = 1, alpha = 0.8, zorder = 4))
    ## adding patches to axis
    for Ball in Balls:
        ax.add_patch(Ball)

    anim = animation.FuncAnimation(fig, animate, frames=XandY.shape[0], fargs=(1,Balls), interval=20, blit=False)
    plt.show()
    anim.save("Videos/Random6.mp4", fps=FPS, extra_args=['-vcodec', 'h264', '-pix_fmt', 'yuv420p'])

def animate(i,episode,Balls):
    for n,ball in enumerate(Balls):
        ball.center = (XandY[i,n], XandY[i,n+2])

RunAnimation()

np.savetxt("Videos/Random6.csv", XandY, delimiter=",", fmt='%s')
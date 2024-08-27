import math
def will_collide(a,b):
    dis=math.sqrt(pow(a[1]-b[1],2)+pow(a[0]-b[0],2))
    rad_sum=a[2]+b[2]
    if(dis<=rad_sum):
         return True
    else:
        return False

ball_1=(0,0,2)
ball_2=(2,0,2)

print("A : ",ball_1,"\nB : ",ball_2)
if (will_collide(ball_1,ball_2)):
    print("A and B are colliding")
else:
    print("A and B are not collding")
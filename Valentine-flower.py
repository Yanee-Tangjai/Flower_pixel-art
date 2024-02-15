def pt():
  a = "🍀🌼🌻🌺🌹🌷🌸 "
  b = "❀❀❀ ---------------- "
  c = " ---------------------- ❀❀❀"
  print()
  print(b+a*8+c)
  print()
  print ("Happy Valentine Yanee! Do you like the flowers? Hope you like them. You always keep the Valentine flowers, so this year you could keep the long-lasting ones since they are digital. LOL")
  print()
  print("                                                                                                                                    Love you as always, Huuman")
  print()
  print(b+a*8+c)

import numpy as np
import matplotlib.pyplot as plt
import random

# res
n = 100
canv = np.zeros((n,n,3))

# blue sky bg
#White
l1w = int(n/2.8)
bgw = [x/255 for x in [224, 255, 255]]
canv[int(n/3):l1w,:,:] = bgw
#L1blue
l1e = int(n/1.2)
bgs_l1 = [x/255 for x in [3, 255, 253]]
canv[l1w:l1e,:,:] = bgs_l1
#L2blue
l2e = int(n/1.05)
bgs_l2 = [x/255 for x in [143, 218, 250]]
canv[l1e:l2e,:,:] = bgs_l2
#L3blue
bgblue = [x/255 for x in [123, 193, 250]]
canv[l2e:,:,:] = bgblue

#Ground
horizon = int(n/3)
hg = [x/255 for x in [10, 105, 33]]
canv[:horizon,:,:] = hg
hg2 = [x/255 for x in [26, 136, 40]]
canv[:horizon-int(n/30),:,:] = hg2
hg3 = [x/255 for x in [148, 197, 140]]
canv[:horizon-int(n/20),:,:] = hg3

hg4 = [x/255 for x in [121, 245, 138]]
p = 13
a = 5
for i in range(n):
  y = 4*a/p*abs((i-p/4)//p-p/2)-a
  canv[:horizon-int(n/10)-int(y),i,:] = hg4

hg5 = [x/255 for x in [152, 255, 152]]
p = 50
a = 5
for i in range(n):
  y = 4*a/p*abs((i-p/4)//p-p/2)-a
  canv[:horizon-int(n/5)-int(y),i,:] = hg5

mbc = [x/255 for x in [166, 218, 223]]
mbp = [x/255 for x in [218, 241, 236]]
mbg = [x/255 for x in [190, 218, 186]]

mh = int(n/3)
mw = int(n/3*4.5)
ms = (mh/mw)*1.5
for i in range(mw):
  if i < mw/3:
    for j in range(horizon,int(ms*i)+horizon):
      canv[j,i,:] = mbp
  elif i < mw:
    ms = ms
    for j in range(horizon,(int(-ms*(i-mw/3)+ms*(mw/3))+horizon)):
      canv[j,i,:] = mbp

mh = int(n/3)
mw = int(n/3*2.5)
ms = (mh/mw)*2
for i in range(mw):
  if i < mw/3:
    for j in range(horizon,int(ms*i)+horizon):
      canv[j,i,:] = mbc
  elif i < mw:
    ms = ms
    for j in range(horizon,(int(-ms*(i-mw/3)+ms*(mw/3))+horizon)):
      canv[j,i,:] = mbc

ni = 15
nf = 25
t = 55
b = 40
for i in range(ni,nf):
  # for j in range(b,int(-2*(i-ni)+t)):
  for j in range(b,t):
    if j == i+b-ni:
      canv[j,i,:] = mbp

for ni in range(18,20):
  nf = ni+15
  t = 50
  b = 40
  for i in range(ni,nf):
    # for j in range(b,int(-2*(i-ni)+t)):
    for j in range(b,t):
      if j == i+b-ni:
        canv[j,i,:] = mbg

############## SF ##############

##### STM ########
stc = [x/255 for x in [71, 84, 85]]

control_point = [60, 60]  # Control point for the curve
end_point = [80, 0]  # Ending point for the curve
for t in np.linspace(0, 1, 100):
    x = int((1-t)**2 * 10 + 2 * (1-t) * t * control_point[0] + t**2 * end_point[0])
    y = int((1-t)**2 * 20 + 2 * (1-t) * t * control_point[1] + t**2 * end_point[1])
    if 60 <= x < n and 0 <= y < n:
        canv[y, x-1:x+1, :] = stc


###### PETL ##########
px = 60
py = 30
sfp = [x/255 for x in [255, 173, 41]]
for rr in np.arange(1,15):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(5/2* theta)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    # if 0<=x<=r and 0<=y<=r:
    canv[y+py,x+px,:] = sfp

px = 60
py = 30
sfp = [x/255 for x in [255, 234, 0]]
for rr in np.arange(1,14):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(5/2* theta)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    # if 0<=x<=r and 0<=y<=r:
    canv[y+py,x+px,:] = sfp

px = 60
py = 30
sfin = [x/255 for x in [141, 61, 50]]
for rr in np.arange(1,9):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    # if 0<=x<=r and 0<=y<=r:
    canv[y+py,x+px,:] = sfin

px = 60
py = 30
sfinr = [x/255 for x in [233, 99, 46]]
for rr in np.arange(1,7):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = sfinr

for rr in np.arange(1,7):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    if random.random() <0.05:
      canv[y+py,x+px,:] = sfin

#### LF ####
px = 75
py = 15
lc = [x/255 for x in [95, 133, 117]]
for rr in np.arange(1,8):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-np.pi/4)/4)*8) + abs(np.sin((theta-np.pi/4)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lc

lci = [x/255 for x in [53, 94, 59]]
for rr in np.arange(1,3):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-np.pi/4)/4)*8) + abs(np.sin((theta-np.pi/4)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lci

px = 75
py = 5
lc = [x/255 for x in [95, 133, 117]]
for rr in np.arange(1,8):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-3*np.pi/3)/4)*8) + abs(np.sin((theta-3*np.pi/3)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lc
lci = [x/255 for x in [53, 94, 59]]
for rr in np.arange(1,3):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-3*np.pi/3)/4)*8) + abs(np.sin((theta-3*np.pi/3)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lci

############## SF ##############

############ ROS ##############
##### STM ########
control_point = [50, 20]  # Control point for the curve
end_point = [65, 0]  # Ending point for the curve
for t in np.linspace(0, 1, 100):
    x = int((1-t)**2 * 10 + 2 * (1-t) * t * control_point[0] + t**2 * end_point[0])
    y = int((1-t)**2 * 20 + 2 * (1-t) * t * control_point[1] + t**2 * end_point[1])
    if 50 <= x < n and 0 <= y < n:
        canv[y, x-1:x+1, :] = stc

control_point = [10, 20]  # Control point for the curve
end_point = [15, 0]  # Ending point for the curve
for t in np.linspace(0, 1, 100):
    x = int((1-t)**2 * 10 + 2 * (1-t) * t * control_point[0] + t**2 * end_point[0])
    y = int((1-t)**2 * 20 + 2 * (1-t) * t * control_point[1] + t**2 * end_point[1])
    if 0 <= x < n and 0 <= y < n:
        canv[y, n-x-1:n-x+1, :] = stc

### PETL #########

px = 90
py = 20
phi = 3*np.pi/4
pkc = [x/255 for x in [248, 131, 121]]
pkc = [x/255 for x in [255, 182, 193]]
for rr in np.arange(1,10):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(1/3* (theta+phi))
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = pkc

sfp = [x/255 for x in [243, 58, 10]]
for rr in np.arange(1,10,2):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(1/3* (theta+phi))
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    # if 0<=x<=r and 0<=y<=r:
    canv[y+py,x+px,:] = sfp

px = 50
py = 10
phi = np.pi/4
for rr in np.arange(1,10):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(1/3* (theta+phi))
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = pkc

for rr in np.arange(1,10,2):
  for theta in np.linspace(0,4*np.pi,500):
    r = rr * np.cos(1/3* (theta+phi))
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    # if 0<=x<=r and 0<=y<=r:
    canv[y+py,x+px,:] = sfp

px = 90
py = 5
lc = [x/255 for x in [95, 133, 117]]
for rr in np.arange(1,7):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-np.pi/4)/4)*8) + abs(np.sin((theta-np.pi/4)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lc

lci = [x/255 for x in [53, 94, 59]]
for rr in np.arange(1,3):
  for theta in np.linspace(0,4*np.pi,500):
    d = abs(np.cos((theta-np.pi/4)/4)*8) + abs(np.sin((theta-np.pi/4)/4)/5)
    r = rr/d**(1/2)
    x = int(r*np.cos(theta))
    y = int(r*np.sin(theta))
    canv[y+py,x+px,:] = lci
############ ROS ##############

def create_circle_mask(radius):
    mask = np.zeros((2*radius+1, 2*radius+1))
    for y in range(-radius, radius+1):
        for x in range(-radius, radius+1):
            if x**2 + y**2 <= radius**2:
                mask[radius+y, radius+x] = 1
    return mask

cloud_c = np.array([1, 1, 1])
for x in range(10,20):
  # for y in range(65,70):
    y = 70
    size = np.random.randint(2, 5)
    opacity = np.random.uniform(0.2, 0.5)
    cloud_mask = create_circle_mask(size)
    cloud_pixels = np.where(cloud_mask == 1)
    for i in range(len(cloud_pixels[0])):
        canv[y-cloud_pixels[0][i], x-cloud_pixels[1][i], :] += cloud_c * opacity

for x in range(20,40):
  # for y in range(65,70):
    y = 72
    size = np.random.randint(2, 5)
    opacity = np.random.uniform(0.2, 0.5)
    cloud_mask = create_circle_mask(size)
    cloud_pixels = np.where(cloud_mask == 1)
    for i in range(len(cloud_pixels[0])):
        canv[y-cloud_pixels[0][i], x-cloud_pixels[1][i], :] += cloud_c * opacity

for x in range(70,90):
  # for y in range(65,70):
    y = 60
    size = np.random.randint(2, 5)
    opacity = np.random.uniform(0.2, 0.5)
    cloud_mask = create_circle_mask(size)
    cloud_pixels = np.where(cloud_mask == 1)
    for i in range(len(cloud_pixels[0])):
        canv[y-cloud_pixels[0][i], x-cloud_pixels[1][i], :] += cloud_c * opacity

for x in range(50,75):
  # for y in range(65,70):
    y = 80
    size = np.random.randint(2, 5)
    opacity = np.random.uniform(0.2, 0.5)
    cloud_mask = create_circle_mask(size)
    cloud_pixels = np.where(cloud_mask == 1)
    for i in range(len(cloud_pixels[0])):
        canv[y-cloud_pixels[0][i], x-cloud_pixels[1][i], :] += cloud_c * opacity


plt.imshow(canv)
plt.gca().invert_yaxis()

# print(f"For more funny story click https://colab.research.google.com/drive/1AD6Jg9luG84K6EsDHRHVIjg6nel1mKUU?usp=sharing")
pt()

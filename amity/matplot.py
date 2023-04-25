#matplot
#1
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))

plt.show()


#2
import matplotlib.pyplot as plt
import numpy as np

x = np.arrange(0,10,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.title('sine wave')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#3
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)

plt.scatter(x,y,c=colors)
plt.title('scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#4
import matplotlib.pyplot as plt

x = ['A', 'B' , 'C' ,'D']
y = [10,20,30,40]

plt.bar(x,y)
plt.title('bar plot')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()

#5
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)

plt.hist(x,bins=20)
plt.title('Histogram')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show()

#6

import matplotlib.pyplot as plt

x = ['A', 'B' , 'C' ,'D']
y = [20,30,40,10]

plt.pie(values,labels=labels, autopct=)
plt.title('pie chart')
plt.show()

#7
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()

#8
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints)
plt.show()

#9
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()

#10

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10,5,7])

plt.plot(ypoints)
plt.show()

#11

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='o')
plt.show()

#12

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='*')
plt.show()

#13
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='o', ms=20)
plt.show()

#14

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='o', ms=20, mec = 'r')
plt.show()

#15

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='o', ms=20, mfc = 'r')
plt.show()

#16
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='o', ms=20, mfc = 'r',mec = 'r')
plt.show()

#17
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,linestyle = 'dotted')
plt.show()

#18

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,linewidth = '20.5')
plt.show()

#19
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.title('Sports watch data')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

plt.plot(x,y)
plt.grid(color = 'green', linestyle='--',linewidth = 0.5)
plt.show()

#20
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.title('Sports watch data')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

plt.plot(x,y)
plt.grid()
plt.show()

#21

#plot1
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()

#22
#plot1
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title('Sales')

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,1,2)
plt.plot(x,y)
plt.title('Income')

plt.suptitle('My show')
plt.show()

#23
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])


plt.scatter(x,y)
plt.show()


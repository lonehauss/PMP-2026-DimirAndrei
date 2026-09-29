import numpy as np

np.random.seed(12)
#urna = ["red","red","red","blue","blue","blue","blue","black","black"]

def roll():
    urna = ["red", "red", "red", "blue", "blue", "blue", "blue", "black", "black"]
    roll = np.random.randint(1,7)
    if roll in [2,3,5]:
        urna.append("black")
    elif roll == 6:
        urna.append("red")
    else:
        urna.append("blue")
    return np.random.choice(urna)

N=1000
results = np.array([roll() for _ in range(N)])
reds = (results == "red")
print(reds.sum()/N)

#sansa teoretic e 19/60 =~ 0.31


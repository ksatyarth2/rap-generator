
# In[36]:


import numpy as np
def opfile(file):
    with open(file) as f:
        data = f.read()
        return data
# In[65]:
def table(data,k=5):
    Tab={}
    for i in range(len(data)-k):
        x=data[i:i+k]
        y=data[i+k]
        if Tab.get(x) is None:
            Tab[x]={}
            Tab[x][y]=1
        else:
            if Tab[x].get(y) is None:
                Tab[x][y]=1
            else:
                Tab[x][y]+=1
    return Tab
# In[67]:
def predict(seed,tab,k=5):
    inp = seed[-k:]
    
    possibliteis = tab[inp]
    
    freq = list(possibliteis.values())
    
    options = list(possibliteis.keys())
    probabs = [float(ele)/float(sum(freq)) for ele in freq]
    
    next_char = np.random.choice( options , p = probabs )
    
    return next_char
# In[73]:
def rapthis(file,seed="apna time"):
    # data=opfile(file)
    data=file
    tab=table(data.lower())
    # seed="time aayega"
    for i in range(len(data)):
        nextc=predict(seed,tab)
        seed+=nextc
    return seed

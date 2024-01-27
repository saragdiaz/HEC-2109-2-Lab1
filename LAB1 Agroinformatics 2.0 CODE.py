#!/usr/bin/env python
# coding: utf-8

# In[20]:


def backwfunction2(input_file, output_file):
    
    with open(input_file, 'r') as f:
            with open(output_file, 'w') as fw:
                fw.write(f.read()[::-1])
                print("Check Home to find your text reversed")


input_file = 'PLimerick.txt'  # this will change depending on the name of the file you want to reverse

output_file = 'PLimerick_backward.txt'  # change this too to make it organized
reverse_file(input_file, output_file)


# In[ ]:





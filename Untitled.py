#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psi4
import numpy as np


# In[10]:


# Initial setup
psi4.set_memory('2 GB')
psi4.set_num_threads(2)

file_prefix = 'methane_HF-DZ'

ch4 = psi4.geometry("""
symmetry c1
0 1
   C       -0.85972        2.41258        0.00000
   H        0.21028        2.41258        0.00000
   H       -1.21638        2.69390       -0.96879
   H       -1.21639        3.11091        0.72802
   H       -1.21639        1.43293        0.24076
""")


# In[11]:


# Geometry optimization
psi4.set_output_file(file_prefix + '_geomopt.dat', False)
psi4.set_options({'g_convergence': 'gau_tight'})
psi4.optimize('scf/cc-pVDZ', molecule=ch4)


# In[12]:


# Run vibrational frequency analysis
psi4.set_output_file(file_prefix + '_vibfreq.dat', False)
scf_energy, scf_wfn = psi4.frequency('scf/cc-pVDZ', molecule=ch4, return_wfn=True, dertype='gradient')


# In[13]:


# Save "raw" frequencies into a variable
print(scf_wfn.frequency_analysis) # this command is just to get you started!


# In[14]:


print(scf_wfn.frequency_analysis['omega'])


# In[15]:


print(scf_wfn.frequency_analysis['omega'][2])


# In[19]:


freqs = scf_wfn.frequency_analysis['omega'][2]


# In[20]:


# Eliminate imaginary parts of frequencies,
np.real(freqs)


# In[25]:


realfreq = np.real(freqs)


# In[26]:


#Real numbers
np.round(realfreq)


# In[38]:


#Non-zero values. Taking all of the values except for the first 6 values which are zero
np.round(realfreq[6:])


# In[40]:


print (np.round(realfreq[6:]))


# In[41]:


roundfreq = np.round(realfreq[6:])


# In[91]:


unique,counts=np.unique(roundfreq,return_counts=True)


# In[94]:


print(unique)
print(counts)


# In[99]:


x=np.transpose(np.vstack((unique,counts)))


# In[100]:


print(x)


# In[102]:


np.savetxt(fname='CH4-frequencylist.dat', X=x, fmt='%.1f %d', delimiter=',')


# In[ ]:





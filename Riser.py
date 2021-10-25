#!/usr/bin/env python
# coding: utf-8

# # Monitor Riser
# > Andrew Reid (@madeformaking)
# 
# Units: milimeters (mm)
# 
# [Pinterest - Monitor riser](https://www.pinterest.co.uk/search/pins/?q=monitor%20riser&rs=typed&term_meta[]=monitor%7Ctyped&term_meta[]=riser%7Ctyped)
# 
# [Yeggi - Monitor riser](https://www.yeggi.com/q/monitor+riser/)
# 
# [Thingiverse](https://www.thingiverse.com/thing:4687708)

# In[76]:


import cadquery as cq
#from jupyter_cadquery.cadquery import show

#from jupyter_cadquery import set_sidecar

#set_sidecar("CadQuery")


# In[206]:


length = 200
width = 50
height = 50
thickness = 10
fillet_radius_internal = 10
fillet_radius_external = fillet_radius_internal+thickness


# In[209]:


result = (
    cq.Workplane("XY").box(length, width, height)
        .moveTo(0,thickness/2)
        .rect(length-(2*thickness), height-thickness)
        .cutThruAll()
        .edges("Z and (not >>Y) and (not <<Y)")
        #.size()
        .fillet(fillet_radius_internal)
        .edges("<Y and |Z")
        .fillet(fillet_radius_external)
)
#show(result)


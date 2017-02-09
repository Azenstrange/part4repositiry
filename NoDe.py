# -*- coding: utf-8 -*-
"""
this is the function count(on node) of the exercice 4

@author: Eisenfisz
"""

def none (B,h):
     if(B.left == none && B.right == none):
          return (h)
     h += 1
     if(B.left==none):
          return (none(B.right,h))
     elif (B.right == none):
          return (none(B.left,h))
     else:
          return (none(B.left, h), none(B.right,h))
def nope(B):
     h= 0
     return(none(B,h))
     

# AUTHOR : SAYAN BHATTACHARJEE
# EMAIL  : aero.sayan@gmail.com
# LICENSE: DEFAULT, and will remain so.
# FILE   : blitzer_tree_utilities.py
# INFO   : tree utilities module for competitive programming.
# STYLE  : smaller case with underscore for speed

#===============================================================================
#                                UTILITIES
#===============================================================================

#----------------------------------------
# Inorder traversal
def trav_inorder(_root):
    if(_root):
        trav_inorder(_root.left)
        print(_root.val)
        trav_inorder(_root.right)
#----------------------------------------
# Postorder traversal
def trav_postorder(_root):
    pass

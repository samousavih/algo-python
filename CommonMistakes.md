1) for maps always use ``x in map`` or ``x not in map``
2) for a binary search or similar algo use ``(start+end)//2``
3) ```int(int(first)/int(second))`` does return always truncate to Zero while ``(start+end)//2`` would always truncate down ``-3/2 = -2(-1.5)``
4) to check if a string is a number you can do ``i.isnumeric()``
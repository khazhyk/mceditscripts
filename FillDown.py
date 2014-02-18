# FillDown.py - Finds the lowest block in each column and fills down to y=0 below that.
# Made by khazhyk

inputs = (
    ("Fill with","blocktype"),
)

displayNmae = "Fill Down"

def perform(level,box,options):
    blockType = 7
    for x in range(box.minx, box.maxx):
        for z in range(box.minz, box.maxz):
            lowestblock = 0
            foundblock = False
            for y in range(box.maxy, 0):
                if level.blockAt(x,y,z).ID != 0:
                    lowestblock = y
                    foundblock = True
            for y in range(0, lowestblock):
                level.setBlockAt(x,y,z,blockType)
            foundblock = False
        chunk = level.getChunk(x/16, z/16)
        chunk.dirty = True



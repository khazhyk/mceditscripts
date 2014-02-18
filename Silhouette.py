# Silhouette.py - Casts a Silhouette of the map onto y=0
# Made for use with PGM v2.0 Voidmatcher
# Made by khazhyk

import sys

inputs = (
    ("Fill with","blocktype"),
)

displayName = "Silhouette"

def perform(level,box,options):
    blockType = options["Fill with"].ID
    #sys.stdout.write("Hello "+str(box.minx)+" "+str(box.maxx)+" "+str(box.minz)+" "+str(box.maxz)+" "+str(box.maxy))
    for x in range(box.minx, box.maxx):
        for z in range(box.minz, box.maxz):
            foundblock = False
            for y in range(box.maxy, -1, -1): # Loop Backwards from maxy to 0
                if level.blockAt(x,y,z) != 0:
                    foundblock = True
                    break # If we found one, we're done
            if foundblock: # If we found a block in this column
                if level.blockAt(x,0,z) == 0: # Only set the block if there isn't already one there.
                    level.setBlockAt(x,0,z,blockType) # Set the block
                    chunk = level.getChunk(x/16, z/16)
                    chunk.dirty = True
                foundblock = False

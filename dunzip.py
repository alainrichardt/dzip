import sys
import os.path as path

def decodeByte( byte, lastb_length = None):
    quad = ''
    quad += dnaDecode( 0b00000011 & byte )
    quad += dnaDecode( 0b00000011 & (byte >> 2) )
    quad += dnaDecode( 0b00000011 & (byte >> 4) )
    quad += dnaDecode( 0b00000011 & (byte >> 6) )
    return quad

def dnaDecode( byte ):
    if( byte == 0b00 ):
        return 'A'
    elif( byte == 0b01 ):
        return 'C'
    elif( byte == 0b10 ):
        return 'G'
    elif( byte == 0b11 ):
        return 'T'

if __name__ == "__main__":
    if ( len(sys.argv) != 3 ):
        print 'usage: dunzip.py <input file> <output file>'
        sys.exit(1)

    out = open(sys.argv[2], "wb")
    inp = open(sys.argv[1], "rb")

    # Read the header
    headr = inp.read(5)
    lastbyte = inp.read(1)
    if( headr != 'DNAZ1' ):
        print 'Error : Only DNAZ protocol v1 files supported'
        sys.exit()

    byte = None
    while byte == None or byte != "":
        byte = inp.read(1)
        if (len(byte) > 0):
            out.write(decodeByte( ord(byte) ))


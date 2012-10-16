import sys
import os.path as path

def decodeByte( byte, lastb_length = None):

    quad = ''

    if lastb_length == None or lastb_length > 0:
        quad += dnaDecode( 0b00000011 & byte )
    
    if lastb_length == None or lastb_length > 1:
        quad += dnaDecode( 0b00000011 & (byte >> 2) )

    if lastb_length == None or lastb_length > 2:
        quad += dnaDecode( 0b00000011 & (byte >> 4) )

    if lastb_length == None:
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
    headr = inp.read(4)
    lastbyte = inp.read(1)

    if( headr != 'DNAZ' ):
        print 'Error : Only DNAZ protocol v1 files supported'
        sys.exit()

    filesize = path.getsize(sys.argv[1]) - 4  # 4 bytes for header
    bytes_read = 1
    while bytes_read < filesize:
        bytes_read = bytes_read + 1
        byte = inp.read(1)
        
        if (len(byte) > 0) and bytes_read == filesize and lastbyte != '0':
            out.write(decodeByte( ord(byte), ord(lastbyte) ))
        else:
            out.write(decodeByte( ord(byte) ))


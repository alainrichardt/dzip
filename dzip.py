import sys
import os.path as path

def encodeByte( bytes ):
    result = 0
    if( len(bytes) > 0 ):
        result = dnaEncode( bytes[0] )
    if( len(bytes) > 1 ):
        result = result | ( dnaEncode(bytes[1]) << 2 )
    if( len(bytes) > 2 ):
        result = result | ( dnaEncode(bytes[2]) << 4 )
    if( len(bytes) > 3 ):
        result = result | ( dnaEncode(bytes[3]) << 6 )
    return chr(result)

def dnaEncode( byte ):
    if( byte == 'A' ):
        return 0b00;
    elif( byte == 'C'):
        return 0b01;
    elif( byte == 'G'):
        return 0b10;
    elif( byte == 'T'):
        return 0b11;

if __name__ == "__main__":
    if ( len(sys.argv) != 3 ):
        print 'usage: dzip.py <input file> <output file>'
        sys.exit(1)

    out = open(sys.argv[2], "wb")

    # Generate header
    out.write( 'DNAZ' )
    out.write( str( path.getsize(sys.argv[1]) % 4 ) )

    with open(sys.argv[1], "rb") as f:
        bytes = None
        while bytes == None or bytes != "":
            bytes = f.read(4)
            if (len(bytes) > 0):
              out.write( encodeByte(bytes) )


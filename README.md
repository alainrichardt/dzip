dzip
====

Python Compression Lib for DNA Sequencer .DAT (raw) output

=====================================
DNA Compression Script
- Alain Richardt

The dzip app will compress DNA strings, written for tom at Canterbury University.

Usage:

dzip <input file> <output file>
dunzip <input file> <output file>

By convention compressed files should have the '.dz' extension.

Included in this repo is the sample DNA requence for the Acaryochloris Marina Bacteria

.dz File Format
=====================================
At the moment, DNA info is stored in the DAT format which is the raw output of the gene sequencers used in the lab. They currently store A,C,T,G sequences in single bytes, but since there's only 4 distinct types that 8 bit pattern can be reduced to 2 bits, allowing a 4x increase in storage efficiency.

.dz file format uses the following method to compress the DNA pairs.

A - Adenine  - 00
C - Cytosine - 01
G - Guanine  - 10
T - Thymine  - 11

The DNA sequence is stored in bytes, a single byte represents 4 base pairs. When the input sequence is not a multiple of 4, then the last byte may not be a complete pair, this is indicated in the file header

File Header
  Bytes     Explanation
  4         'DNAZ' Indicating this is a '.dz' file
  1         Single byte indicating the number of sequences stored in the last
            byte. Either '1,2,3 or 4'

File Data
The remainder of the bytes in the file is the encoded data. The length of data in the last byte is indicated in the header.


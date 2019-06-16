import sys

f = open(sys.argv[1],"r")
fasta = f.read()
newfile=''
for nuc in fasta:
    if nuc != ' ' or nuc not in '0123456789':
        newfile+=nuc
        
f.close()
print newfile

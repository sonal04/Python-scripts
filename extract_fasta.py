### extract fasta sequences for list of ids from a concatenated fasta file

from Bio import SeqIO

def getSeqRec(seq_id): 
    fasta = SeqIO.parse(fastafile, "fasta")
    for record in fasta:
        
        if seq_id == record.id:

            return record

with open(idlist_file, 'w') as f:
    for line in open(outputfile, "r"):
        line =line.strip()
        seq_rec=getSeqRec(line)
        #print ">"+seq_rec.id + '\n' + seq_rec.seq
        f.write("%s\n" % str(">"+seq_rec.id + '_' + seq_rec.description + '\n' + seq_rec.seq))


import sys
genomes = open ('RR_HK_coli_description.txt') #already sorted
#by genome names and 'from' co-ordinate
orig_stdout = sys.stdout
res = open('RR_HK_coli_separatedbyline.txt','w')    
sys.stdout = res

previous_genome=""
#prev=""

for genome in genomes:
##        genome2 = genome.split('\n')
##        print genome2[2]
        genome = genome.split('\t')
        #print abs(int(genome[11]))
        if abs(int(genome[12])) > 1500:
                print
        
##        print ('\t'.join(genome)).strip()
        
        if not previous_genome:
                previous_genome = genome[5]
                     
        elif previous_genome != genome[5]:
                print
##        if not prev:
##                prev = genome[0]
##        elif prev != genome[0]:
##                print
        ans= ('\t'.join(genome)).strip()
        ans1= ans.replace("\n\n", "")
        print ans


        
        previous_genome=genome[5]
        #prev = genome[0]
	
sys.stdout = orig_stdout
res.close()


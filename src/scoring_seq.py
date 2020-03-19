#!/usr/bin/python3
import argparse
import math

if __name__ == "__main__":
    
    print("START checking_sequence")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input file path')
    parser.add_argument('-o', help='output file path')
    parser.add_argument('-sT', help='Use # as a threshold of letter percentage on raw sequence (default : 5)', default=5)
    args = parser.parse_args()

    in_f_name = args.i    
    out_f_name = args.o
    checking_threshold = int(args.sT)

    in_f = open(in_f_name, 'r')
    out_f = open(out_f_name, 'w')
    
    base_total_count = 0
    bases_count = [0 for i in range(130)] 
 
    while True:
        line = in_f.readline()
        if not line:
            break
        
        raw_sequence = line.split("\n")[0]
        raw_sequence_length = len(raw_sequence)
        base_total_count = base_total_count + raw_sequence_length
        
        for i in range(0, raw_sequence_length):
            bases_count[ord(raw_sequence[i])] = bases_count[ord(raw_sequence[i])] + 1 

            
    scoring_bases_and_count = list()
    priority_scoring_bases_and_count = list()
    priority_bases = list()

    for i in range(len(bases_count)):
        if(( bases_count[i] * 100 / (base_total_count+1) ) > checking_threshold):
            scoring_bases_and_count.append([bases_count[i],i])
    
    priority_scoring_bases_and_count = sorted(scoring_bases_and_count, reverse=True)
    
    for i in range(len(priority_scoring_bases_and_count)-1):
        priority_bases.append(priority_scoring_bases_and_count[i][1])

    print("END checking_sequence")
    print("START scoring_sequence")

    in_f.seek(0)
    while True:
        line = in_f.readline()
        if not line:
            break
        
        raw_sequence = line.split("\n")[0]
        raw_sequence_length = len(raw_sequence)
        bases_count = [0 for i in range(130)]   
    
        for i in range(0, raw_sequence_length):
            bases_count[ord(raw_sequence[i])] = bases_count[ord(raw_sequence[i])] + 1
                      
        for i in priority_bases:
            score = round(bases_count[i]/(raw_sequence_length+1)*5)
            out_f.write(str(score)) 
            
        for i in priority_bases:
            score = round(bases_count[i]/(raw_sequence_length+1)*25)
            if (score == 0):
                out_f.write("00") 
            elif (score < 10):
                out_f.write("0") 
                out_f.write(str(score)) 
            else: 
                out_f.write(str(score)) 
                
        out_f.write("\n")

    in_f.close()    
    out_f.close()
    
    print("END scoring_sequence")


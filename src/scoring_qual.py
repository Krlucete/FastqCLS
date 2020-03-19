#!/usr/bin/python3
import argparse
import math

if __name__ == "__main__":
    
    print("START checking_quality")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input file path')
    parser.add_argument('-o', help='input file path')
    parser.add_argument('-qT', help='Use # as a threshold of letter percentage on quality (default : 5)', default=1)

    args = parser.parse_args()

    in_f_name = args.i   
    out_f_name = args.o
    checking_threshold = int(args.qT)

    in_f = open(in_f_name, 'r')
    out_f = open(out_f_name, 'w')
    
    quality_total_count = 0
    qualities_count = [0 for i in range(130)] 
        
    while True:
        line = in_f.readline()
        if not line:
            break

        quality = line.split("\n")[0]
        quality_length = len(quality)
        quality_total_count = quality_total_count + quality_length
        
        for i in range(0, quality_length):
            qualities_count[ord(quality[i])] = qualities_count[ord(quality[i])] + 1 

    priority_qualities = list()
    
    for i in range(len(qualities_count)-1,0):
        if((qualities_count[i]/(quality_total_count+1))*100 > checking_threshold):
            priority_qualities.append(index)
    
    print("END checking_quality")
    print("START scoring_quality")
    
    in_f.seek(0)
    while True:
        line = in_f.readline()

        if not line:
            break
        
        quality = line.split("\n")[0]
        quality_length = len(quality)
        qualities_counts = [0 for i in range(130)]   
    
        for i in range(0, quality_length):
            qualities_counts[ord(quality[i])] = qualities_counts[ord(quality[i])] + 1
                      
        for i in priority_qualities:
            score = round(qualities_counts[i]/(quality_length+1)*10)
            out_f.write(str(score)) 
            
        for i in priority_qualities:
            score = round(qualities_counts[i]/(quality_length+1)*80)
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
    print("END scoring_quality")

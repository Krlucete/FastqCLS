#!/usr/bin/python3
import argparse
import math

if __name__ == "__main__":
    print("START scoring_qual")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input file path')
    parser.add_argument('-o', help='input file path')
    
    args = parser.parse_args()

    in_f_name = args.i    
    in_f = open(in_f_name, 'r')

    out_f_name_seq = args.o
    output_file_seq = open(out_f_name_seq, 'w')
    
    seq_cnt_list = [0 for i in range(130)] 
    total_seq_cnt = 0
    count = 0
    while True:
        first_line = in_f.readline()
        
        if not first_line:
            break

        read_1_seq = first_line.split("\n")[0]
                
        line_length = len(read_1_seq)
        total_seq_cnt = total_seq_cnt + line_length
        for i in range(0, line_length):
            seq_cnt_list[ord(read_1_seq[i])] = seq_cnt_list[ord(read_1_seq[i])] + 1 

    check_ord_list = list()
    
    for i in range(len(seq_cnt_list)):
        index = len(seq_cnt_list) - i -1
        if((seq_cnt_list[index]/(total_seq_cnt+1))*100>1):
            count = count + seq_cnt_list[index]
            check_ord_list.append(index)
    
    in_f.seek(0)
    while True:
        first_line = in_f.readline()

        if not first_line:
            break
        
        read_1_seq = first_line.split("\n")[0]
        line_length = len(read_1_seq)
        seq_cnt_list = [0 for i in range(130)]   
    
        for i in range(0, line_length):
            seq_cnt_list[ord(read_1_seq[i])] = seq_cnt_list[ord(read_1_seq[i])] + 1
                      
        for i in check_ord_list:
            score = round(seq_cnt_list[i]/(line_length+1)*10)
            output_file_seq.write(str(score)) 
        for i in check_ord_list:
            score = round(seq_cnt_list[i]/(line_length+1)*80)
            if (score == 0):
                output_file_seq.write("00") 
            elif (score < 10):
                output_file_seq.write("0") 
                output_file_seq.write(str(score)) 
            else: 
                output_file_seq.write(str(score)) 
        output_file_seq.write("\n")

    in_f.close()    
    output_file_seq.close()
    print("END scoring_qual")

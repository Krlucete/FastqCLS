#!/usr/bin/python3
import argparse
import math

if __name__ == "__main__":
    print("START scoring_seq")
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
#         if(total_seq_cnt==100):
#             break
        
        read_1_seq = first_line.split("\n")[0]
                
        line_length = len(read_1_seq)
        total_seq_cnt = total_seq_cnt + line_length
        for i in range(0, line_length):
            seq_cnt_list[ord(read_1_seq[i])] = seq_cnt_list[ord(read_1_seq[i])] + 1 

    check_ord_list = list()
    sort_check_ord_list = list()
    sort_check_ord = list()
    
    for i in range(len(seq_cnt_list)):
        if((seq_cnt_list[i]*100/(total_seq_cnt+1))>5):
            tmp = [seq_cnt_list[i],i]
            count = count + seq_cnt_list[i]
            check_ord_list.append(tmp)
    
    sort_check_ord_list = sorted(check_ord_list, reverse=True)
    
    for i in range(len(sort_check_ord_list)-1):
        sort_check_ord.append(sort_check_ord_list[i][1])
 
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
                      
        for i in sort_check_ord:
            score = round(seq_cnt_list[i]/(line_length+1)*5)
            output_file_seq.write(str(score)) 
        for i in sort_check_ord:
            score = round(seq_cnt_list[i]/(line_length+1)*25)
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
    print("END scoring_seq")


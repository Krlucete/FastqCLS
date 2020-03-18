import subprocess
import shlex
import argparse
import glob
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input file path')
    parser.add_argument('-t', help='num of threads', default='8')
    args = parser.parse_args()
    
    
    threads = args.t
    input = args.i
    
    hash = random.getrandbits(128)
    output = input.split(sep=".")[0] + str(hash)
    
    command = "mkdir " + output
    subprocess.check_call(command, shell=True) 
        
    command = "split -n r/4 " + input + " " + output + "/" 
    subprocess.check_call(command, shell=True)
    
    command = "mv " + output + "/ac "+ input.split(sep=".")[0] +".third_line" 
    subprocess.check_call(command, shell=True)   
    command = "rm -f " + output+"/ac "
    subprocess.check_call(command, shell=True)    
    
    command = "cut -f 1 -d ' ' " + output + "/aa > " + output +"/id_front"
    subprocess.check_call(command, shell=True)
    command = "cut -f 2 -d ' ' " + output + "/aa > " + input.split(sep=".")[0] +".id_back" 
    subprocess.check_call(command, shell=True)

    command = "rm -f " + output + ".aa"
    subprocess.check_call(command, shell=True)
    
    command = "pypy scoring_seq.py -i " + output + "/ab -o " + output + "/score_seq"
    subprocess.check_call(command, shell=True)

    command = "pypy scoring_qual.py -i " + output + "/ad -o " + output + "/score_qual"
    subprocess.check_call(command, shell=True)
    
    command = "paste -d' ' " + output + "/ab " + output +"/id_front " + output + "/score_seq | sort -k3 -k1 > " + output + "/sort_seq"
    subprocess.check_call(command, shell=True)    
    command = "paste -d' ' " + output + "/ad " + output +"/id_front " + output + "/score_qual | sort -k3 -k1 > " + output + "/sort_qual"
    subprocess.check_call(command, shell=True) 
    
    command = "rm -f " + output + "/ab"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/ad"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/score_seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/score_qual"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/id_front"
    subprocess.check_call(command, shell=True)  

    command = "cut -f1 -d' ' " + output + "/sort_seq > " + input.split(sep=".")[0] + ".sorted_seq"
    subprocess.check_call(command, shell=True)   
    command = "cut -f2 -d' ' " + output + "/sort_seq > " + input.split(sep=".")[0] + ".sorted_seq_id" 
    subprocess.check_call(command, shell=True)   
    command = "cut -f1 -d' ' " + output + "/sort_qual > " + input.split(sep=".")[0] + ".sorted_qual" 
    subprocess.check_call(command, shell=True)   
    command = "cut -f2 -d' ' " + output + "/sort_qual > " + input.split(sep=".")[0] + ".sorted_qual_id" 
    subprocess.check_call(command, shell=True)

    command = "rm -rf " + output
    subprocess.check_call(command, shell=True)
    
    command = "rm -f " + input.split(sep=".")[0] + ".abc_zpaq"
    subprocess.check_call(command, shell=True)
    
    command = "zpaq -m5 a " + input.split(sep=".")[0] +".abc_zpaq "+input.split(sep=".")[0]+".sorted_seq_id "+input.split(sep=".")[0]+".sorted_qual_id "+input.split(sep=".")[0]+".id_back "+input.split(sep=".")[0]+".sorted_seq "+input.split(sep=".")[0]+".sorted_qual "+input.split(sep=".")[0]+".third_line"
    subprocess.check_call(command, shell=True)    
   
 
    command = "rm -f "+input.split(sep=".")[0]+".third_line"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".id_back"
    subprocess.check_call(command, shell=True)    
    command = "rm -f "+input.split(sep=".")[0]+".sorted_seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".sorted_seq_id"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".sorted_qual"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".sorted_qual_id"
    subprocess.check_call(command, shell=True)

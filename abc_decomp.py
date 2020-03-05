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
    
    input = args.i
    threads = args.t
    
    hash = random.getrandbits(128)
    output = args.i + str(hash) 

    command = "zpaq -t" + threads + " -f x " + input
    subprocess.check_call(command, shell=True) 
    
    command = "paste -d ' ' " + input.split(sep=".")[0] + ".sorted_seq_id " + input.split(sep=".")[0] + ".sorted_seq | sort -V > " + output + ".sort_seq"
    subprocess.check_call(command, shell=True)     
    command = "paste -d ' ' " + input.split(sep=".")[0] + ".sorted_qual_id " + input.split(sep=".")[0] + ".sorted_qual | sort -V | cut -f 2 -d ' ' > " + output + ".qual"
    subprocess.check_call(command, shell=True)      

    command = "rm -f " + input.split(sep=".")[0]+".sorted_seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + input.split(sep=".")[0]+".sorted_seq_id"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + input.split(sep=".")[0]+".sorted_qual"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + input.split(sep=".")[0]+".sorted_qual_id"
    subprocess.check_call(command, shell=True)
    
    command = "cut -f 2 -d ' ' " + output + ".sort_seq > " + output + ".seq"
    subprocess.check_call(command, shell=True)
    command = "cut -f 1 -d ' ' " + output + ".sort_seq > " + output + ".id_front" 
    subprocess.check_call(command, shell=True)

    command = "rm -f " + output + ".sort_seq"
    subprocess.check_call(command, shell=True)
    
    command = "paste " + output + ".id_front " + input.split(sep=".")[0] + ".id_back > " + output + ".id"
    subprocess.check_call(command, shell=True)  
 
    command = "rm -f " + output + ".id_front"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".id_back"
    subprocess.check_call(command, shell=True)   
    
    command = "paste -d '\n' " + output + ".id " + output + ".seq " + input.split(sep=".")[0] + ".third_line " + output + ".qual > " + input.split(sep=".")[0] + ".abc_decomp"
    subprocess.check_call(command, shell=True)  
       
    command = "rm -f " + output + ".id"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + ".seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + input.split(sep=".")[0] + ".third_line"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + ".qual"
    subprocess.check_call(command, shell=True)
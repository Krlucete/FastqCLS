import subprocess
import shlex
import argparse
import glob
import random
import timeit

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
    
    start_scoring_time = timeit.default_timer()
    command = "split -n r/4 " + input + " " + output + "/" 
    subprocess.check_call(command, shell=True)
    end_scoring_time = timeit.default_timer()
    print("%f : split time" % (end_scoring_time-start_scoring_time))  
    
    command = "cut -f 1 -d ' ' " + output + "/aa > " + output +"/id_front"
    subprocess.check_call(command, shell=True)
    command = "cut -f 2 -d ' ' " + output + "/aa > " + input.split(sep=".")[0] +".id_back" 
    subprocess.check_call(command, shell=True)

    command = "rm -f " + output + ".aa"
    subprocess.check_call(command, shell=True)
    
    start_scoring_time = timeit.default_timer()
    command = "pypy scoring_seq_dict.py -i " + output + "/ab < "+ output + "/ab > " + output + "/score_seq -sT 1"
    subprocess.check_call(command, shell=True)
    end_scoring_time = timeit.default_timer()
    print("%f : scoring time" % (end_scoring_time-start_scoring_time))
    
    start_scoring_time = timeit.default_timer()
    command = "paste -d' ' " + output + "/ab " + output +"/id_front " + output + "/score_seq | sort -k3 -k1 --parallel=" +threads+" > " + output + "/sort_seq"
    subprocess.check_call(command, shell=True)
    end_scoring_time = timeit.default_timer()
    print("%f : paste_and_sorting time" % (end_scoring_time-start_scoring_time))
    
    command = "rm -f " + output + "/ab"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/score_seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f " + output + "/id_front"
    subprocess.check_call(command, shell=True)  

    command = "cut -f1 -d' ' " + output + "/sort_seq > " + input.split(sep=".")[0] + ".sorted_seq"
    subprocess.check_call(command, shell=True)   
    command = "cut -f2 -d' ' " + output + "/sort_seq > " + input.split(sep=".")[0] + ".sorted_seq_id" 
    subprocess.check_call(command, shell=True) 
    
    command = "mv " + output + "/ac "+ input.split(sep=".")[0] +".third_line" 
    subprocess.check_call(command, shell=True)   
    command = "rm -f " + output+"/ac "
    subprocess.check_call(command, shell=True)   
    
    command = "mv " + output + "/ad "+ input.split(sep=".")[0] +".quality" 
    subprocess.check_call(command, shell=True)   
    command = "rm -f " + output+"/ad "
    subprocess.check_call(command, shell=True)  
    
    command = "rm -rf " + output
    subprocess.check_call(command, shell=True)
    
    command = "rm -f " + input.split(sep=".")[0] + ".cle"
    subprocess.check_call(command, shell=True)
    
    start_scoring_time = timeit.default_timer()
    command = "zpaq -method 5 a " + input.split(sep=".")[0] +".cle "+ input.split(sep=".")[0] + ".sorted_seq " + input.split(sep=".")[0]+".sorted_seq_id "+input.split(sep=".")[0]+".id_back "+input.split(sep=".")[0]+".third_line "+input.split(sep=".")[0]+".quality -threads " + threads
    subprocess.check_call(command, shell=True)
    end_scoring_time = timeit.default_timer()
    print("%f : zpaq time" % (end_scoring_time-start_scoring_time))
    
    command = "rm -f "+input.split(sep=".")[0]+".quality"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".third_line"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".id_back"
    subprocess.check_call(command, shell=True)    
    command = "rm -f "+input.split(sep=".")[0]+".sorted_seq"
    subprocess.check_call(command, shell=True)
    command = "rm -f "+input.split(sep=".")[0]+".sorted_seq_id"
    subprocess.check_call(command, shell=True)

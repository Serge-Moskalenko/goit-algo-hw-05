import sys
from pathlib import Path
import re
from collections import defaultdict

def main():
    try:
        if len(sys.argv)<2:
            user_input=""
        if len(sys.argv)<3:
            user_input=sys.argv[1]
        else:  
            user_input=sys.argv[1]  
            log_file=sys.argv[2]

        path=Path(user_input)

        if log_file:
            extended_log(path,log_file)
        else:
            count_log(path)

    except:"not found" 

def count_log(path):
        logs = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
        counts = defaultdict(int)
        
        with open(path, 'r',encoding="utf-8") as file:
            for item in file:
                for log in logs:
                    if log in item:
                        counts[log] += 1
                        break
        
        for log in logs:
            print(f"{log}:{counts[log]}")
        
def extended_log(path,log_file:str):
    count_log(path)
    lines=[]

    with open(path, 'r',encoding="utf-8") as file:
        for item in file:
            if re.search(log_file, item, re.IGNORECASE):
                lines.append(item)
    
    print(f"Деталі логів для рівня {log_file.upper()}:")
    for line in lines:
        print(line)
        
if __name__ == "__main__":
    main()

# python task_3.py ./log_data.txt error




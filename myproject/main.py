from src import add
from src import Agent
from src import SYSTEM_PROMPT

import os
import time

from dotenv import load_dotenv
load_dotenv()

def main():
    print("Hello from myproject")
    
    start=time.perf_counter()
    agent=Agent("professional")
    print(agent.name)
    
    number_1=10
    number_2=12
    
    result=add(number_1,number_2)
    print(f" {number_1} {number_2}= {result}")
    
    print(f" System prompt is: {SYSTEM_PROMPT}")
    
    password=os.getenv("password")
    print(f"{password[0:2]}***")
    elapsed=time.perf_counter()-start
    
    print(f"time taken {elapsed}")
    
if __name__ =="__main__":
    main()
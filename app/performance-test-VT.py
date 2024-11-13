import sys
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
import time 

def send_request(url, data):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        return f"Error: {e.reason}"

def main():

    # Check if any arguments were provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <arg1> <arg2> ...")
        sys.exit(1)

    # Print the script name (first argument)
    print(f"Script name: {sys.argv[0]}")

    # Print all the arguments
    print("Arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")

    # Access the arguments
    ins_type = sys.argv[1]
    num_of_jobs = int(sys.argv[2])

    url_sd_trn = 'http://vittrn-1991450041.us-west-2.elb.amazonaws.com/imgcls'
    url_sd_inf = 'http://vitinf-1082920408.us-west-2.elb.amazonaws.com/imgcls'
    url_sd_c8g = 'http://vitc8g-1573098688.us-west-2.elb.amazonaws.com/imgcls'
    url_sd_g6  = 'http://vitg6-29816370.us-west-2.elb.amazonaws.com/imgcls'

    if ins_type == 'trn':
        url = url_sd_trn
    elif ins_type == 'inf':
        url = url_sd_inf
    elif ins_type == 'c8g':
        url = url_sd_c8g
    else:   
        url = url_sd_g6

    data = {
        "prompt": "http://images.cocodataset.org/val2017/000000039769.jpg"
    }
    
    num_requests = num_of_jobs  # Number of parallel requests to make

    print(f"Invoking this {url} for number of parallel jobs {num_of_jobs}") 
    
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request, url, data) for _ in range(num_requests)]
        
        for future in as_completed(futures):
            result = future.result()
            print(result)
            print('\n *********** \n')
            time.sleep(2)
            

if __name__ == '__main__':
    main()
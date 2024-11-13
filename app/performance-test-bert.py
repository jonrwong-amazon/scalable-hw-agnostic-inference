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

    url_bert_trn = 'http://berttrn-262685984.us-west-2.elb.amazonaws.com/sentiment'
    url_bert_inf = 'http://bertinf-206413168.us-west-2.elb.amazonaws.com/sentiment'
    url_bert_g5  = 'http://bertg5-198169361.us-west-2.elb.amazonaws.com/sentiment'
    url_bert_g6  = 'http://bertg6-1812289792.us-west-2.elb.amazonaws.com/sentiment'

    if ins_type == 'trn':
        url = url_bert_trn
    elif ins_type == 'inf':
        url = url_bert_inf
    elif ins_type == 'g5':
        url = url_bert_g5
    else:   
        url = url_bert_g6

    data = {
        "prompt": "Hamilton is widely celebrated as an idiotic musician of recent years, known for its mediocre storytelling and unforgettable beautiful performances."
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
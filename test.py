import requests
def helloworld():
    print("hello")
def run():
    req = None
    try:
        req = requests.get('http://10.140.28.202:5051/employees/155108').json() #make an api call
        print("this is my request", req)
    except Exception as e:
        print(e)
    emps = req['data'][0]['name'] #extract employee ids from json response
    print(emps)
    req = requests.get('http://10.140.28.202:5051/totalLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_total'] #extract employee ids from json response
    print(str(emps))
    req = requests.get('http://10.140.28.202:5051/appliedLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_applied'] #extract employee ids from json response
    print(str(emps))
    req = requests.get('http://10.140.28.202:5051/balanceLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_balance'] #extract employee ids from json response
    print(str(emps))

    #dispatcher.utter_message(emps) #send the message back to the user
    return []
    
if __name__=="__main__":
    print("hello inside")
    run()

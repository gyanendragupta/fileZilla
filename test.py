import requests
def helloworld():
    print("hello")
def run():
    req = None
    try:
        req = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
        print("this is my request", req)
    except Exception as e:
        print(e)
    joke = req['value']['joke'] #extract employee ids from json response
    print(joke)
    print(str(joke))

    #dispatcher.utter_message(emps) #send the message back to the user
    return []
    
if __name__=="__main__":
    print("hello inside")
    run()

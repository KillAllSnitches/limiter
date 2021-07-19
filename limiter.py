import requests, os, time
from colorama import Fore, init, Style
init(convert=True)
Red = Fore.RED
Green = Fore.GREEN
Blue = Fore.BLUE
Cyan = Fore.LIGHTBLUE_EX
Purple = Fore.MAGENTA
Orange = Fore.YELLOW
Reset = Style.RESET_ALL


def logo():
    os.system('cls')
    print(Orange, """      ..    .                           .         s                            
x .d88"    @88>                        @88>      :8                            
 5888R     %8P      ..    .     :      %8P      .88                  .u    .   
 '888R      .     .888: x888  x888.     .      :888ooo      .u     .d88B :@8c  
  888R    .@88u  ~`8888~'888X`?888f`  .@88u  -*8888888   ud8888.  ="8888f8888r 
  888R   ''888E`   X888  888X '888>  ''888E`   8888    :888'8888.   4888>'88"  
  888R     888E    X888  888X '888>    888E    8888    d888 '88%"   4888> '    
  888R     888E    X888  888X '888>    888E    8888    8888.+"      4888>      
  888R     888E    X888  888X '888>    888E   .8888Lu= 8888L       .d888L .+   
 .888B .   888&   "*88%""*88" '888!`   888&   ^%888*   '8888c. .+  ^"8888*"    
 ^*888%    R888"    `~    "    `"`     R888"    'Y"     "88888%       "Y"      
   "%       ""                          ""                "YP'                 
                                                                               
                                Coded by: vx#1234                                                  
                                                                               """, Reset)
    limiter()

def limiter():
    url = "urlhere"

    req = {"query":"req data here"}

    headers = {
    'x-rapidapi-key': "key",
    'x-rapidapi-host': "host"
    }

    response = requests.request("GET", url, headers=headers, params=req)
    if response.text == "success text here":
        print(Green, "Request Sent!")
        time.sleep(1.3)
        limiter()
    elif response.text == "rate limit text":
        print(Orange, "Rate Limited!")
        time.sleep(1.3)
        limiter()
    else:
        print(Red, "WE GOT EM BOIZ")
        print(response.text)
logo()

# {"message":"You have exceeded the DAILY quota for Requests on your current plan, BASIC. Upgrade your plan at https:\/\/rapidapi.com\/softrix-technologies-dnschecker\/api\/mac-address-lookup1"}

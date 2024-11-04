
from modules.manager import UrlManager


if __name__ == "__main__":

    print("Welcome to url shortner app")
    urlManager = UrlManager()
    while True:

        print('''To encode Urls - 1 \n 
                 Access Urls - 2 ''')

        try: 
            i = int(input("Enter number - "))
            if i == 1:
                url = input("enter your url")
                encodedUrl = urlManager.encode_url(url)

                print(encodedUrl)

            elif i == 2:
                url = input("enter encoded url")
                urlManager.access_url(url)
        except ValueError:
            print("Please enter a valid input ")





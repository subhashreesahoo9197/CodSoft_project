import requests  
import sys  
  
#A sample python code to shorten a URL with the use of cutt.ly APIs with different options.  
class URLHandler:  
  
    #constructor to initialize the class variables that will be used for the initializing the class variables of the above-written class  
    def __init__(self):  
        self.api_key = None  
        self.shortened_url = None  
        self.exception_encountered  = None  
  
# A sample function that will be sued to Set the  API value  which we will use to shorten the input URL that will be provided by the user  
    def set_api_url(self):  
        print("enter the api key of the service account::")  
        input_api_key = input()  
        self.api_url = input_api_key  
  
#  this function is a written explicitly  to take an input URL from the user that will be used to short  
    def get_input_url(self):  
        print("Enter the URL that you want to shorten.")  
        url_to_shorten = input()  
        return url_to_shorten  
  
#  this function is written to perform the shorter operation on the input URL there is one parameter that is specified for this particular function and this parameter is the URL  parameter that is representing the input URL provided by the user.  try-catch block is implemented in this function so that if some exception is encountered while shortening the input URL which is provided by the user that  exception is handled  and the value of the shortened URL variable is set to none which represents that there is some error exception which is encountered while performing the shortening operation of the specified URL,  and if the operation is successful and no error exception is encountering while shortening the input URL provided by the user the shorten URL variable is set with the actual shorten URL which is returned by the API call that we have given in this function If the exception or errors encountered while shortening the input URL there are a couple of steps that are performed first of all the shortened URL variable is set to none representing there is an exception and along with that the message associated with the exception or error which is encounter is also printed to the user representing the root cause of the exception that is encounter   
    def shorten_url(self,url):  
        api_url = f"https://cutt.ly/api/api.php?key={self.api_key}&short={url}"  
        request_return_obj = requests.get(self.api_url).json()["url"]  
          
        try:  
            if request_return_obj["status"] == 7:  
                self.shortened_url = request_return_obj["shortLink"]  
            else:  
                self.shortened_url = None      
        except Exception as e:  
            self.exception_encountered  = e  
              
          
  
  
# This function is written to print the result of the above Return function,  the printing of the shortened URL is done with the logic,  we have an if else block checking whether the shortening of URL operation is performed successfully or not,  for that, we are checking the value of the shortened URL variable if the value is not set to null then that means the operation is performed successfully and that particular URL is printed which is shortened on the other hand if the value is set to none that means there is some exception which is encountered during the shortening operation so in that case the associated exception or error message which is encountered during that operation is presented to the user   
    def print_shortened_url(self):  
  
        if self.shortened_url:  
            print("Shortened URL: {}".format(self.shortened_url))  
        else :  
            print("URL shortening got an exception {}.".format(self.exception_encountered))  
  
  
  
# And this is the main function in this function the object of the above-written class is created and that object is used to call all the above-written functions inside that class,  the user is given multiple options like to enter the API key of the service account,  to enter the URL which the user wants to shorten,  to perform the actual shortening operation of the specified input URL,   once the sorting operation is performed successfully the user can print the URL which is shortened,  and in the last option user can accept the code execution by opting the last and final option,  appropriate input is taken from the user and appropriate output is given according to the option which is selected by the user to perform the operation.  
def main():  
      
    shortner =  URLHandler()  
    url = None  
    while(True):  
        print("Please choose any one of the operations from the listed below the list of operations::")  
        print("1. To enter the API key for the service account.")  
        print("2. To enter the URL which you want to shorten.")  
        print("3. To perform the operation of shortening the URL.")  
        print("4. To print the URL which is shortened.")  
        print("5. To exit from the code execution.")  
          
        menu_choice = input()  
        menu_choice = int(menu_choice)  
  
        if menu_choice == 1:  
            shortner.set_api_url()  
        elif menu_choice == 2:  
            url = shortner.get_input_url()  
        elif menu_choice == 3:  
            # shortner.shorten_url(url)  
            print("URL shortned successfully.")  
        elif menu_choice == 4:  
            shortner.print_shortened_url()  
        elif menu_choice == 5:  
            sys.exit()  
          
        print("To keep on going with code execution, type [y] otherwise [n].")  
        continue_or_exit = input()  
  
        if continue_or_exit == 'y' or continue_or_exit == 'Y':  
            pass  
        elif continue_or_exit == 'n' or continue_or_exit == 'N':  
            sys.exit()  
  
if __name__ == '__main__':  
    main()  
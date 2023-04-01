# Get_Best_Price

Hi! Do you wanna purchase your favourite item from popular e-commerce website like Flipkart, but still waiting for best price? Getting tired of opening and monitoring prices manually? Here comes **Get_Best_Price** to your rescue by automating this boring process of manually opening and checking prices. This application will not only monitor and plot beautiful price plots but also will take threshold value from you and will send you an email notification whenever prices falls below that threshold value. It can even be deployed on cloud platforms. Crazy? Let's get started

# Installation

You will require Python3 for building this source code on you local machine. You can download the source code and install the dependencies given in **requirement.txt** . You may use pip to install this dependencies. **Recommended operating system**:It works fine on Linux Operating system. It also works in windows. In case GUI is not properly rendered in windows then comment line 32 and 33 and uncomment line 34 in interface.py and you are good to go!

# One time configuration

Run the interface.py file, which renders pyQt5 based GUI. Welcome screen will pop up.

On clicking this button, we get on to next frame where we need to fill some details. Firstly we need to provide the user agent of our system which can be found by simply googling it :)

Next we need to add the Fli\*pk@rt URL of our favourite product

Copy URL and paste it and click submit

Next you need to inspect element to get the class name corresponding to product name (It is generally "B_NuCI", but it may change if there are some changes made to the site)

Paste it and click submit 

Similarly inspect class corresponding to price and paste it (generally it is "\_30jeq3 \_16Jk6d") :

Click Submit 

After that paste your gmail id and click submit

Now go to your google account and turn on the 2 step verification. Read more <a href ="https://www.google.com/landing/2step/">here</a>.

Now set up 16 digit app password for your gmail . Read more <a href="https://support.google.com/mail/answer/185833?hl=en#:~:text=An%20App%20Password%20is%20a,2%2DStep%20Verification%20turned%20on.">here</a>

Now enter your 16 digit gmail app password, which will be used to send you self mail notification regarding price drop. **NOTE : We don't collect or use your any credential and we may not be responsible for any loss/leak of credentials.**

Now your product name and its current price will be visible. You need to enter a threshold for price.

On clicking set threshold, you will be navigated to home page. Now whenever you will open the application, you will be viewing this screen only:

Also whenever you start your PC you need to run this application and then only it will track price every two hours. It can also be deployed on cloud platforms.

Now whenever price falls below threshold value you will receive email notification and threshold will get updated to that lower value. Wanna see the price trend? Click on "Monitor Price" button and it will open beautiful price plot on your default browser:

You will receive such type of email notification when price drops:

## Checking prices for more than one products?

Extract and build this code at different location and you are good to go! configure it for another product in the same way as done before.

## Errors? Crashes?

Filling wrong information can cause program to crash. In such cases, delete the folder where you have kept this source code and then download and copy the fresh code and configure again.

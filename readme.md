# Raspberry Pi Reminder (Pi Zero W and Blinkt Version)

I often get distracted by what I'm working on, and miss reminders from Google Calendar. To help me avoid missing meetings, I created the Pi Reminder project, a visual notifier that uses the Raspberry Pi, the Pimoroni Unicorn HAT and the Google Calendar API. I wrote about the project on [johnwargo.com](http://johnwargo.com/microcontrollers-single-board-computers/raspberry-pi-reminder-project.html) and the folks at Make Magazine published a version of the article as [*Get a Flashing Meeting Reminder with a Raspberry Pi*](http://makezine.com/projects/get-a-flashing-meeting-reminder-with-a-raspberry-pi/). The project's been sitting on my desk for months, quietly reminding me of my appointments throughout the day.

With the announcement of the [Raspberry Pi Zero W](https://www.raspberrypi.org/blog/raspberry-pi-zero-w-joins-family/), I knew I had an opportunity to create a much smaller version of the Pi Reminder project. I used a Raspberry Pi 3 for the original project because I wanted a bright display and needed an Internet connection. But with the Pi Zero W, I had everything I needed. Immediately after the announcement, I poked around on the Internet looking for a way to buy one. Adafruit, and the other US distributors wouldn't have any for quite a while (it took me 5 months to get a Pi Zero in the US after it launched), so I looked in the UK and found the Pimoroni [Pi Zero W Starter Kit](https://shop.pimoroni.com/products/pi-zero-w-starter-kit) which seemed just right for this project. The kit includes the Pi, a case and the Blinkt LED board. 

The Repository contains the project code for the Pi Zero W/Blinkt version of the Pi Reminder project.


[Assembly](https://learn.pimoroni.com/tutorial/sandyj/pibow-zero-assembly)

[https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt)


	curl -sS get.pimoroni.com/blinkt | bash

Now, install the [Google Calendar API Python files](https://developers.google.com/api-client-library/python/start/installation) along with some other libraries using the following command:

    sudo pip install --upgrade google-api-python-client python-dateutil pytz httplib2 oauth2client

this.

	python ./remind.py


Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-01.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-02.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-03.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-04.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-05.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

![SOME DESCRIPTION](screenshots/figure-06.png)

Shankle ground round shank strip steak spare ribs pork short loin capicola. Ham hock porchetta tenderloin, turducken meatball brisket chicken beef alcatra. Tenderloin cow fatback t-bone, shankle pork chop prosciutto chicken jowl spare ribs bacon. Turducken shankle chicken pig, rump doner pork loin cow porchetta ham strip steak.

## Update History

Nothing yet.

***
By [John M. Wargo](http://www.johnwargo.com) - If you find this code useful, and feel like thanking me for providing it, please consider making a purchase from [my Amazon Wish List](https://amzn.com/w/1WI6AAUKPT5P9). You can find information on many different topics on my [personal blog](http://www.johnwargo.com). Learn about all of my publications at [John Wargo Books](http://www.johnwargobooks.com). 
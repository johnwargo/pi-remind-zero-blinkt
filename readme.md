# Raspberry Pi Reminder (Pi Zero W and Blinkt Version)

I often get distracted by what I'm working on, and miss reminders from Google Calendar on my desktop or laptop PCs. To help me avoid missing meetings, I created the Pi Reminder project, a visual notifier that uses the Raspberry Pi, the Pimoroni Unicorn HAT and the Google Calendar API. The folks at Make Magazine published the original version of the article as [*Get a Flashing Meeting Reminder with a Raspberry Pi*](http://makezine.com/projects/get-a-flashing-meeting-reminder-with-a-raspberry-pi/), and I later published an article about the project on [johnwargo.com](http://johnwargo.com/microcontrollers-single-board-computers/raspberry-pi-reminder-project.html). The completed project's been sitting on my desk for months, quietly reminding me of my Google Calendar appointments throughout the day.

With the announcement of the [Raspberry Pi Zero W](https://www.raspberrypi.org/blog/raspberry-pi-zero-w-joins-family/), I knew I had an opportunity to create a much smaller version of the Pi Reminder project. I used a Raspberry Pi 3 for the original project because I wanted a bright display and needed an Internet connection. But with the Pi Zero W, I had everything I needed. Immediately after the announcement, I poked around on the Internet looking for a way to buy one. Adafruit, and the other US distributors wouldn't have any for quite a while (it took me 5 months to get a Pi Zero in the US after it launched), so I looked in the UK and found the Pimoroni [Pi Zero W Starter Kit](https://shop.pimoroni.com/products/pi-zero-w-starter-kit) which seemed just right for this project. The kit includes the Pi, a case and the Blinkt LED board. 

The Repository contains the project code for the Pi Zero W/Blinkt version of the Pi Reminder project.

## Alerts

The Pi will connect to Google Calendar and check every minute for upcoming appointments then flash the LEDs for following alerts:

+	White @ 10 minutes until 5 minutes
+	Yellow @ 5 minutes until 2 minutes
+	Multi-color swirl @ 2 minutes

## Indicator LED

The app uses a single indicator LED to let you know the app is working. It will illuminate a single LED along the row of LEDs and move the LED across the display every time it connects to Google to obtain calendar information. The color of the LED indicates status of the app as well:

+	Blue - The app is connecting to the Google Calendar API
+	Green - The app received data from the Google Calendar API, but there are no pending appointments within the next 10 minutes
+	Red - The app encountered an error connecting to the Google Calendar API
+	White - There is an appointment beginning within 10 minutes
+	Yellow - There is an appointment beginning within the next 5 minutes
+	Orange - There is an appointment beginning within the next 2 minutes

This way, even if you miss the flashing lights, you can glance at the display and still determine how far away your next appointment is.

## Hardware Components

For this project, I used the [Pi Zero W Starter Kit](https://shop.pimoroni.com/products/pi-zero-w-starter-kit). From the Pimoroni web site, here's the list of the kit's components:

+	Pi Zero W
+	Blinkt! multicolor LED strip
+	Pibow case
+	8GB micro-SD card with operating system pre-loaded
+	Male 2x20 pin header
+	USB A to micro-B cable
+	USB A (female) to micro B (male) adapter
+	mini to full-size HDMI adapter
+	Sticker sheet (personalize your Pibow!)
+	Reusable kit box

You'll also need a 5V power supply, I used the [CanaKit 5V 2.5A Raspberry Pi 3 Power Supply / Adapter / Charger (UL Listed)](http://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4) from Amazon.

## configuring the Raspberry Pi

### Hardware Setup

To setup the hardware, complete the following steps:

1. Assemble the Pibow case using the [setup instructions](https://learn.pimoroni.com/tutorial/sandyj/pibow-zero-assembly) 
2. Attach the Blinkt! board to the Raspberry Pi
3. Power it up!

That's it, you're done. That was easy, right?

### Software

Download the latest version of the Raspbian OS from the [Raspberry Pi web site](https://www.raspberrypi.org/downloads/raspbian/) and follow the [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) for writing the OS image to a Micro SD card for the Pi. Insert the **SD card** in the Pi, connect **Ethernet**, **keyboard**, **mouse**, and a **monitor** to the Pi using the cables that come with the starter kit, and, finally, **power it up** using a smartphone charger or some suitable power source.

Connect the Pi to your Wireless network (the Pi Zero doesn't support a wired network connection, so you'll have to use Wi-Fi) using [these instructions](https://www.raspberrypi.org/documentation/configuration/wireless/).

When the Pi is connected to the network all ready to go, open a terminal window and update the device's software using the following commands:

	sudo apt-get update
	sudo apt-get upgrade

The first command updates the local software repositories and the second command updates the Pi OS and associated files. There’s a set of scientific libraries that are used in some of the Unicorn HAT code in the project, so you will need to install them using the following command:


**STOPPED HERE!!!**



Finally, copy the project's Python source code to the new folder and extract the files using the following commands:

	wget https://github.com/johnwargo/pi_remind/archive/master.zip
	unzip -j master.zip

If all goes well, you should see the following files in the folder:

+	`LICENSE`
+	`readme.md` (this file)
+	`remind.py`
+	`start-remind.sh`


### Google Calendar API Setup

Before you can use the project's software, you have to setup an account with Google so the app can consume the Google Calendar APIs used in this project. To setup your account, read the [Google Calendar API Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python).

Download your Google Calendar API application's `client_secret.json` file to the project folder. Be sure to name the downloaded file using that file name. You'll need it to authorize the app to access your Google Calendar and that file name is hard coded into the Python app.

### Google Calendar API Installation

Now, install the [Google Calendar API Python files](https://developers.google.com/api-client-library/python/start/installation) along with date handling libraries using the following command:

    sudo pip install --upgrade google-api-python-client python-dateutil pytz httplib2 oauth2client

## Running the Reminder Application

With everything in place, execute the reminder app using the following command:

    sudo python ./remind.py

Before the app can access the calendar, you'll need to authorize the app to use the Google Calendar API for your calendar account. When you launch the app for the first time (using the command shown above) the browser will launch and walk you through the process. With that complete, PI Remind should start watching your calendar for events.

Note: if you ever change Google calendars (from a work to a personal calendar or from one work calendar profile to another) you'll need to whack the existing access token created during the initial startup or the Pi Reminder app. Instructions for deleting this token are available on [johnwargo.com](http://www.johnwargo.com/index.php/microcontrollers-single-board-computers/pi-reminder-%E2%80%93-delete-google-calendar-access-authorization-token.html).

Starting The Project's Application's Automatically
--------------------------------------------------

There are a few steps you must complete to configure the Raspberry Pi so it executes the the remind app on startup. You can read more about this here: [Autostart Python App on Raspberry Pi in a Terminal Window](http://johnwargo.com/index.php/microcontrollers-single-board-computers/autostart-python-app-on-raspberry-pi-in-a-terminal-window.html).

***Note:** Don't forget to authorize the Google Calendar API to access your Google Calendar by running the manual startup process described in the previous session before enabling autostart.* 

If you don't already have a terminal window open, open one then navigate to the folder where you extracted the project files. Make the project's bash script files executable by executing the following command:

    chmod +x start-remind.sh
    
Next, you'll need to open the pi user's session autostart file using the following command:  

	sudo nano ~/.config/lxsession/LXDE-pi/autostart    

Add the following lines to the end (bottom) of the file:

	@lxterminal -e /home/pi/pi_remind/start-remind.sh

To save your changes, press `ctrl-o` then press the Enter key. Next, press `ctrl-x` to exit the `nano` application.
  
Reboot the Raspberry Pi; when it restarts, the python remind process should execute in its own terminal window.

Another option is to copy the `start-remind.desktop` file to `~/.config/autostart`. Reboot the Pi and you should see a terminal window running the Reminder app.






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
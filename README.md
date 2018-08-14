Dependencies: python 2.7, kivy

Files: wtv.py, wtv.kv

Purpose:

I made this script after FB decided to cenor a webaddress that I had posted. So in response wtv(What the Vet) was born. I used kivy for the gui because I am planning to make the script into an android app so that android users can make use of it as well. Basically it will take any string of text webaddress or simple message and obfuscate it by spelling out the entire string using the Military phonetic alphabet. 

I use a simple python dictionary to achive this certain characters such as spaces, punctuation marks, etc are spelled out with dashes between the phonetic letters. For instance if there is as space between the words of a string space will be spelled out like so sierra-papa-alpha-charlie-echo. I haven't yet put all the punctuation marks or other special characters in the dictionary yet but enoungh are there to do the job.

How to install and use: 

Just download or clone this repository to your computer and open a terminal window in the folder you put it in. Type python wtv.py, a new window will open and you will be greeted with the baic gui for What the Vet. A text area and two buttons labeled Do It and Undo It.

To obfuscate a webaddress simply paste the address string into the text area and click Do It. The script will take care of the rest, you will see the phoneticaly spelled webaddress in the text area and a message will show that it has already been copied to the clipboard. All you have to do is paste it to FB or whereever you want to paste it to. Click the Undo It button and the script will convert it back to regular text.

To do:

Make it look pretty. Right now the gui is very basic I plan to make it visually more appealing later on but right at the moment I am going for function over asthetics.

Create standalone binaries. I want to make the script into a standalone binary for all the platforms Linux, Windows, Mac, Android, Ios, etc so that users don't have to install python. But that is proving to be harder than anticipated so far I haven't had much success in this regard yet.

Add all the Ascii characters.



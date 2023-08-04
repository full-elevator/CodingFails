# Updating Python

Recently (July 31st) I updated to Python 3.11 with the installer `python-3.11.0-amd64.exe` downloaded from python.org, following the tutorials on the official site. I had no experience of updating Python before, so I ended up running into a bunch of issues and had to spend a few days dealing with them.

## Setup

 - OS: Windows 10, 64-bit system
 - Old version: 3.10 
 - New version: 3.11, both installed with the web installer from python.org

I have heard that multiple Python versions may cause conflicts, so I uninstalled Python 3.10 first. Then I ran the 3.11 installer, and it finished successfully in about a minute. Hoping to save time, I copied the site-packages folder from 3.10 into the 3.11 directory. This proved a mistake.

## The issues

1. Immediately after the update, a few libraries ceased to work. Matplotlib and NumPy were broken, the latter of which threw an `ImportError`. 

```IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE! Importing the numpy c-extensions failed... (33 more lines)```

2. Pydub could still load and save files, but whenever I used `play(AudioSegment)`, it threw an error:

```PermissionError: [Errno 13] Permission denied: 'C:\\Users\\third\\AppData\\Local\\Temp\\tmpiqsyuk1j.wav'``` (`third` is my username)

3. When I try to re-install NumPy with pip, I found out that pip was broken as well. It printed the following error message:

```Unable to create process using 'C:\Users\third\AppData\Local\Programs\Python\Python311\Scripts\pip uninstall numpy': ??????????```

I retried in Powershell to fix the potential encoding issue, but the error message was still question marks, so I don't know what it's supposed to say.

4. I tried to re-install pip, but the cmd command printed 

```'python' is not recognized as an internal or external command, operable program or batch file.```

5. I knew that the last issue is because `python.exe` is not added to `PATH`, so I opened the "Edit Environment Variables" window. Strangely, my changes to `PATH` do not save; they are automatically reverted after I click "Apply". Restarting did not work either. 

## The solutions

5. See [Superuser](https://superuser.com/questions/1107605/windows-10-system-environment-variables-dont-stick). I switched to `regedit` to edit the values of `PATH`, then the changes got saved normally. I added both ...\Python311 and ...\Python311\Scripts to `PATH`.

Side note: I also get this error when testing in the python shell. Later, I found out that the new python executables are not run with administrator privileges. To fix this, I set "Always run with administrator privileges" for all users for both `python.exe` and `pythonw.exe`.

4. Then, the unable to create process error appeared again.

```Unable to create process using 'C:\Users\third\AppData\Local\Programs\Python\Python311\python: ??????????```

I tried to reinstall pip with `get-pip.py` from `https://bootstrap.pypa.io/get-pip.py`. Strange things happened: the command line ran, but gave no output, neither the downloading progress bar nor an error. After searching around, I finally realized that the command line was executed, though the results were not printed to shell. I resorted to checking the newly installed packages manually. 

Later, I found out that the results can be saved by writing to a file. For example, `pip list > D:\list.txt` prints the list of installed modules to D:\list.txt.

3. I uninstalled and reinstalled NumPy and the `ImportError` disappeared. Same with Matplotlib.

2. I tried to reinstall Pydub, but it still threw the `PermissionError`. At this point I was running everything with administrator privileges. From what I have read, this usually occurs when the given path is a directory; however, it is clear from the error message (see above) that the path points to a file. 

There are a few `tempfile` related changes in the [3.11 changelog](https://docs.python.org/3/whatsnew/changelog.html), but none of them seem relevant. I'll add something here if I fix that as well.

## Ending

Conclusion: probably it's better to use a virtual environment or a trusted environment management tool. I might be switching to `conda` when I have the determination to tackle one more "issue-chain" like this.

Useful resources:
 - [The official installation tutorial with troubleshooting tips](https://docs.python.org/3/using/index.html).

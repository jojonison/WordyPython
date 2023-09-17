How to set-up omniORB python 

1. Download omniORBpy4.3.0 from https://sourceforge.net/projects/omniorb/files/omniORBpy/omniORBpy-4.3.0/

2. Extract the files and put it in a directory that you prefer (e.g C:\)

3. Download pyCharm

4. Since omniORBpy 4.3.0 supports python 3.10.x, download python3.10 (In my case, I downloaded python 3.10 from pycharm. You can also download
any python 3.10 in python.org)

5. Under system variables edit the PATH variable and add the path directory of the omniidl executable
 (omniidl.exe).
Usually, the omniidl executable is found in the bin directory (C:\omniORBpy4.3.0\bin\x86_win32\) 

6. Add another path directory to a file called python310.dll found in the python version fold in the PATH varaible
(The file is usually found in the AppData folder [C:\Users\nseno\AppData\Local\Programs\Python\Python310])

7. After which omniidl commands are now available in the command prompt (You can test by doing command 'omniidl -h').

8. In the systems variable create a new variable named 'PYTHONPATH' and the value of the variable should be path in
the library of the omniORBpy (C:\omniORBpy-4.3.0\lib\python)

9. You can now use the modules found in omniORBpy in the pyCharm IDE

10. Go to settings and find the tab for project settings. Under project settings, press the project interpreter. After pressing,
press the plus button and search for omniorb and download the package.

11. Open cmd and type in pip install omnipy

12. Clone the project

13. Under the configuration of the main script to run the python client, type in these parameters.[-ORBInitRef NameService=corbaname::localhost:9999]

14. Your set-up is now complete!
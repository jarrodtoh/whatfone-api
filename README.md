whatfone-api
============

API of Whatfone

### Getting Started

<b>Install Python:</b><br>
1) Goto http://python.org/download/ and download the latest Python 2.7.5 (32bit) installer<br>
2) Install Python<br>
3) (Windows) Add “c:\python27” and “c:\python27\scripts” into PATH (the latter is for your python packages)
* Windows 7 and below:
 - Right-click “My Computer” and choose Properties
 - Click “Advanced System Settings and click “Environment Variables”
 - Find “PATH” and append “c:\python27; c:\python27\scripts”. (IMPORTANT: Must have semi-colon after each directory)
* Windows 8:
 - Press “Windows Key + W” and type “System”
 - Click “Advanced System Settings and click “Environment Variables”
 - Find “PATH” and append “c:\python27; c:\python27\scripts”. (IMPORTANT: Must have semi-colon after each directory)

<br>
<b>Install Python Packages:</b><br>
For <b>Windows</b>:<br>
1) Setuptools (http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)<br>
2) Pip (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)<br>
3) After installing pip, goto terminal and `$ pip install nltk`<br>
For <b>Mac</b><br>
1) Setuptools (https://pypi.python.org/pypi/setuptools)<br>
2) After installing setuptools, goto terminal and `$ sudo easy_install pip` to install Pip<br>
3) After installing pip, goto terminal and `$ sudo pip install nltk`<br>

<br>
<b>NLTK Treebank Download</b><br>
1) Goto terminal and `$ python`, it will go into python terminal mode.<br>
2) Type `$ import nltk`<br>
3) Type `$ nltk.download()`, and a new window will appear.<br>
4) Go under "All Packages", and download "maxent_treebank_pos_tagger"<br>

### Corpora FAQ
All data stored in `~PROJECT_ROOT/data` folder
<table>
  <tr>
    <td>Subfolder</td>
    <td>Description</td>
    <td>Docs</td>
    <td>Tokens</td>
    <td>Status</td>
  </tr>
  <tr>
    <td>0</td>
    <td>Original copy</td>
    <td>4,999</td>
    <td>200,003</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Tag Stage 1</td>
    <td>25</td>
    <td>1057</td>
    <td>IN-PROGRESS</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Tag Stage 2</td>
    <td>27</td>
    <td>1221</td>
    <td></td>
  </tr>
</table>
Total: 4999 reviews, 200,003 tokens<br>

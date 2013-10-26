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
    <td><b>Subfolder</b></td>
    <td><b>Description</b></td>
    <td><b>Docs</b></td>
    <td><b>Tokens</b></td>
    <td><b>Status</b></td>
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
    <td>DONE</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Tag Stage 2</td>
    <td>26</td>
    <td>939</td>
    <td>DONE</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Tag Stage 3</td>
    <td>9</td>
    <td>1043</td>
    <td>DONE</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Tag Stage 4</td>
    <td>47</td>
    <td>969</td>
    <td>DONE</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Tag Stage 5</td>
    <td>29</td>
    <td>1028</td>
    <td>Trained, not corrected.</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Tag Stage 6</td>
    <td>20</td>
    <td>1009</td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Tag Stage 7</td>
    <td>28</td>
    <td>972</td>
    <td></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Tag Stage 8</td>
    <td>32</td>
    <td>1097</td>
    <td></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Tag Stage 9</td>
    <td>32</td>
    <td>1121</td>
    <td></td>
  </tr>
  <tr>
    <td>10</td>
    <td>Tag Stage 10</td>
    <td>16</td>
    <td>1517</td>
    <td></td>
  </tr>
</table>

### API Commands

* <b>Count Stats for XML (counter.py)</b><br>
`$ python counter.py <FILENAME>.xml`<br>
Example: `$ python counter.py data/0/reviews.xml`<br>
* <b>Train using Default Tagger Model (default-tag-trainer.py)</b><br>
`$ python default-tag-trainer.py data/x/<RAW>.xml data/x/trained.xml`<br>
Example: `$ python default-tag-trainer.py data/1/test1.xml data/1/trained1.xml`<br>
* <b>Train using previously trained XML</b> (trainer-tag-trainer.py)<br>
`$ python trained-tag-trainer.py <INT_NUM_OF_TRAINED_FILES> <TRAINED_FILE_X> * <TEST_FILE> <TRAINED_FILE>`<br>
Example for tagging stage 2, need to pass trained+corrected stage 1 file to train a stage 2 test file:<br>
`$ python trained-tag-trainer.py 1 corrected1.xml test2.xml trained2.xml`<br>
Example for tagging stage 4, need to pass trained+corrected stage 1,2,3 files to train a stage 4 test file:<br>
`$ python trained-tag-trainer.py 3 corrected1.xml corrected2.xml corrected3.xml test4.xml trained4.xml`<br>
* <b>Count Corrected Tags (count-corrected-tags.py)</b><br>
`$ python count-corrected-tags.py trained.xml corrected.xml`<br>
It will return <u>corrected tag count</u> and <u>error review ID(s)</u> if any. Error usually happens if the number of tags did not tally. 
* <b>Check for missing tags (check-missing-tags.py)</b><br>
`$ python check-missing-tags.py <XML_FILE>`<br>
If missing tag found, it will display on terminal. If the missing tag is non-word, it is fine. Else, go tag that word.

### POS-Tagging FAQ
Currently, we uses NLTK for POS-tagging. 
* <b>Codes covering POS-Tagging</b>:
 - Library File: `libraries\tags.py`
 - API Wrapper Files: `default-tag-trainer.py` (Default Tagging Model) and `trained-tag-trainer.py` (Custom Model via trained tags)
* <b>Handy POS Tag List</b>
 - http://www.monlp.com/2011/11/08/part-of-speech-tags/
* <b>What do we need to do?</b>
 - Tagging consists of 10 stages. For each stage, there are a series of steps to be completed. Here's the steps:
 <table>
   <tr>
      <td><b>Stage</b></td>
      <td><b>Steps</b></td>
   </tr>
   <tr>
      <td>1</td>
      <td>
        1) `$ python default-tag-trainer.py data/1/test1.xml data/1/trained1.xml`<br>
        2) Manually correct `trained1.xml` and saved as `corrected1.xml`<br>
      </td>
   </tr>
   <tr>
      <td>2</td>
      <td>
        1) `$ python trained-tag-trainer.py 1 data/1/corrected1.xml data/2/test2.xml data/2/trained2.xml`<br>
        2) Manually correct `trained2.xml` and saved as `corrected2.xml`<br>
      </td>
   </tr>
   <tr>
      <td>3</td>
      <td>
        1) `$ python trained-tag-trainer.py 2 data/1/corrected1.xml data/2/corrected2.xml data/3/test3.xml data/3/trained3.xml`<br>
        2) Manually correct `trained2.xml` and saved as `corrected2.xml`<br>
      </td>
   </tr>
   <tr>
      <td colspan="2">Blah Blah Blah...</td>
   </tr>
 </table>
* <b>What if the token is not really formal English?</b>
 - As mentioned by Prof. Kim, if it is "plz" instead of "please", tag it with the same tag. For this case, Adverb. So, `please/RB` equals `plz/RB`
 - If it is Singlish, like "lah", "leh", "lor", use Interjection (`UH`) tag. Interjection means "exclamation" word. Examples of Interjection are: "Uhhuh", "Oh", "Damn".
 - If it is email address or something non-word and non-punctuation, tag it as "Foreign Word" (`FW`).
* <b>What if there's spelling error on the word?</b>
 - Leave it as it is, tag it to the closest word you think it represents.

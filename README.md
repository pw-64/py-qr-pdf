# pyqr-pdf

Thank you to https://github.com/shivamsoods/raymond-python for which I based this off of.
I was tasked with batch creating qr codes with extra textual information, so improved upon [@shivamsoods](https://github.com/shivamsoods) fpdf implementation to do the task for me, rather than create them manually in MS Word.


## Getting Started
1. Create a virtual environment with `python3 -m venv env`
2. Activate virtenv with `source env/bin/activate` (or the script for your shell)
3. Check you are using the correct pip and python with `which pip python3`
4. Install packages `pip install fpdf qrcode`

## Usage
Adjust the variables under `# CONFIG` to get the proper layout and output format & count. s1, s2, w & h are found through trial and error, unless you already know the exact physical measurements (in millimeters).

Once configured, run `python3 main.py`
- The individual qr codes will be kept in `./qrCodes`
- The pdf will appear in the same directory the script is run in

## Note
I have substituted all of the actual info like text and the url for placeholders, since that is for you to customise and play with.

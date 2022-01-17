# Steps to activate the Script
1. Copy the following AutoHotkey (AHK) Snippet to your runninig AHK Script
```
; Pressing Alt + t to activate the HotKey
!t::
; Copying Selection
SendInput {LCtrl down}{x down}
Sleep 100
SendInput {x up}{LCtrl up}
ClipWait, 1
; Replacing all Whitespaces with § necessary, because Input String seperating at Whitespace when running script
ipt := StrReplace(Format("{1:s}", Clipboard)," ","§")
; Run the Python script
RunWait, python "C:\Users\thies\PycharmProjects\csv-clip2table\main.py" %ipt%
; Pasting Selekction
SendInput {LCtrl down}{v down}
Sleep 100
SendInput {v up}{LCtrl up}
ClipWait, 1
return
```
2. Install the required Python packages by running the following command
`
pip install -r C:\Users\thies\PycharmProjects\csv-clip2table\requirements.tx
`

# How to use the script
The selection used must have the following format (# separator):

```
Header 1 # Header 2 # Header 3
Entry 1 # Entry 2 # Entry 3 
Entry 4 # Entry 5 # Entry 6 
```

Now select all lines and press Alt + t and let the script do its magic ;) 
pip install -r requirements.txt



@echo off



set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"



echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%

echo sLinkFile = "spotify_shortcut.lnk" >> %SCRIPT%

echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = "%cd%\spotify_liker.py" >> %SCRIPT%

echo oLink.WorkingDirectory = "%cd%" >>  %SCRIPT%
echo oLink.Hotkey = "ALT+CTRL+."

echo oLink.WindowStyle = 7 >>  %SCRIPT%

echo oLink.Save >> %SCRIPT%



cscript /nologo %SCRIPT%

del %SCRIPT%




copy "spotify_shortcut.lnk" "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu"

echo "the shortcut has been moved to " "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu"

pause

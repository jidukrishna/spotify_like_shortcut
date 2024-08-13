# <img src='https://raw.githubusercontent.com/jidukrishna/spotify_like_shortcut/main/newicon.png' height=35> spotify keyboard shortcut liker <img src='https://raw.githubusercontent.com/jidukrishna/spotify_like_shortcut/main/newicon.png' height=35>



 A simple python script that likes the playing song in spotify via keyboard shortcut....


## Youtube video tutorial

 [![YouTube](http://i.ytimg.com/vi/6vB3U7__b-s/hqdefault.jpg)](https://www.youtube.com/watch?v=6vB3U7__b-s)

### Description

A spotify python script based on the spotipy module. This script checks for the current playing song in the spotify and retrieves the song uri (spotify unique song code).
This uri is checked whether it exists in liked songs and if its not there then its added . Now inorder to display this we use winotify to display the results. And this script is 
is assigned a shortcut (lnk file) where the keyboard shortcuts are assigned.

## Getting Started
<h3>Spotify setup</h3>

* if you know me personally skip this step and message me on insta... <br>
1. Create a spotify app <a href="https://developer.spotify.com/dashboard" target="_blank">Spotify Dashboard</a> <br>
2. Put the Redirect URIs as http://google.com/callback/ in the spotify app.<br>
3. Make sure to copy down the client id and client secret.<br>


### Dependencies

* Python3 (added in path)
* Pip (added in path)

  
### Cloning repo
```
git clone https://github.com/jidukrishna/spotify_like_shortcut.git
```
* If git is not downloaded then click on code option (green button) and download the zip file <br>
* Extract or download the folder in the required folder of your choice . (can't change afterwards)

### Executing program on windows

* Make the changes in the spotify_data.env file.
* Run the setup_1_file.bat
* You will see a shortcut created. Right click on it and go to properties. Click on shortcut key and assign a shortcut (recommandation : ctrl+alt+. )
* After that click on setup_2_file.bat which will copy the shortcut to C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu".
* U can also update shortcut by changing the key here and clicking on setup_2_file.bat
* Now run the file directly or via shortcut . When you run for the first time a browser window containing the spotify page will pop up. Agree and press continue . After that copy the url that appears (a google callback page will appear)
* That's it (❁´◡`❁)


## Help
* It may take a few tries to get the spotify redirect url working.
* Make sure your running from the correct path.

## Author 🗿
Jidu Krishna P J <br>
Instagram : [@jidukrishnapj](https://www.instagram.com/jidukrishnapj/) <br>
Github : [@jidukrishna](https://github.com/jidukrishna)

## Version History

* 0.1
    * Initial Release

## License

```
Copyright [2024] [Jidu Krishna P J]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Made with the help of
* [spotipy](https://pypi.org/project/spotipy/)

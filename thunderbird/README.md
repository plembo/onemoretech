# Gnome desktop files for Thunderbird
I recently decided to give the latest Thunderbird (as of this writing v68.1.0) a try, which is only available for Ubuntu in tarball format. After extracting to /opt/thunderbird, I proceeded to create the .desktop file and icons needed. What you see here is the result.

My process to deploy these is to zip them up and then extract into /usr/share, although ~/.local/share would work as well. Just remember to refresh your icon cache after extracting (```sudo update-icon-caches /usr/share/icons/*```, or ```update-icon-caches ~/.local/share/icons/*```) to ensure the desktop can see the new icons.


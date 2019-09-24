# Gnome desktop files for Thunderbird
I recently decided to give the latest Thunderbird (as of this writing v68.1.0) a try, which is only available for Ubuntu in tarball format. After extracting to /opt/thunderbird, I proceeded to create the .desktop file and icons needed. What you see here is the result.

My process to deploy these is to zip them up and then extract into /usr/share, although ~/.local/share would work as well.

```
$ cd thunderbird
$ zip -r thunderbird.zip *
$ sudo unzip thunderbird.zip -d /usr/share
```

Just remember to refresh your icon cache after extracting:

```
sudo update-icon-caches /usr/share/icons/*
```


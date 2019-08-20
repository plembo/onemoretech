# Motion server configuation
Using motion 4.2.2 from the [Motion project](https://motion-project.github.io) on Ubuntu Server 18.04.3 (headless). This is a simple setup to support 3 outdoor [Wyze](https://wyzecam.com) remote IP cameras that stream over RTSP (using latest Beta firmware). Note
that the setup includes control by systemd running the service as a local "motion" user.

Files provided:

```
/etc/motion/motion.conf
/etc/motion/camera1.conf
/etc/motion/camera2.conf
/etc/motion/camera3.conf
/etc/logrotate.d/motion
/etc/systemd/system/motion.service
```

Data and logs are stored on a separate ext4 volume (in my case /data/app/motion and /data/logs/motion).
Original shipping configs from the motion project provided for comparison have "-dist" in their names.
Log level reduced to 4 and log rotation scheduled every 4 days.

Main changes made include setting netcam_keepalive and netcam_set_tcp to "on" to maintain a connection
between the RTSP server on the camera and the motion server.

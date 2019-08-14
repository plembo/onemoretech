# Motion server configuation
Using motion 4.2.2 from the [Motion project](https://motion-project.github.io) on Ubuntu Server 18.04.3 (headless). This is a simple setup to support 3 outdoor [Wyze](https://wyzecam.com) remote IP cameras that stream over RTSP. Note that the setup includes control by systemd running the service as a local "motion" user. Data is stored on a separate ext4 volume.

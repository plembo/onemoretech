# Gerbera Media Server Configuration
My configuration for the open source [Gerbera UPnP media server](https://github.com/gerbera/gerbera) in the [docker container](https://hub.docker.com/r/gerbera/gerbera) maintained by the project.

The docker "run" script provides the main details:

* Separate docker volume for root's home directory (used by Gerbera to hold its configuration and sqlite database.
* Explicitly mapping the ports for SSDP (1900/udp) and data/web (49152/tcp).
* Mapping my server's top level media directory (/d1/media) as a volume inside
the container so that Gerbera can access it.
* Increasing the SSDP discovery interval to 3 minutes from a half hour (180s vs the 1800s default).

That's pretty much it. My main beef with Gerbera is that its documentation
consistently fails to address really basic, practical, questions like "how do
I actually set this up in docker?" This repo is a very superficial attempt at
filling that gap.


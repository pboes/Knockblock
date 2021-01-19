# Knockblock

Knockblock was an installation that I set up in 2016. The idea was to connect
a piece of wood and a little hammer to Twitter and "knock on wood" whenever
somebody would tweet something that, in the physical world, would prompt people
to knock on wood. Doing this, I wanted to "investigate", as they say so
beautifully, the material conditions for superstition and magic more generally
to be credible as well as the extent to which these conditions can be
transferred into the digital realm. This repo contains the files I used back
then. 

The setup was simple: Connect to the Twitter API and listen to terms associated
to "knockin on wood", then activate my hammer using a solenoid via the serial
library. Most of the repo is a standard Django setup which I used to display
the tweets alongside the installation in what I know believe was a bit of an
overkill solution using a database of tweets, jquery scripts etc. You can find
footage and an accompanying essay about the knockblock in action 
[here](https://beingbutlumps.wordpress.com/portfolio/knockblock/).


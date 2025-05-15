A practice room from TryHackMe. Problem statement : Someone broke into our office last night, but they destroyed the hard drives with the security footage. Can you recover the footage?

Given ::: We have a pcap file that captures the TCP stream for Security Footage. Download it from TryHackMe Platform.

We will use this TCP stream to get the flag. Go to Analyze -> Follow -> TCP Stream 

You can see stream encoding is set to chunked and content type is multipart/x-mixed-replace; boundary=BoundaryString that is basically for motion jpeg.



Save this stream in RAW format named as stream.raw.


Now we will use python to dechunk this raw stream. Python script is attached here. You can use chatgpt to get it too.

Now run " ffmpeg -framerate 10 -i frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4 " to get footage. 

Footage has a video of flag. 



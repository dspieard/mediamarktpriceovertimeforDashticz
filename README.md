# MediaMarkt price over time for Dashticz
With this program you can check the price over time of a product from MediaMarkt.nl and create a graph

This program create an html that you can place in a frame for you Dashtics

1) Create a new file [filename].py (like example.py) and place it in the same dir as mmpricechecker.py and change the variables.
Make sure you use your dashtics rootfolder as the path. Dashticz will use this for creating the frame.

2) Make sure you run requirements.txt
```
pip3 install -r requirements.txt
```

3) Run the created Python file (or create a cronjob, that's what I did to auto-update it)

4) Changes in Dashtics, use below and add to column:

``` 
////////////////////// FRAMES ///////////////////////////
var frames = {}
frames.iphonechart = {
  frameurl:"iphonese.html",
  height: 400,     //height of the block in pixels
  width: 24
}
```

Done!

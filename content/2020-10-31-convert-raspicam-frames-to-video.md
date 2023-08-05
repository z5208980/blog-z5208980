---
title: "Convert Raspicam Frames To Video (ROS)"
date: "2020-10-31"
tags: ["ROS"]
image: ""
gradients: ["#0093E9", "#80D0C7"]
---

[Offical ROS Reference](https://wiki.ros.org/rosbag/Tutorials/Exporting%20image%20and%20video%20data)

## Convert Image topic to mp4
To download each frame in rosbag we’ll need, `mjpegtools`

```bash
roscd image_view
rosmake image_view
sudo apt-get install mjpegtools
```

### Creating .launch for export
**Note**: For `raspicam_node` which only publishes `compressed`, you’ll need to run a republish to convert the compressed image to raw (We will need the raw image in the launch file).

```bash
rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image/image_raw
```

Create a launch file anywhere, `export.launch` and change `args` for rosbag to the `.bag` dir.

```xml
<launch>
	<node pkg="rosbag" type="play" name="rosbag" required="true" args=“.bag dir”/>
	<node name="extract" pkg="image_view" type="extract_images" respawn="false" required="true" output="screen" cwd="ROS_HOME">
		<remap from="image" to="raspicam_node/image/image_raw"/>
	</node>
</launch>
```
Once done, export the image with,
```bash
roslaunch export.launch
```

## Converting frames into mp4
The export frame should exist in `~/.ros`. Move the files to somewhere else,

```bash
cd ~
mkdir tmp
mv ~/.ros/frame*.jpg tmp/
```

To convert the frames, we’ll be using `ffmpeg`.

```bash
sudo apt install ffmpeg
```

and using `ffmpeg`, enter as such to obtain `output.mp4` (Note you can adjust the frame rate).

```bash
ffmpeg -framerate 5 -i frame%04d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv4
```
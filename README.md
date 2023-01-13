                                                                    Abstract 

	

In this project I attempt to make a script that can track a person’s eyes. This script can have many applications in the real world such as, gaze detection technology which can tell where a person is looking based on their eyes only and then process if the person is paying attention or not. 
Another application for this technology is to control things with just tracking the user’s eyes. This may be needed not due to need for comfort but for a user who is confined to just the use of their eyes and can prove to be very helpful in situations like paralysis where communication itself is not conventionally possible. For this project, there was a lot of setup. The first step was to understand what eye-tracking is and how it is done.
My goal was to understand different eye tracking techniques, learning the concept and how they try to solve the problems faced. I tried to build an eye tracking script that did not use any eye tracking libraries so that I could implement the concept myself.


Structure of an eye 

For this project, I only needed to understand the structure of the eye from the front as that was the viewing angle for the camera in an ideal setting. 




![image](https://user-images.githubusercontent.com/79290729/212207089-ca2815a2-93e3-494a-90c3-59d9f02991bf.png)





This is the structure of the eye as seen from the front and it consists the following components –
•	Pupil
•	Iris
•	Sclera (MyHealth.Alberta, 2019)
Technical Discussion
In this diagram, I could see some obvious things that could be easily be separated from the rest of the photo with the help of the things that I had learned while working on my labs. This mainly gets divided into three things that I could have tracked (but first isolated) from the photo of the eye.  That is the iris or the pupil or the sclera. (Canu, 2019)
 
After some research I found that the best way to track the eyes and also the easiest way is to track the pupils as they are the largest and the darkest mass in the whole photo and so it made sense it first isolate it and then track it.
Getting the video feed
I downloaded a sample video of an eye from the internet to use as the input for the script and first tested if the script was getting the video.

  


Cropping the image
After the video feed was working and tested, the next step was to crop the eye out of the video as it is the main part we will be focusing on. For this, we use ROI (region of interest) functionality given in OpenCV.
This is shown as follows in the code-
  
And produces the following results – 


As we can see that the frame has been cropped to our liking by entering the coordinates of the region we want to crop. 
Conversion to black and white 
After this step, I converted the frame to black and white to make it easier to work with and to make the image much simpler.
Here is the command used to do so – 
 
And here is the result – 


Here is the black and white frame along with the color one

Isolating the pupil
In this frame, there are all the parts of an eye present that can be isolated somehow and tracked. For the sake of this experiment, I decided to go with pupils as we can isolate them by setting a threshold for a certain amount of darkness in the frame and can eliminate everything that does not cross the threshold.
This is implemented in such a way-
 
And here is the result – 
 
As we can see in the results, we actually needed the pupil to be white and the rest of the photo to be black to be able to work on it and so we will invert the cv2.THRESH_BINARY to invert the colors of the frame.
Here is the result – 




Noise removal

 
As the image that I got after this step was very noisy due to the dark parts of the eye elsewhere and the eyelashes also matched my threshold. For this, I referred to my previous lecture slides and found that gaussian blur can help with noise removal and is also somewhat easier to use.
Here is the implementation – (Canu, 2019)
 
And here is the result- 
 
This step seemed to do the trick, but I had to find the balance between the size of the kernel that I chose and the level of noise removal it did. Eventually, the kernel size 7 proved to be the best.
Detecting the edges –
Now that we have only the pupil showing up in our desired frame, we can start finding the edges and for that I have used the find contours functionality in OpenCV which I learned in my previous lab
Here is the implementation of the find contour functionality and with it I printed out the contours to check if everything was working fine or not. – 
 
Here is the result of the script and in the command line, we can see the contours being printed. The next step is to draw the contours onto the main video

 
Drawing the contours
In this step, I drew the contours over the original cropped feed and removed the print command to check how everything was working. I used a simple imshow command to draw the contours with a for loop to keep drawing the contours. 



Here is the result – 
 

Polishing the detection
Even after this step, we still are detecting a small area that is above the pupil and it is constantly there in the video feed. Our next step is to knock this out of the final image and to do that, we must sort the frames with the contours first. The idea behind this being that in every frame, all the contours that are detected will be kept in the descending order according to the area of that contour. As in each frame, the contour with the biggest frame is the one around the pupil and not the one above it.  This means that we only must print the first contour from the for loop onto the cropped frame and not the other ones. This should eliminate the second and the smaller contour showing up in each frame. (Canu, 2019)
To implement this, we must use a function that will sort the contours. For that, we will use ‘lambda’ as our key and will implement it something like this (M, 2018) – 
 
And here are the results that this gets us – 
 
Here, we can see that the smaller contour that was above the pupil has now been completely removed.
Milestone
At this point in the project, I had reached the goal that I had set for myself that was to construct an eye tracking script without using any premade libraries and implementing the concept myself. Here I had an opportunity to finish the project as I had a working model of an eye tracking script, but I was not satisfied with the fact that it was doing so on a pre-made video.
•	I wanted to integrate the webcam in my laptop to make the whole script work in real time. 
•	This was a huge challenge because before, I had a script that was optimized to only one high quality video and I had to convert it to a script that could track the eye in real time from the feed I got from the webcam. 
•	The main challenge that I wanted to overcome now was to move on from a predefined region of interest to a region of interest that was automatically drawn around the eyes wherever they were in the frame.




Taking the feed from the webcam
The first part in making the script work real time was to have a real time video feed from the webcam. This is a simple step. To get the feed from the webcam, we need to implement the following code- 
 

After this step, the first real challenge arrives. Now I had to track the face and turn it into a region of interest. After this, I can track the face and crop it from a live feed. The reason behind first tracking the face was so that no other place other than a face would then be scanned for eyes instead of the whole frame which increases the risk of false positives.

Tracking the face 

The next step is to track the face and calculating the new region of interest as the person’s eyes. After which we can apply the various filters to the new roi and can see if that works or not. For the face and eye detection purposes, I looked online for some ways we can accomplish that and came across the cascades functionality in OpenCV (sentdex, 2016). I specifically found haar cascades to be useful because I could then get the region of interest that I want while getting the feed from the webcam and not relying on a steady video which greatly increases the functionality and capability.

For the purpose of testing, I first constructed the face and eye detection script separately and later integrate it with the eye tracking software.

Here is the script that I constructed: 
 





Here are the results: 

 

As you can see, the script was detecting my eyes very well. I preferred frontal face tracking only because I wanted to track someone’s attention and for that reason, only the frontal face detection is required to determine if the person is facing the screen or not. This can be seen in this example where I am not facing the screen and the software stops the detection as well. This can be used as a great indicator to tell when a person is paying attention or not.

 

Combining the codes

My next step was to combine the face tracking software and the eye tracking software so that we can detect a face, detect its eyes, set that as our region of interest and track the pupils from there. In theory this is a great plan as it can detect a face anywhere in the frame, and once we have the face, we can then cut in on the eyes and track them.

To do this, I took the face detection script and added the code for pupil detection right after the eyes get detected so that the computer can move on to tracking the pupils once the eyes are detected.

Here is what the code looks like: 
 

While everything seemed to be perfect in theory, this is the result I got: 

 

After a lot of research, I found that the resolution of the webcam was not good enough to zoom in that much into a moving face and still have enough detail left to track the pupils. And so, I moved on to find another solution to this problem.

After this I tried detecting only the eyes in my original script and applying my filters over that. For this, I modified my original script and added the eye detection cascades to it. I then used the detected area as my ROI and tried to apply my filter over those.
Here is the code: 
 

Here is the result: 

 

At this point, the detection algorithm that I had prepared could not work well enough to track the eyes and the camera quality couldn’t keep up with the demand as well, so I decided to stop here.

Result
In the end, I was able to take the feed from my laptop webcam and could detect the eyes no matter where my face was in the frame. This worked well and detected both the eyes really well. I will continue working on how to get the eye tracking going and eventually, a fully functional gaze detection script that can tell where you are looking at the screen.

 






















References
Canu, S. (2019, january 4). pysource. Retrieved from pysource: https://pysource.com/2019/01/04/eye-motion-tracking-opencv-with-python/
M, S. (2018, March 15). Stack overflow. Retrieved from stack overflow: https://stackoverflow.com/questions/32669415/opencv-ordering-a-contours-by-area-python
MyHealth.Alberta. (2019, May 5). Eye structures. Retrieved from MyHealth.Alberta.ca: https://myhealth.alberta.ca/Health/Pages/conditions.aspx?hwid=tp9807#:~:text=The%20sclera%20is%20the%20tough,focus%20them%20on%20the%20retina.
sentdex. (2016, january 10). haar cascade object detection. Retrieved from youtube.com: https://www.youtube.com/watch?v=88HdqNDQsEk



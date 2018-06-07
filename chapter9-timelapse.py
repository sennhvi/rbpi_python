import subprocess
import time

for i in range(1, 10):
    filename = "test" + format(i, "03d") + ".jpg"
    # -e export to jpeg, convenient for transforming
    subprocess.call(["raspistill", "-n", "-t", "1", "-w", "200", "-h", "200", "-co",
                     "90", "-ifx", "sketch", "-e", "jpg", "-e", "jpg", "-o", filename])
    print("taking photo", i)

print("Encoding...")
# first: -r specify image amount for creating one second video
# second: -r specify frames per second in output video
# -i %03d is not format output but regex
subprocess.call(["avconv", "-r", "5", "-i", "test%03d.jpg", "-r", "24", "-s", "200x200",
                 "-vsync", "cfr", "out.mpg"])

# Optical Character Recognition-by-Vaibhav-Karnwal
python

openalpr-

OpenALPR is an open source Automatic License Plate Recognition library written in C++ with bindings in C#, Java, Node.js, Go, and Python. The library analyzes images and video streams to identify license plates. The output is the text representation of any license plate characters.

Check out a live online demo here: http://www.openalpr.com/demo-image.html

User Guide
OpenALPR includes a command line utility. Simply typing "alpr [image file path]" is enough to get started recognizing license plate images.

For example, the following output is created by analyzing this image: Plate Image

user@linux:~/openalpr$ alpr ./samplecar.png

plate0: top 10 results -- Processing Time = 58.1879ms.
    - PE3R2X     confidence: 88.9371
    - PE32X      confidence: 78.1385
    - PE3R2      confidence: 77.5444
    - PE3R2Y     confidence: 76.1448
    - P63R2X     confidence: 72.9016
    - FE3R2X     confidence: 72.1147
    - PE32       confidence: 66.7458
    - PE32Y      confidence: 65.3462
    - P632X      confidence: 62.1031
    - P63R2      confidence: 61.5089

Detailed command line usage:

user@linux:~/openalpr$ alpr --help

USAGE: 

   alpr  [-c <country_code>] [--config <config_file>] [-n <topN>] [--seek
         <integer_ms>] [-p <pattern code>] [--clock] [-d] [-j] [--]
         [--version] [-h] <image_file_path>


Where: 

   -c <country_code>,  --country <country_code>
     Country code to identify (either us for USA or eu for Europe). 
     Default=us

   --config <config_file>
     Path to the openalpr.conf file

   -n <topN>,  --topn <topN>
     Max number of possible plate numbers to return.  Default=10

   --seek <integer_ms>
     Seek to the specified millisecond in a video file. Default=0

   -p <pattern code>,  --pattern <pattern code>
     Attempt to match the plate number against a plate pattern (e.g., md
     for Maryland, ca for California)

   --clock
     Measure/print the total time to process image and all plates. 
     Default=off

   -d,  --detect_region
     Attempt to detect the region of the plate image.  [Experimental] 
     Default=off

   -j,  --json
     Output recognition results in JSON format.  Default=off

   --,  --ignore_rest
     Ignores the rest of the labeled arguments following this flag.

   --version
     Displays version information and exits.

   -h,  --help
     Displays usage information and exits.

   <image_file_path>
     Image containing license plates


   OpenAlpr Command Line Utility

Binaries
Pre-compiled Windows binaries can be downloaded on the releases page

Install OpenALPR on Ubuntu 16.04 with the following commands:

sudo apt-get update && sudo apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev
Documentation
Detailed documentation is available at doc.openalpr.com

Integrating the Library
OpenALPR is written in C++ and has bindings in C#, Python, Node.js, Go, and Java. Please see this guide for examples showing how to run OpenALPR in your application: http://doc.openalpr.com/bindings.html

Compiling
Build Status

OpenALPR compiles and runs on Linux, Mac OSX and Windows.

OpenALPR requires the following additional libraries:

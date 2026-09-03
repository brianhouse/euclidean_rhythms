Euclidean Rhythms in Python
==================================================

After encountering some [buzz](http://ruinwesen.com/blog?id=216) about it online, I read and was inspired by Godfried Toussaint’s paper, [“The Euclidean Algorithm Generates Traditional Musical Rhythms”](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf). In short, he demonstrates how many classic rhythms, particularly of African origin, can be described by a ubiquitous mathematical principle first documented by Euclid and even used for timing patterns in neutron accelerators.

However, while I found many implementations of the algorithm in various languages, all of the ones I tried (in Ruby, Python, Java, and Javascript) return inaccurate results! Trying 13 steps with 5 pulses was an easy way to break most of them. Luckily, Toussaint’s source, Björklund, provides C code in his paper [The Theory of Rep-Rate Pattern Generation in the SNS Timing System](https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf). I translated this into Python 3, and found the result to accurate.

...except it didn't exactly match what was in Toussaint's paper, being rotations of those strings. Turns out the [Bresenham algorithm](https://arxiv.org/abs/2206.12421) is a better fit, so this module offers both options. (Some rhythm necklaces still don't match what Toussaint uses, but he likely rotated those to match traditional musical patterns)

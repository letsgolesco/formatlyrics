# FormatLyrics - Use it to format lyrics!

Ay what up it's your boy young junior dev aka old intern aka amateur
expert

# Why I made it - the long short story
I found the lyrics for Moonhead by Hymie's Basement on songmeanings.com
but it wasn't up on RapGenius, so I decided to copy-paste them over. The
lines weren't capitalized though, and unformatted bullshit like that
won't fly. Going through and manually capitalizing each line would have
worked, but it also would have lowered my self esteem and made me feel
like a caveman.

At some point I also felt like I wanted to remove the periods that
showed up periodically in the transcription, so I made an option to
remove those. But why stop there? The option ended up removing whatever
characters you want, so you can go wild and exterminate all undesired
ASCII.

SO I learned a bit about python's cool-ass `getopt` module and made this
little thing that a million other people have probably made better
versions of... ENJOY!

# Usage:
python formatlyrics.py -i <input_filename> -o <output_filename> ...

# Additional options include:
-c             capitalize each line
-r <chars>     removes the chars from the file

Title:  Why python
Date: 2010-12-03 10:20
Category: Python
Tags: python
Slug: why-python
Author: Alas Zhang

#Why Python?
为什么是python呢？
	Cardinal Biggles had Eric in the comfy chair for over four hours before wringing this confession from him...
My first look at Python was an accident, and I didn't much like what I saw at the time. It was early 1997, and Mark Lutz's book Programming Python from O'Reilly & Associates had recently come out. O'Reilly books occasionally land on my doorstep, selected from among the new releases by some mysterious benefactor inside the organization using a random process I've given up trying to understand.

One of them was Programming Python. I found this somewhat interesting, as I collect computer languages. I know over two dozen general-purpose languages, write compilers and interpreters for fun, and have designed any number of special-purpose languages and markup formalisms myself. My most recently completed project, as I write this, is a special-purpose language called SNG for manipulating PNG (Portable Network Graphics) images. Interested readers can surf to the SNG home page at [http://www.catb.org/~esr/sng/](ttp://www.catb.org/~esr/sng/). I have also written implementations of several odd general-purpose languages on my Retrocomputing Museum page, [http://www.catb.org/retro/](http://www.catb.org/retro/).

I had already heard just enough about Python to know that it is what is nowadays called a “scripting language”, an interpretive language with its own built-in memory management and good facilities for calling and cooperating with other programs. So I dived into Programming Python with one question uppermost in my mind: what has this got that Perl does not?

Perl, of course, is the 800-pound gorilla of modern scripting languages. It has largely replaced shell as the scripting language of choice for system administrators, thanks partly to its comprehensive set of UNIX library and system calls, and partly to the huge collection of Perl modules built by a very active Perl community. The language is commonly estimated to be the CGI language behind about 85% of the “live” content on the Net. Larry Wall, its creator, is rightly considered one of the most important leaders in the Open Source community, and often ranks third behind Linus Torvalds and Richard Stallman in the current pantheon of hacker demigods.

At that time, I had used Perl for a number of small projects. I'd found it quite powerful, even if the syntax and some other aspects of the language seemed rather ad hoc and prone to bite one if not used with care. It seemed to me that Python would have quite a hill to climb as yet another scripting language, so as I read, I looked first for what seemed to set it apart from Perl.

I immediately tripped over the first odd feature of Python that everyone notices: the fact that whitespace (indentation) is actually significant in the language syntax. The language has no analog of the C and Perl brace syntax; instead, changes in indentation delimit statement groups. And, like most hackers on first realizing this fact, I recoiled in reflexive disgust.

I am just barely old enough to have programmed in batch FORTRAN for a few months back in the 1970s. Most hackers aren't these days, but somehow our culture seems to have retained a pretty accurate folk memory of how nasty those old-style fixed-field languages were. Indeed, the term “free format”, used back then to describe the newer style of token-oriented syntax in Pascal and C, has almost been forgotten; all languages have been designed that way for decades now. Or almost all, anyway. It's hard to blame anyone, on seeing this Python feature, for initially reacting as though they had unexpectedly stepped in a steaming pile of dinosaur dung.

That's certainly how I felt. I skimmed through the rest of the language description without much interest. I didn't see much else to recommend Python, except maybe that the syntax seemed rather cleaner than Perl's and the facilities for doing basic GUI elements like buttons and menus looked fairly good.

I put the book back on the shelf, making a mental note that I should code some kind of small GUI-centered project in Python sometime, just to make sure I really understood the language. But I didn't believe what I'd seen would ever compete effectively with Perl.

A lot of other things conspired to keep that note way down on my priority list for many months. The rest of 1997 was eventful for me; it was, among other things, the year I wrote and published the original version of “The Cathedral and the Bazaar”. But I did find time to write several Perl programs, including two of significant size and complexity. One of them, **keeper**, is the assistant still used to file incoming submissions at the Metalab software archive. It generates the web pages you see at metalab.unc.edu/pub/Linux/!INDEX.html. The other, **anthologize**, was used to automatically generate the PostScript for the sixth edition of Linux from the Linux Documentation Project's archive of HOWTOs. Both programs are available at Metalab.

Writing these programs left me progressively less satisfied with Perl. Larger project size seemed to magnify some of Perl's annoyances into serious, continuing problems. The syntax that had seemed merely eccentric at a hundred lines began to seem like a nigh-impenetrable hedge of thorns at a thousand. “More than one way to do it” lent flavor and expressiveness at a small scale, but made it significantly harder to maintain consistent style across a wider code base. And many of the features that were later patched into Perl to address the complexity-control needs of bigger programs (objects, lexical scoping, “use strict”, etc.) had a fragile, jerry-rigged feel about them.

These problems combined to make large volumes of Perl code seem unreasonably difficult to read and grasp as a whole after only a few days' absence. Also, I found I was spending more and more time wrestling with artifacts of the language rather than my application problems. And, most damning of all, the resulting code was ugly—this matters. Ugly programs are like ugly suspension bridges: they're much more liable to collapse than pretty ones, because the way humans (especially engineer-humans) perceive beauty is intimately related to our ability to process and understand complexity. A language that makes it hard to write elegant code makes it hard to write good code.

With a baseline of two dozen languages under my belt, I could detect all the telltale signs of a language design that had been pushed to the edge of its functional envelope. By mid-1997, I was thinking “there has to be a better way” and began casting about for a more elegant scripting language.

One course I did not consider was going back to C as a default language. The days when it made sense to do your own memory management in a new program are long over, outside of a few specialty areas like kernel hacking, scientific computing and 3-D graphics—places where you absolutely must get maximum speed and tight control of memory usage, because you need to push the hardware as hard as possible.

For most other situations, accepting the debugging overhead of buffer overruns, pointer-aliasing problems, malloc/free memory leaks and all the other associated ills is just crazy on today's machines. Far better to trade a few cycles and a few kilobytes of memory for the overhead of a scripting language's memory manager and economize on far more valuable human time. Indeed, the advantages of this strategy are precisely what has driven the explosive growth of Perl since the mid-1990s.

I flirted with Tcl, only to discover quickly that it scales up even more poorly than Perl. Old LISPer that I am, I also looked at various current dialects of Lisp and Scheme—but, as is historically usual for Lisp, lots of clever design was rendered almost useless by scanty or nonexistent documentation, incomplete access to POSIX/UNIX facilities, and a small but nevertheless deeply fragmented user community. Perl's popularity is not an accident; most of its competitors are either worse than Perl for large projects or somehow nowhere near as useful as their theoretically superior designs ought to make them.

My second look at Python was almost as accidental as my first. In October 1997, a series of questions on the fetchmail-friends mailing list made it clear that end users were having increasing trouble generating configuration files for my fetchmail utility. The file uses a simple, classically UNIX free-format syntax, but can become forbiddingly complicated when a user has POP3 and IMAP accounts at multiple sites. As an example, see Listing 1 for a somewhat simplified version of mine.

[Listing 1](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3882/3882l1.html)

I decided to attack the problem by writing an end-user-friendly configuration editor, fetchmailconf. The design objective of fetchmailconf was clear: to completely hide the control file syntax behind a fashionable, ergonomically correct GUI interface replete with selection buttons, slider bars and fill-out forms.

The thought of implementing this in Perl did not thrill me. I had seen GUI code in Perl, and it was a spiky mixture of Perl and Tcl that looked even uglier than my own pure-Perl code. It was at this point I remembered the bit I had set more than six months earlier. This could be an opportunity to get some hands-on experience with Python.

Of course, this brought me face to face once again with Python's pons asinorum, the significance of whitespace. This time, however, I charged ahead and roughed out some code for a handful of sample GUI elements. Oddly enough, Python's use of whitespace stopped feeling unnatural after about twenty minutes. I just indented code, pretty much as I would have done in a C program anyway, and it worked.

That was my first surprise. My second came a couple of hours into the project, when I noticed (allowing for pauses needed to look up new features in Programming Python) I was generating working code nearly as fast as I could type. When I realized this, I was quite startled. An important measure of effort in coding is the frequency with which you write something that doesn't actually match your mental representation of the problem, and have to backtrack on realizing that what you just typed won't actually tell the language to do what you're thinking. An important measure of good language design is how rapidly the percentage of missteps of this kind falls as you gain experience with the language.

When you're writing working code nearly as fast as you can type and your misstep rate is near zero, it generally means you've achieved mastery of the language. But that didn't make sense, because it was still day one and I was regularly pausing to look up new language and library features!

This was my first clue that, in Python, I was actually dealing with an exceptionally good design. Most languages have so much friction and awkwardness built into their design that you learn most of their feature set long before your misstep rate drops anywhere near zero. Python was the first general-purpose language I'd ever used that reversed this process.

Not that it took me very long to learn the feature set. I wrote a working, usable fetchmailconf, with GUI, in six working days, of which perhaps the equivalent of two days were spent learning Python itself. This reflects another useful property of the language: it is compact--you can hold its entire feature set (and at least a concept index of its libraries) in your head. C is a famously compact language. Perl is notoriously not; one of the things the notion “There's more than one way to do it!” costs Perl is the possibility of compactness.

But my most dramatic moment of discovery lay ahead. My design had a problem: I could easily generate configuration files from the user's GUI actions, but editing them was a much harder problem. Or, rather, reading them into an editable form was a problem.

The parser for fetchmail's configuration file syntax is rather elaborate. It's actually written in YACC and Lex, two classic UNIX tools for generating language-parsing code in C. In order for fetchmailconf to be able to edit existing configuration files, I thought it would have to replicate that elaborate parser in Python. I was very reluctant to do this, partly because of the amount of work involved and partly because I wasn't sure how to ascertain that two parsers in two different languages accept the same. The last thing I needed was the extra labor of keeping the two parsers in synchronization as the configuration language evolved!

This problem stumped me for a while. Then I had an inspiration: I'd let fetchmailconf use fetchmail's own parser! I added a --configdump option to fetchmail that would parse .fetchmailrc and dump the result to standard output in the format of a Python initializer. For the file above, the result would look roughly like Listing 2 (to save space, some data not relevant to the example is omitted).

[Listing 2](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3882/3882l2.html)

Python could then evaluate the fetchmail --configdump output and have the configuration available as the value of the variable “fetchmail”.

This wasn't quite the last step in the dance. What I really wanted wasn't just for fetchmailconf to have the existing configuration, but to turn it into a linked tree of live objects. There would be three kinds of objects in this tree: Configuration (the top-level object representing the entire configuration), Site (representing one of the sites to be polled) and User (representing user data attached to a site). The example file describes five site objects, each with one user object attached to it.

I had already designed and written the three object classes (that's what took four days, most of it spent getting the layout of the widgets just right). Each had a method that caused it to pop up a GUI edit panel to modify its instance data. My last remaining problem was somehow to transform the dead data in this Python initializer into live objects.

I considered writing code that would explicitly know about the structure of all three classes and use that knowledge to grovel through the initializer creating matching objects, but rejected that idea because new class members were likely to be added over time as the configuration language grew new features. If I wrote the object-creation code in the obvious way, it would be fragile and tend to fall out of sync when either the class definitions or the initializer structure changed.

What I really wanted was code that would analyze the shape and members of the initializer, query the class definitions themselves about their members, and then adjust itself to impedance-match the two sets.

This kind of thing is called metaclass hacking and is generally considered fearsomely esoteric—deep black magic. Most object-oriented languages don't support it at all; in those that do (Perl being one), it tends to be a complicated and fragile undertaking. I had been impressed by Python's low coefficient of friction so far, but here was a real test. How hard would I have to wrestle with the language to get it to do this? I knew from previous experience that the bout was likely to be painful, even assuming I won, but I dived into the book and read up on Python's metaclass facilities. The resulting function is shown in Listing 3, and the code that calls it is in Listing 4.

[Listing 3](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3882/3882l3.html)

[Listing 4](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3882/3882l4.html)

That doesn't look too bad for deep black magic, does it? Thirty-two lines, counting comments. Just from knowing what I've said about the class structure, the calling code is even readable. But the size of this code isn't the real shocker. Brace yourself: this code only took me about ninety minutes to write—and it worked correctly the first time I ran it.

To say I was astonished would have been positively wallowing in understatement. It's remarkable enough when implementations of simple techniques work exactly as expected the first time; but my first metaclass hack in a new language, six days from a cold standing start? Even if we stipulate that I am a fairly talented hacker, this is an amazing testament to Python's clarity and elegance of design.

There was simply no way I could have pulled off a coup like this in Perl, even with my vastly greater experience level in that language. It was at this point I realized I was probably leaving Perl behind.

This was my most dramatic Python moment. But, when all is said and done, it was just a clever hack. The long-term usefulness of a language comes not in its ability to support clever hacks, but from how well and how unobtrusively it supports the day-to-day work of programming. The day-to-day work of programming consists not of writing new programs, but mostly reading and modifying existing ones.

So the real punchline of the story is this: weeks and months after writing fetchmailconf, I could still read the fetchmailconf code and grok what it was doing without serious mental effort. And the true reason I no longer write Perl for anything but tiny projects is that was never true when I was writing large masses of Perl code. I fear the prospect of ever having to modify keeper or anthologize again—but fetchmailconf gives me no qualms at all.

Perl still has its uses. For tiny projects (100 lines or fewer) that involve a lot of text pattern matching, I am still more likely to tinker up a Perl-regexp-based solution than to reach for Python. For good recent examples of such things, see the timeseries and growthplot scripts in the fetchmail distribution. Actually, these are much like the things Perl did in its original role as a sort of combination awk/sed/grep/sh, before it had functions and direct access to the operating system API. For anything larger or more complex, I have come to prefer the subtle virtues of Python—and I think you will, too.

[Resources](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3882/3882s1.html)

All listings referred to in this article are available by anonymous download in the file [ftp.linuxjournal.com/pub/lj/listings/issue73/3882.tgz]([ftp.linuxjournal.com/pub/lj/listings/issue73/3882.tgz).


Eric Raymond is a Linux advocate and the author of The Cathedral & The Bazaar . He can be reached via e-mail at (esr@thyrsus.com).

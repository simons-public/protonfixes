# libwebkit2gtk wrapper instructions

This document outlines how to recreate the libwebkit2gtk shared library
present in this folder.

## Why do this?
Soldier is a new runtime released by Steam, that powers Proton 5.13+.  
While a great step to enhance cross-distro compatibility in games, it poses
some challenges in regards to installing additional software to make protonfixes
work properly. On the flipside, once it does work it means we don't need to
install packages manually and that everything runs smoothly in a containerized
environment.  
One of the main components of protonfixes is zenity, a program that show the progress
of protonfixes before launching the game, it's very important to have it
otherwise a user might think that steam has silently crashed or something similar.  
One might think that unzipping the binary release of zenity onto the root might
do the trick, however one *big* dependency of zenity is webkit2gtk, which is
used for the very niche html mode. Having webkit2gtk as a binary dependency is
quite cumbersome as it pulls in all the webkit dependencies, such as libraries
for videos, pictures etc.  
To fix this problem we use a library that declares the same symbols as the 
original library, so that we trick the linker in running zenity. As long
as the html mode is not used it shouldn't cause any issues.

## Actually Building the shared library

In order to rebuild the so the following programs are needed:

* nasm
* gcc
* readelf

First download the real deal™ library from the debian repositories, and extract
it. At the time of writing the shared library is called `libwebkit2gtk-4.0.so.37.44.6`.  
Then run:

``` bash
readelf -Ws libwebkit2gtk-4.0.so.37.44.6 | grep webkit_ | awk '{print $8}' > webkit-symbols.txt
echo 'BITS 64' > webkit-shim.S
cat webkit-symbols.txt | xargs -n1 printf 'global %s:function\n' >> webkit-shim.S
echo 'section .text' >> webkit-shim.S
cat webkit-symbols.txt | xargs -n1 printf '%s: ret\n' >> webkit-shim.S
# Now we compile the asm file
nasm -f elf64 webkit-shim.S -o webkit-shim.o
gcc -shared webkit-shim.o -o libwebkit2gtk-4.0.so.37
```

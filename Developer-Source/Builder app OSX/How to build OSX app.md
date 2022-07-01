# How to build OSX cat-net app
Welcome Developer! if you've ended up in this guide, you probably either can't mind your own business, or (most likely) you're here to create your own version of the Cat-Net app. In this guide, you will find a detailed guide to every single line of code. So that we can replicate our builds!
## Explanation of the code.
⚠️**Premise**. We use the **py2app** library to generate apps for OSX. **Do not take this guide as a documentation of the library itself**. As here you will find only the information you will need to create your build!

**Row n ° 7**: The name of the cat-net source code must be entered in this line. We developers always recommend calling main like this: CAT-NET V (version number) - (beta or stable) - (cli or gui) .py.

**Row n ° 8**: 
Here you have to enter all the options containing information to be shown inside the finder or for example by right clicking -> get information. Pay attention to line 9. Where the app icon is defined. In the "Other Source" folder you will find two icons. one .ico (for windows) and one .icns (for mac). Obviously, during the building, multiple errors will be found if you send or the format is wrong.

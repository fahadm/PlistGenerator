#!/usr/bin/python
#Copyright (C) 2013  Fahad Mansoor


#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys, optparse

def generate(server,ipa,iconSmall,iconLarge,title,subtitle,identifier,fname):
    if  server[-1] != '/' :
	server = server + '/'
    outFile = open(fname,'w')
    ipa = server +ipa
    iconSmall = server + iconSmall
    iconLarge = server + iconLarge
    
    str = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>items</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>assets</key>\n\t\t\t<array>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>kind</key>\n\t\t\t\t\t<string>software-package</string>\n\t\t\t\t\t<key>url</key>\n\t\t\t\t\t<string>'+ipa+'</string>\n\t\t\t\t</dict>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>kind</key>\n\t\t\t\t\t<string>full-size-image</string>\n\t\t\t\t\t<key>needs-shine</key>\n\t\t\t\t\t<true/>\n\t\t\t\t\t<key>url</key>\n\t\t\t\t\t<string>'+iconLarge+'</string>\n\t\t\t\t</dict>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>kind</key>\n\t\t\t\t\t<string>display-image</string>\n\t\t\t\t\t<key>needs-shine</key>\n\t\t\t\t\t<true/>\n\t\t\t\t\t<key>url</key>\n\t\t\t\t\t<string>'+iconSmall+'</string>\n\t\t\t\t</dict>\n\t\t\t</array>\n\t\t\t<key>metadata</key>\n\t\t\t<dict>\n\t\t\t\t<key>bundle-identifier</key>\n\t\t\t\t<string>'+identifier+'</string>\n\t\t\t\t<key>kind</key>\n\t\t\t\t<string>software</string>\n\t\t\t\t<key>subtitle</key>\n\t\t\t\t<string>'+subtitle+'</string>\n\t\t\t\t<key>title</key>\n\t\t\t\t<string>'+title+'</string>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n</dict>\n</plist>' 

    outFile.write(str)
    outFile.close()
    print "Plist file Successfully Created"


def main():
    optparser = optparse.OptionParser(prog='plistgen.py', version='0.0.1',
        description='Creates a simple plist file for enterprise publishing',
        usage='%prog -s [server] -i [path to ipa file] ' + \
            '-l [path to icon large] -m [path to icon small] -d [identifier] -t [title] -u [subtitle] -f [outputfilename] ')

    optparser.add_option('--server', '-s', dest='server') 
    optparser.add_option('--ipa', '-i', dest='ipa')
    optparser.add_option('--icnsmall', '-m', dest='icnsmall')
    optparser.add_option('--icnlarge', '-l', dest='icnlarge')
    optparser.add_option('--identifier', '-d', dest='identifier')
    optparser.add_option('--title', '-t', dest='title')
    optparser.add_option('--subtitle', '-u', dest='subtitle')
    optparser.add_option('--outfile','-f',dest='outputfile')
    options, arguments = optparser.parse_args()
    if options.server and options.ipa and options.icnsmall and \
        options.icnlarge and options.identifier and options.title and options.subtitle and options.outputfile:
        generate(options.server ,options.ipa, options.icnsmall,options.icnlarge,options.title,options.subtitle,options.identifier,options.outputfile)
    else:
        optparser.print_help()
  
     


if __name__ == "__main__":
   main()

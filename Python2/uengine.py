#!/usr/bin/env python2

import sys
import os.path
import argparse

from os import path

Chars = ['', '.', '-', '_']

InFile = ''
OutFile = ''

Check = False
Domain = ''

InNames = [];
OutNames = [];

def Description(man=False):
    var = ''
    ds = '\n\n'

    if man == True:
        var += '# Author: NoSkillNick'
        var += ds

    var += 'Manipulates first and last names to generate possible usernames and emails'
    var += ds

    if man == False:
        var += 'View Example Commands:\n'
        var += './uengine.py -m'
        var += ds

    var += 'For Additional Help Visit:\n'
    var += 'http://www.github.com\n'
    var += 'http://www.youtube.com'
    var += ds

    if man == True:
        var += 'Example Usage:\n'
        var += '# Single Name\n'
        var += './uengine.py -n \'Joe Schmoe\''
        var += ds
        var += '# Name List\n'
        var += './uengine.py -n \'Joe Schmoe, George Brown, Paul Jones\''
        var += ds
        var += '# Name File\n'
        var += './uengine.py -f in.txt -o out.txt'
        var += ds
        var += '# Output emails\n'
        var += './uengine.py -n \'Joe Schmoe\' -e -d domain.com'
        var += ds
        var += '# Output to file\n'
        var += './uengine.py -n \'Joe Schmoe, George Brown, Paul Jones\' -o out.txt'
        var += ds
        var += '# Generate more combinations with char list\n'
        var += './uengine.py -n \'Joe Schmoe\' -c '

    return var

def CheckDomain(d):
    domain = str(d.strip())

    if domain[0] == '@':
        return domain
    else:
        return '@' + domain

def OutPut(item):
    global OutNames

    if args.Email:
        OutNames.append(item + Domain)
    else:
        OutNames.append(item)

def ParseArgs():
    global args, Check, Domain, InFile, OutFile
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=Description(), usage='%(prog)s [options]', add_help=False)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-n', '--name', metavar='x', help='Names to manipulate seperated by commas')
    parser.add_argument('-f', '--file', metavar='x', help='Input file containing names to be processed')
    parser.add_argument('-o', '--out', metavar='x', help='Output file to write that will contain the results')
    parser.add_argument('-d', '--domain', metavar='x', help='Domain to append to usernames. Email must be set to true.')
    group.add_argument('-e', '--Email', action='store_true', help='Format output as email addresses')
    parser.add_argument('-c', '--Char', action='store_true', help='Include character list combinations')
    parser.add_argument('-p', '--Print', action='store_true', help='Print output to console')
    parser.add_argument('-v', '--Verbose', action='store_true', help='Verbose output (Does not print output)')
    group.add_argument("-h", "--Help", action="help", help="Displays this help message")
    group.add_argument("-m", "--Manual", action="store_true", help="Displays manual for command usage")
    parser.add_argument('-nw', '--No-Write', action='store_true', help='Do not write output to file')
    args = parser.parse_args()

    #Checks if no args were passed
    if not len(sys.argv) > 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.Manual:
        parser.description = Description(True)
        parser.print_help()
        sys.exit(0)

    InFile = str(args.file)

    if not args.out:
        OutFile = 'ue-output.txt'
    else:
        OutFile = args.out

    if args.Email:
        if not args.domain:
            print('Error: Email output was selected, but no domain was provided!')
            print('Fix: Add -d example.com')
            sys.exit(1)
        else:
            Domain = CheckDomain(args.domain)

    if args.name and not args.out:
        Check = True

def LoadNames():
    global InNames

    if args.file:
        try:
            temp = ReadFile()

            for item in temp:
                name = item.strip().lower().split()

                if len(name) == 2:
                    InNames.append(name)
                else:
                    print('Error: Input format is incorrect')
                    print('Fix: The correct format is:\nFirst Last \nFirst Last \nFirst Last')
                    sys.exit(1)
        except:
            sys.exit(0)

    if args.name:
        try:
            temp = args.name.split(',')

            for item in temp:
                name = item.strip().lower().split()

                if len(name) == 2:
                    InNames.append(name)
                else:
                    print('Error: Input format is incorrect')
                    fix = 'Fix:\n'
                    fix += 'The correct format is: -n \'Joe Schmoe\'\n'
                    fix += 'or\n'
                    fix += 'The correct format is: -n \'Joe Schmoe, George Brown, Paul Jones\''
                    print(fix)
                    sys.exit(1)
        except:
            sys.exit(1)

    if Check:
        if args.No_Write:
            return

        while True:
            val = raw_input('Would you like to write the output to a file? [y/n]: ')

            if str(val).lower() == 'y':
                print('')
                break
            elif str(val).lower() == 'n':
                args.No_Write = True
                args.Print = True
                print('')
                break

def ReadFile():
    data = []

    if path.exists(InFile):
        with open(InFile) as ufile:
            data = ufile.readlines()
        return data
    else:
        print('Error: File Not Found!')
        sys.exit(1)

def WriteFile():
    if args.No_Write:
        return

    with open(OutFile, 'w') as f:
        for item in OutNames:
            f.write("%s\n" % item)
    print('Wrote results to %s' % OutFile)

def PrintOut():
    if args.Print or args.No_Write:
        for item in OutNames:
            print(item)

    if args.Print and (args.Verbose or not args.No_Write):
        print('')

    if args.Verbose:
        print('Names Provided: %s' % len(InNames))
        print('Created %s combinations!' % len(OutNames))

    if args.Verbose and not args.No_Write:
        print('')

def CreateNames():
    global InNames, OutNames

    for name in InNames:
        first = name[0]
        last = name[1]
        char = ['']

        if (args.Email or args.Char) and not (args.Email and args.Char):
            char = Chars

        for c in char:
            #first.last
            OutPut(first + c + last)
            #last.first
            OutPut(last + c + first)
            #f.last
            OutPut(first[0] + c + last)
            #first.l
            OutPut(first + c + last[0])
            #last.f
            OutPut(last + c + first[0])

def main():
    ParseArgs()
    LoadNames()
    CreateNames()
    PrintOut()
    WriteFile()

if __name__ == "__main__":
    main()

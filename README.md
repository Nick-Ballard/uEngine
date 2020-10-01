# uengine
A simple python script that generates possible usernames and email addresses by manipulating names provided.

# Example Usage:
Single Name

./uengine.py -n 'Joe Schmoe'

Name List

./uengine.py -n 'Joe Schmoe, George Brown, Paul Jones'

Name File:<br>
./uengine.py -f in.txt -o out.txt

Output emails
./uengine.py -n 'Joe Schmoe' -e -d domain.com

Output to file
./uengine.py -n 'Joe Schmoe, George Brown, Paul Jones' -o out.txt

Generate more combinations with char list
./uengine.py -n 'Joe Schmoe' -c 


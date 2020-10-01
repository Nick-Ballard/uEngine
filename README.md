# uengine
A simple python script that generates possible usernames and email addresses by manipulating names provided.

# Example Usage
Single Name:<br>
./uengine.py -n 'Joe Schmoe'

Name List:<br>
./uengine.py -n 'Joe Schmoe, George Brown, Paul Jones'

Name File:<br>
./uengine.py -f in.txt -o out.txt

Output Emails:<br>
./uengine.py -n 'Joe Schmoe' -e -d domain.com

Output to File:<br>
./uengine.py -n 'Joe Schmoe, George Brown, Paul Jones' -o out.txt

Generate more combinations with char list<br>
./uengine.py -n 'Joe Schmoe' -c 


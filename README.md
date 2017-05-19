# my_data_project



## Background
### Problem:
Due to some error when processing a subset of the 20,000 resources before uploading it into our database, we mistakenly converted all of the descriptions of that subset entirely into title case (that is, first letter of each word is upper case, the rest of the word in lower case). 

### Solution:
I chose to write a python3 script that would parse each row and determine if the description was erroneous (if all words were in title case). For the rows that are erroneous I change the to lower case and make the first letter of each sentence upper case. To improve this, I could look for a list of proper nouns that might be in my resources list. Some thoughts on that would be to try to scrape the yellow pages or a site like yelp. Then I could look to see if those businesses's names are in those resource descriptions.

## requirements
Python3 (I used 3.6)

## directions
1. Clone into a directory that you remember
2. Assuming you're using a mac, open your terminal and `$ cd <<your path>>/my_data_project`
3. `python3 casify.py`
4. That will create a new in your current directory csv called casified_data.csv

import requests
import json
import csv

url_posts = 'https://jsonplaceholder.typicode.com/posts'
url_comments = 'https://jsonplaceholder.typicode.com/comments'

response_posts = requests.get(url_posts).text.replace('\\n', ' ')
response_comments = requests.get(url_comments).text.replace('\\n', ' ')
# print(response.status_code)

json_data_posts = json.loads(response_posts)
json_data_comments = json.loads(response_comments)

keys_posts = json_data_posts[0].keys()
keys_comments = json_data_comments[0].keys()

with open('data/post.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys_posts)
    dict_writer.writeheader()
    dict_writer.writerows(json_data_posts)

with open('data/comments.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys_comments)
    dict_writer.writeheader()
    dict_writer.writerows(json_data_comments)

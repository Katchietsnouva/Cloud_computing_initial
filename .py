# import required modules
import firebase_admin
from firebase_admin import db, credentials

# authenticate to firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://testproject-ac656-default-rtdb.asia-southeast1.firebasedatabase.app/"})
<firebase_admin.App at 0x2800fef1400>
# creating reference to root node
ref = db.reference("/")
# retrieving data from root node
ref.get()
{'language': 'Python',
 'name': 'All About Python',
 'title_count': 0,
 'titles': ['send email in python', 'create excel in python'],
 'url': 'https://youtube.com/AllAboutPython',
 'videos': [1, 2, 3]}
db.reference("/name").get()
'All About Python'
# set operation
db.reference("/videos").set(3)
ref.get()
{'language': 'Python',
 'name': 'All About Python',
 'title_count': 0,
 'titles': ['send email in python', 'create excel in python'],
 'url': 'https://youtube.com/AllAboutPython',
 'videos': 3}
# update operation (update existing value)
db.reference("/").update({"language": "python"})
ref.get()
{'language': 'python',
 'name': 'All About Python',
 'title_count': 0,
 'titles': ['send email in python', 'create excel in python'],
 'url': 'https://youtube.com/AllAboutPython',
 'videos': 3}
# update operation (add new key value)
db.reference("/").update({"subscribed": True})
ref.get()
{'language': 'python',
 'name': 'All About Python',
 'subscribed': True,
 'title_count': 0,
 'titles': ['send email in python', 'create excel in python'],
 'url': 'https://youtube.com/AllAboutPython',
 'videos': 3}
# push operation
db.reference("/titles").push().set("create modern ui in python")
ref.get()
{'language': 'python',
 'name': 'All About Python',
 'subscribed': True,
 'title_count': 0,
 'titles': {'0': 'send email in python',
  '1': 'create excel in python',
  '-NS_AHc4EiFqorc47wPo': 'create modern ui in python'},
 'url': 'https://youtube.com/AllAboutPython',
 'videos': 3}
# transaction
def increment_transaction(current_val):
    return current_val + 1

db.reference("/title_count").transaction(increment_transaction)
ref.get()
{'language': 'python',
 'name': 'All About Python',
 'subscribed': True,
 'title_count': 1,
 'titles': {'0': 'send email in python',
  '1': 'create excel in python',
  '-NS_AHc4EiFqorc47wPo': 'create modern ui in python'},
 'url': 'https://youtube.com/AllAboutPython',
 'videos': 3}
print(ref.key)
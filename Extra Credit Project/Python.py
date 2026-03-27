# downloading the subreddit CSV here
!wget -q https://raw.githubusercontent.com/almayor/reddit-mods-dataset/master/subreddits.csv -O subreddits_redditmods.csv

import pandas as pd
df = pd.read_csv('subreddits_redditmods.csv', dtype=str, low_memory=False)
print("Rows:", len(df))
df.head()

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# Using a dataset with around 25k samples (Subreddits)
# Cleaning the data

# keeping only required columns
df = df[['name', 'n_members']]

# dropping missing names
df = df.dropna(subset=['name'])

# converting everything to lowercase
df['name'] = df['name'].str.lower()

# removing duplicates
df = df.drop_duplicates(subset=['name'])

# filling up missing members
df['n_members'] = df['n_members'].fillna('0')

print("Cleaned rows:", len(df))
df.head()

class TreeNode:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, name, members):
        if root is None:
            return TreeNode(name, members)

        if name < root.name:
            root.left = self.insert(root.left, name, members)
        elif name > root.name:
            root.right = self.insert(root.right, name, members)

        return root

    def search(self, root, name):
        if root is None or root.name == name:
            return root

        if name < root.name:
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append((root.name, root.members))
            self.inorder(root.right, result)



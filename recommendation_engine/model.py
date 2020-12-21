import os
import pandas as pd

from matplotlib import pyplot
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import hind.db.blog as db_blog

MAX_BLOGS_TO_RECOMMEND = 2
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs')


class CFModel():
    def __init__(self):
        self.blogs = db_blog.get_blogs()
        self.curate_data()
        self.create_mapping()

    def curate_data(self):
        self.blogs['id'] = self.blogs['id'].astype('int')

        self.blogs["title"] = self.blogs["title"].apply(lambda x: x.replace(".", ""))
        self.blogs["category"] = self.blogs["category"].apply(lambda x: x.replace(" ", ""))
        self.blogs["location"] = self.blogs["category"].apply(lambda x: x.replace(" ", ""))
        self.blogs["tags"] = self.blogs["tags"].apply(lambda x: [i.replace(" ", "") for i in x])

        self.blogs["metadata"] = self.blogs.apply(lambda x: "" + " ".join([x["category"]]) +
                                                  " ".join([x["location"]]) + " " + " ".join(x["tags"]), axis=1)

    def create_mapping(self):
        count_vec = CountVectorizer(stop_words="english")
        count_vec_matrix = count_vec.fit_transform(self.blogs["metadata"])

        self.cosine_sim_matrix = cosine_similarity(count_vec_matrix, count_vec_matrix)
        self.mapping = pd.Series(self.blogs.index, index=self.blogs["id"])

    def recommend_blog(self, blog_id) -> list:
        blog_index = self.mapping[blog_id]

        self.similarity_score = list(enumerate(self.cosine_sim_matrix[blog_index]))
        self.similarity_score = sorted(self.similarity_score, key=lambda x: x[1], reverse=True)
        self.similarity_score = self.similarity_score[1:MAX_BLOGS_TO_RECOMMEND+1]

        blog_indices = [i[0] for i in self.similarity_score]
        return self.blogs["id"].iloc[blog_indices]

    def generate_recommendations(self):
        liked_blogs = db_blog.get_liked_blogs()
        for lb in liked_blogs:
            blog_ids = self.recommend_blog(blog_id=lb["blog_id"])
            for blog_id in blog_ids:
                db_blog.insert_recommendation(user_id=lb["user_id"], blog_id=blog_id)

    def save_outputs(self):
        temp_sim_matrix = self.cosine_sim_matrix[0:5, 0:5]
        with open(os.path.join(OUTPUT_DIRECTORY, 'cosine_sim_matrix.txt'), 'w+') as fl:
            print(temp_sim_matrix, file=fl)

        pyplot.imshow(temp_sim_matrix)
        pyplot.colorbar()
        pyplot.savefig(os.path.join(OUTPUT_DIRECTORY, 'cosine_sim_matrix.png'))

        temp_mapping = self.mapping[0:5]
        with open(os.path.join(OUTPUT_DIRECTORY, 'mapping.txt'), 'w+') as fl:
            print(temp_mapping, file=fl)

        self.recommend_blog(blog_id=10)
        temp_sim_score = self.similarity_score[0:5]
        with open(os.path.join(OUTPUT_DIRECTORY, 'similarity_score.txt'), 'w+') as fl:
            print(temp_sim_score, file=fl)

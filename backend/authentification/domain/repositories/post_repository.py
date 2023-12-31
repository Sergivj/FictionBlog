from authentification.domain.models.post_model import Post
from authentification.domain.models.user_model import User


class PostRepository:
    def get_posts(self):
        return Post.objects.all().order_by('-date_posted')

    def create_post(self, post: Post):
        Post.objects.create(title=post['title'], content=post['content'], author=User(id=post['author']['id']))

    def delete_post(self, post_id: int):
        Post.objects.get(id=post_id).delete()

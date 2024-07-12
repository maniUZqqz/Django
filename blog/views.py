from django.shortcuts import render
from datetime import date
# machine-learning

all_posts = [
    {
        'slug': 'learning-js',
        'title': 'js course',
        'author': 'QQZ',
        'image': 'js.png',
        'time': date(2021, 4, 5),
        'data': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'UZ',
        'image': 'python.png',
        'time': date(2021, 6, 3),
        'data': """ 
             Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
             Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-php',
        'title': 'php course',
        'author': 'QQU',
        'image': 'php.png',
        'time': date(2007, 3, 1),
        'data': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug': 'learning-linux',
        'title': 'Linux course',
        'author': 'kally',
        'image': 'Linux.png',
        'time': date(2022, 3, 1),
        'data': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
        perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
        deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
    """
    },
]


def time_lane(post):
    return post['time']


def blog(request):
    sorted_time = sorted(all_posts, key=time_lane)
    posts_in_page = sorted_time[-2:]
    return render(
        request, 'blog/blog.html', {'latest_posts': posts_in_page}
    )


def all_post(request):
    Context = {
        "all_posts": all_posts
    }
    return render(
        request, 'blog/all_post.html', Context
    )


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(
        request, 'blog/single_post.html', {"post": post}
    )


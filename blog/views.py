from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'QQZ',
        'image': 'django.png',
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
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! 
            Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
             Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
             Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
             Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
             Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
             Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
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
        'slug': 'learning-machine-learning',
        'title': 'ml course',
        'author': 'QQU',
        'image': 'ml.png',
        'time': date(2021, 3, 1),
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
    return render(
        request, 'blog/blog.html'
    )


def all_post(request):
    return render(
        request, 'blog/all_post.html'
    )


def single_post(request, slug):
    return render(
        request, 'blog/single_post.html'
    )
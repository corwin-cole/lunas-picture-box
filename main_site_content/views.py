from collections import OrderedDict
from operator import itemgetter
from django.views.generic import DetailView
from .models import MainSiteContent
from photos.models import Photo
from blog.models import BlogPost


class MainSiteView(DetailView):
    """
    Single view class, convenient for an entire one-page site.
    """
    model = MainSiteContent
    template_name = 'base.html'

    def get_object(self, queryset=None):
        # For good measure, assume queryset could be set manually if this is called from elsewhere
        if not queryset:
            return self.model.objects.get(is_live=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(MainSiteView, self).get_context_data(**kwargs)

        # Add up to 20 randomly-ordered photos to context
        photos = Photo.objects.filter(is_live=True).order_by('?')[:20]
        ctx['photos'] = photos

        # Analyze the most-represented categories in the photos
        categories = {}
        # Count the number of photos in each category in the current photo queryset
        for photo in photos:
            if photo.category in categories:
                categories[photo.category] += 1
            else:
                categories[photo.category] = 1
        # Create a dictionary ordered by the number of photos per category
        ctx['categories'] = OrderedDict(categories.items(), key=itemgetter(1), reverse=True)

        # Include up to 10 blog posts
        blog_posts = BlogPost.objects.all()[:10]
        ctx['blog_posts'] = blog_posts

        return ctx

from blog.models import Article
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(is_published=True)
        return queryset


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')

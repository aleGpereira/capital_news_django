from django.contrib.auth.models import User

from .models import Post


def get_pendings(username):
    pendings = 0
    user = User.objects.filter(username=username).first()
    pendings = len(Post.objects.all()) - len(user.read_set.all())
    return pendings


def set_context(request):
    current_user = request.user
    context = {}
    if current_user.is_authenticated:
        pendings = get_pendings(current_user.username)
        context['pendings'] = pendings
    return context

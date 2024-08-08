from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="دسته بندی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name="تگ")

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

    def __str__(self):
        return self.title


class Author(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="نام نویسنده")
    avatar = models.ImageField(upload_to="Author", blank=True, null=True, verbose_name="آواتار نویسنده")
    user = models.OneToOneField(User, related_name="authors", verbose_name=" یوزر", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return self.fullname


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان بلاگ")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Blog", blank=True, null=True, verbose_name="تصویر مطلب")
    categories = models.ManyToManyField(Category, related_name="posts", verbose_name="دسته بندی")
    tag = models.ManyToManyField(Tag, related_name="posts", verbose_name="تگ")
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE, verbose_name="نویسنده")
    text1 = models.TextField(verbose_name="متن بخش اول")
    quote = models.CharField(max_length=255, verbose_name="نقل قول", null=True, blank=True)
    text2 = models.TextField(verbose_name="متن بخش دوم", null=True, blank=True)
    popular = models.BooleanField(default=False, verbose_name="آیا پست برتر است؟")

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "بلاگ ها"
        ordering = ('-date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}|||{self.post}'


class SocialGroupSidebar(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام گروه شبکه های اجتماعی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "شبکه های اجتماعی"


class EmailSidebar(models.Model):
    social = models.ForeignKey(SocialGroupSidebar, on_delete=models.CASCADE, related_name="email")
    email = models.EmailField(verbose_name="پست الکترونیکی")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها"


class SocialSideBar(models.Model):
    social = models.ForeignKey(SocialGroupSidebar, on_delete=models.CASCADE, related_name="socials")
    name = models.CharField(max_length=255, verbose_name="نام شبکه اجتماعی")
    link = models.CharField(max_length=255, verbose_name="لینک شبکه اجتماعی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

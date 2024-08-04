from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام دسته بندی")
    slug = models.CharField(max_length=255, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان پروژه")
    image = models.ImageField(upload_to="Projects", blank=True, null=True, verbose_name="تصویر")
    category_slug = models.CharField(max_length=255, verbose_name="اسلاگ دسته بندی")
    category_name = models.CharField(max_length=255, verbose_name=" نام دسته بندی")
    date = models.CharField(max_length=255, verbose_name="تاریخ اجرای پروژه")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

    def __str__(self):
        return self.title


class Intro(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="intro")
    subtitle = models.CharField(max_length=100, verbose_name="زیرنویس")
    title = models.CharField(max_length=255, verbose_name="عنوان روی عکس")
    bgImage = models.ImageField(upload_to="Projects", blank=True, null=True, verbose_name="تصویر پس زمینه")

    class Meta:
        verbose_name = "معرفی کل پروژه"
        verbose_name_plural = "معرفی کلی پروژه"

    def __str__(self):
        return self.title


class Descriptions(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="description")
    title = models.CharField(max_length=255, verbose_name="عنوان توضیحات")
    subtitle = models.CharField(max_length=100, verbose_name="زیر نویس عنوان")
    content = models.TextField("متن توضیحات پروژه")

    class Meta:
        verbose_name = "توضیح"
        verbose_name_plural = "توضیجات"

    def __str__(self):
        return self.title


class Avatar(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to="Projects", blank=True, null=True, verbose_name="آواتار")
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    role = models.CharField(max_length=155, verbose_name="موقعیت شفلی")
    text = models.TextField(verbose_name="متن", blank=True, null=True)

    class Meta:
        verbose_name = "آواتار"
        verbose_name_plural = "آواتارها"

    def __str__(self):
        return self.name


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="details")
    label = models.CharField(max_length=255, verbose_name="لیبیل")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "جزئیات"
        verbose_name_plural = "جزئیات"

    def __str__(self):
        return self.label


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Projects", blank=True, null=True, verbose_name="عکس")
    alt = models.CharField(max_length=200)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.alt = self.project.title
        super(Gallery, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "نگاره"
        verbose_name_plural = "گالری"


class Resume(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="resume")
    title = models.CharField(max_length=255, verbose_name="عنوان رزومه")
    content = models.TextField(verbose_name="توضیح رزومه")
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    role = models.CharField(max_length=155, verbose_name="موقعیت شفلی")
    text = models.TextField(verbose_name="متن", blank=True, null=True)
    quote = models.TextField(verbose_name="متن", blank=True, null=True)
    author = models.CharField(max_length=255, verbose_name="نام نویسنده")

    def save(self, *args, **kwargs):
        self.name = self.project.avatar.name
        self.role = self.project.avatar.role
        self.text = self.project.avatar.text
        super(Resume, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه ها"

    def __str__(self):
        return self.title


class Benefit(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=100, verbose_name="زیرنویس")
    description = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "فایده"
        verbose_name_plural = "فایده ها"

    def __str__(self):
        return self.title


class BenefitItem(models.Model):
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, related_name="items")
    icon = models.ImageField(upload_to="Icon", blank=True, null=True, verbose_name="آیکون")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"

from django.db import models


class Team(models.Model):
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    name = models.CharField(max_length=255, verbose_name="نام")
    role = models.CharField(max_length=255, verbose_name="شغل")
    category_slug = models.CharField(max_length=255)
    fullImage = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر بزرک")
    description = models.TextField(verbose_name="توضیحات")
    signature = models.CharField(max_length=255, verbose_name="امضا")

    class Meta:
        verbose_name = "عضو"
        verbose_name_plural = "تیم"

    def __str__(self):
        return self.name


class Info(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="info")
    name = models.CharField(max_length=255, verbose_name="اطلاعات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "اطلاعات"


class Social(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="social")
    name = models.CharField(max_length=255, verbose_name="نام شبکه اجتماعی")
    link = models.CharField(max_length=255, verbose_name="لینک شبکه اجتماعی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"


class Avatar(models.Model):
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    name = models.CharField(max_length=250, verbose_name="نام و نام خانوادگی")
    subname = models.CharField(max_length=250, verbose_name="پوزیشن کاری")

    class Meta:
        verbose_name = "آواتار"
        verbose_name_plural = "آواتار ها"

    def __str__(self):
        return self.name


class Recruit(models.Model):
    title = models.CharField(max_length=110, verbose_name="عنوان")
    subtitle = models.CharField(max_length=55, verbose_name="زیرنویس")
    description = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, related_name="avatars", verbose_name="آواتار")

    class Meta:
        verbose_name = "استخدام"
        verbose_name_plural = "استخدامی ها"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=220, verbose_name="نام دسته بندی")
    slug = models.CharField(max_length=220, verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی شغلی"
        verbose_name_plural = "دسته بندی های شغلی"

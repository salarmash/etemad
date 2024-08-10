from django.db import models


class Hero(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"


class HeroItem(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="اسلاید")

    class Meta:
        verbose_name = " اسلاید"
        verbose_name_plural = " اسلاید ها"


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="Home", blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"


class Avatar(models.Model):
    about = models.OneToOneField(About, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to="Team", blank=True, null=True, verbose_name="تصویر")
    name = models.CharField(max_length=250, verbose_name="نام و نام خانوادگی")
    subName = models.CharField(max_length=250, verbose_name="پوزیشن کاری")

    class Meta:
        verbose_name = "آواتار"
        verbose_name_plural = "آواتار ها"

    def __str__(self):
        return self.name


class AboutItems(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="aboutItems")
    value = models.CharField(max_length=255, verbose_name="مقدار")
    valueAfter = models.CharField(max_length=20, verbose_name="مقدار پسین")
    label = models.CharField(max_length=255, verbose_name="لیبل")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"

    def __str__(self):
        return self.label


class Idea(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ایده"
        verbose_name_plural = "ایده ها"


class IdeaItem(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaItems")
    icon = models.ImageField(upload_to="Icons", blank=True, null=True, verbose_name="آیکون")
    label = models.CharField(max_length=255, verbose_name="لیبل")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    subtitle = models.CharField(max_length=200, verbose_name="زیر عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس ها"


class ServiceItem(models.Model):
    what_we_do = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceItems')
    title = models.CharField(max_length=200, verbose_name="عنوان")
    icon = models.ImageField(upload_to='Icons', blank=True, null=True, verbose_name="آیکن")
    num = models.CharField(max_length=7, verbose_name="تعداد")
    text = models.TextField("توضیحات")

    def __str__(self):
        return f"{self.num} {self.title}"

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class Advantage(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیرنویس")
    description = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "برتری"
        verbose_name_plural = "برتری ها"


class AdvantageItem(models.Model):
    our_advantages = models.ForeignKey(Advantage, on_delete=models.CASCADE, related_name='advantageItems')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class HowWeWork(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیرنویس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "روند ما"
        verbose_name_plural = "روند ما"


class WorkItem(models.Model):
    how_we_work = models.ForeignKey(HowWeWork, on_delete=models.CASCADE, related_name='workItems')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    icon = models.ImageField(upload_to='Icons', blank=True, null=True, verbose_name="آیکن")
    text = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"


class Core(models.Model):
    image = models.ImageField(upload_to='backgrounds/', blank=True, null=True, verbose_name="تصویر پس زمینه")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیرنویس")
    description = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "فلسفه "
        verbose_name_plural = "فلسفه ما"


class CoreItem(models.Model):
    our_core = models.ForeignKey(Core, on_delete=models.CASCADE, related_name='coreItems')
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"

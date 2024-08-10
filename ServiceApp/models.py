from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    icon = models.ImageField(upload_to="Icons", blank=True, null=True)
    short = models.TextField(verbose_name="توضیح کوتاه")

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="تصویر گالری")

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "گالری"


class Description(models.Model):
    service = models.OneToOneField(Service, related_name='descriptions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن")
    title2 = models.CharField(max_length=255, verbose_name="عنوانبخش مزایا اول")
    body2 = models.TextField("متن بخش مزایا اول")

    class Meta:
        verbose_name = "نوشتار"
        verbose_name_plural = "نوشتارها"

    def __str__(self):
        return self.title


class DescriptionList(models.Model):
    service = models.ForeignKey(Service, related_name='listItems', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="آیتم")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "برجستگی ها"


class Description2(models.Model):
    service = models.OneToOneField(Service, related_name='descriptions2', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن")
    title2 = models.CharField(max_length=255, verbose_name="عنوانبخش مزایا اول")
    body2 = models.TextField("متن بخش مزایا اول")

    class Meta:
        verbose_name = "نوشتار دوم"
        verbose_name_plural = "نوشتارهای بخش دوم"

    def __str__(self):
        return self.title


class SideBar(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام کل ساید بار")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "سایدبار مادر"
        verbose_name_plural = "سایدبار مادر"


class SideBarItem(models.Model):
    sidebar = models.ForeignKey(SideBar, on_delete=models.CASCADE, related_name="SideItems",
                                verbose_name="عنوان سایدبار مادر")
    title = models.CharField(max_length=255, verbose_name="عنوان زیر مجموعه ساید بار")

    class Meta:
        verbose_name = "سایدبار"
        verbose_name_plural = "سایدبار"

    def __str__(self):
        return self.title


class SideBarContent(models.Model):
    item = models.ForeignKey(SideBarItem, related_name='contents', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.label


class SideBarCounter(models.Model):
    sidebar = models.ForeignKey(SideBar, on_delete=models.CASCADE, related_name="SideCounter",
                                verbose_name="عنوان سایدبار مادر")
    label1 = models.CharField(max_length=255, verbose_name="عنوان شمارنده اول")
    counter1 = models.IntegerField(default=0, blank=True, null=True, verbose_name="شمارنده اول")
    label2 = models.CharField(max_length=255, verbose_name="عنوان شمارنده دوم")
    counter2 = models.IntegerField(default=0, blank=True, null=True, verbose_name="شمارنده دوم")
    label3 = models.CharField(max_length=255, verbose_name="عنوان شمارنده سوم")
    counter3 = models.IntegerField(default=0, blank=True, null=True, verbose_name="شمارنده سوم")
    label4 = models.CharField(max_length=255, verbose_name="عنوان شمارنده چهارم")
    counter4 = models.IntegerField(default=0, blank=True, null=True, verbose_name="شمارنده چهارم")

    def __str__(self):
        return self.sidebar.name

    class Meta:
        verbose_name = "شمارنذه"
        verbose_name_plural = "شمارنذه ها"


class FAQSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان ")
    subtitle = models.CharField(max_length=255, verbose_name="زیرنویس")

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.title


class FAQItem(models.Model):
    faq = models.ForeignKey(FAQSection, related_name='faqItems', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, verbose_name="سوال")
    content = models.TextField(verbose_name="جواب سوال")

    def __str__(self):
        return self.label


class VisionsSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان بخش ویژگی ها")
    subtitle = models.CharField(max_length=255, verbose_name="زیرعنوان بخش ویژگی ها")

    class Meta:
        verbose_name = "اهداف ما"
        verbose_name_plural = "اهداف ما"

    def __str__(self):
        return self.title


class VisionItem(models.Model):
    vision_section = models.ForeignKey(VisionsSection, related_name='VItems', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="عنوان")
    icon = models.ImageField(upload_to="Icons", blank=True, null=True, verbose_name="آیکون")
    text = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "آیتم هدف"
        verbose_name_plural = "لیست اهداف"

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    text = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

    def __str__(self):
        return self.title


class FeatureItem(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="featureItems")
    list_item = models.CharField(max_length=255, verbose_name="آیتم های برجسته")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "لیست ویژگی ها"

    def __str__(self):
        return self.list_item


class AboutSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image_url = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="تصویر")
    image_alt = models.CharField(max_length=255, verbose_name="نام عکس")
    avatar_image = models.ImageField(upload_to="Service", blank=True, null=True, verbose_name="آواتار")
    avatar_name = models.CharField(max_length=255, verbose_name="نام آواتار")
    avatar_subname = models.CharField(max_length=255, verbose_name="زیر نام آواتار")

    def save(self, *args, **kwargs):
        self.image_alt = self.title
        self.avatar_name = self.title
        super(AboutSection, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "معرفی"
        verbose_name_plural = "معرفی ما"

    def __str__(self):
        return self.title


class AboutList(models.Model):
    about = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="aboutLists")
    list = models.CharField(max_length=255, verbose_name="لیست")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "لیست پروموشن ها"

    def __str__(self):
        return self.list


class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    subtitle = models.CharField(max_length=155, verbose_name="زیر عنوان")

    class Meta:
        verbose_name = "راه ارتباطی"
        verbose_name_plural = "راه های ارتباطی"

    def __str__(self):
        return self.title


class ContactPhone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="phones")
    phone = models.CharField(max_length=12, verbose_name="تلفن")

    class Meta:
        verbose_name = "تلفن"
        verbose_name_plural = "تلفن ها"

    def __str__(self):
        return self.phone


class ContactEmail(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="emails")
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها"

    def __str__(self):
        return self.email


class ContactAddress(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField(verbose_name="آدرس")

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"

    def __str__(self):
        return self.address


from django.db import models

# Create your models here.

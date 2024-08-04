from django.db import models


class Award(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="متن سکشن")
    image = models.ImageField(upload_to="About", null=True, blank=True, verbose_name="تصویر سکشن")

    class Meta:
        verbose_name = "سکشن"
        verbose_name_plural = "جوایز"

    def __str__(self):
        return self.title


class AwardItems(models.Model):
    award = models.ForeignKey(Award, models.CASCADE, "items", verbose_name="جایزه")
    title = models.CharField(max_length=100, verbose_name="عنوان تقدیرنامه")
    year = models.CharField(max_length=4, verbose_name="سال دریافت تقدیرنامه")
    image = models.ImageField(upload_to="About", null=True, blank=True, verbose_name="تصویر تقدیرنامه")

    class Meta:
        verbose_name = "تقدیرنامه"
        verbose_name_plural = "تقدیرنامه ها"


class Testimonial(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    subtitle = models.CharField(max_length=220, verbose_name="زیر عنوان")

    class Meta:
        verbose_name = "سکشن"
        verbose_name_plural = "رضایت مشتریان"

    def __str__(self):
        return self.title


class TestItems(models.Model):
    testimonial = models.ForeignKey(Testimonial, on_delete=models.CASCADE, related_name="testItems")
    name = models.CharField(max_length=100, verbose_name="نام مشتری")
    image = models.ImageField(upload_to="About", null=True, blank=True, verbose_name="تصویر مشتری")
    role = models.CharField(max_length=100, verbose_name="شغل مشتری")
    text = models.TextField(verbose_name="متن نظر")

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="serviceItems")
    title = models.CharField(max_length=100, verbose_name="عنوان")
    text = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتمها"

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(verbose_name="پست الکترونیکی")
    phone = models.CharField(max_length=12, verbose_name="تلفن")

    class Meta:
        verbose_name = "ارتباط با ما"
        verbose_name_plural = "ارتباط با ما"

    def __str__(self):
        return f"{self.email} -- {self.phone}"


class Signature(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    subname = models.CharField(max_length=100, verbose_name="نوشتار دوم")
    text = models.CharField(max_length=100, verbose_name="نوشتار امضا")

    class Meta:
        verbose_name = "امضا"
        verbose_name_plural = "امضاها"

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=200, verbose_name=" عنوان")
    subtitle = models.CharField(max_length=200, verbose_name="زیر عنوان")
    description = models.TextField(verbose_name="توضیحات")
    signature = models.OneToOneField(Signature, on_delete=models.CASCADE, related_name="signature",
                                     verbose_name=" امضا")

    class Meta:
        verbose_name = "اطلاعات شرکت"
        verbose_name_plural = "اطلاعات شرکت"

    def __str__(self):
        return self.title


class Company2(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=100)
    subtitle = models.CharField(verbose_name="زیرنویس", max_length=50)
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات بیشتر"

    def __str__(self):
        return self.title


class CompanyImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="About", null=True, blank=True, verbose_name="تصویر")

    def __str__(self):
        return self.company.title


class Company2Image(models.Model):
    company2 = models.ForeignKey(Company2, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="About", null=True, blank=True, verbose_name="تصویر")

    def __str__(self):
        return self.company2.title


class AboutExtra(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام گروه")

    class Meta:
        verbose_name = "شرکت همکار"
        verbose_name_plural = "شرکت های همکار"


class AllProcess(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    subtitle = models.CharField(max_length=255, verbose_name="زیرنویس")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "روند کاری"
        verbose_name_plural = "روند کاری"


class Group(models.Model):
    allProcess = models.ForeignKey(AllProcess, on_delete=models.CASCADE, related_name="group")
    name = models.CharField(max_length=200, verbose_name="گروه روندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "گروه روندی"
        verbose_name_plural = "گروه های روندی"


class Process(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="process")
    title = models.CharField(max_length=100, verbose_name="عنوان")
    text = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"

    def __str__(self):
        return f" {self.title}"


class Partner(models.Model):
    about = models.ForeignKey(AboutExtra, on_delete=models.CASCADE, related_name="partner")
    title = models.CharField(max_length=100, verbose_name="شرکت همکار")
    image = models.ImageField(upload_to="About", blank=True, null=True)

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها"

    def __str__(self):
        return self.title

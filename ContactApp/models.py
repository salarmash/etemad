from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    content = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "راه ارتباطی"
        verbose_name_plural = "تماس با ما"

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


class ContactForm(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    tel = models.CharField(max_length=12, verbose_name="تلفن")
    fullName = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    message = models.TextField(verbose_name="متن در خواست")

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"

    def __str__(self):
        return f"{self.fullName}--{self.tel}--{self.email}"

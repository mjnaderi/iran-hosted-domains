<div dir=rtl>

#  دامنه‌های میزبانی شده در ایران


بسیاری از سرویس ها و دامنه های خارج از ایران سانسور و مسدود شده اند و ما باید برای دسترسی به آنها از VPN و proxy هایی با امنیت بالا استفاده کنیم، جدای از این مسئله چون ما از پراکسی استفاده میکنیم و ip ما ایران نیست دسترسی به بعضی سرویس های ایرانی مسدود میشود، برای دور زدن این سرویس ها ما لیستی از دامنه و ip جمع کردیم که دیگر نیاز به قطع کردن vpn برای دسترسی به سرویس داخلی نباشد

## مشکلات VPN و پروکسی

مشکلات زیر هنگام بازدید برخی از وب‌سایت‌های داخلی از طریق IP خارجی بوجود می‌آید:

- برای دسترسی ممکن است کاربر را مجبور به داشتن IP داخلی کنند.
- برخی از ISP ها درصورت مصرف پهنای باند داخلی تخفیف ۵۰ درصد اعمال می‌کنند.
- برخی از سایت‌ها ممکن است سرعت و پهنای باند کاربران خارجی را محدود کنند


## روش استفاده

بسته به اینکه از کدام کلاینت استفاده می‌کنید، ممکن است متفاوت باشد.  لیست دامنه‌ها و فایل‌های مربوط را می‌توانید از [این صفحه](https://github.com/SamadiPour/iran-hosted-domains/releases) دریافت کنید.  
برای سیستم routing بهتر در کلاینت‌های v2ray شما می‌توانید پارامتر `Domain Resolution Strategy` را به `IPIfNonMatch` تغییر دهید. [اطلاعات بیشتر](https://www.v2ray.com/en/configuration/routing.html) 


### [Qv2ray](https://github.com/Qv2ray/Qv2ray)


شما می‌توانید فایل qv2ray_schema.json را در [این صفحه](https://github.com/SamadiPour/iran-hosted-domains/releases) پیدا کنید.
  
1. فایل را دانلود کنید.
2. در بخش `preferences` بر روی `Advanced Route Settings` کلیک کنید.
3. در پایین صفحه، بر روی `import schema...` کلیک کنید.
4. فایل qv2ray_schema.json دانلود شده را انتخاب کنید.
5. در کادر باز شده بر روی yes کلیک کنید.
6. بر روی OK کلیک کنید.

![image](https://user-images.githubusercontent.com/24422125/115480663-397d3880-a260-11eb-88db-d3d7f8074767.png)

### .dat file

این فایل در تمامی کلاینت‌های v2ray
  v2fly و xray قابل استفاده است.

1. فایل `iran.dat` را از [این صفحه](https://github.com/SamadiPour/iran-hosted-domains/releases) دانلود کنید.
2. فایل را در کلاینت خود کپی و یا وارد کنید.  
  به عنوان مثال:
    - v2ray macOS: `/usr/local/share/v2ray`
    ![image](https://user-images.githubusercontent.com/24422125/123522516-f2ce1380-d6d2-11eb-971f-0176f6e5b8ec.png)

3. قوانین مناسب را اضافه کنید
    - `ext:iran.dat:ir`
    - `ext:iran.dat:other`
    - `ext:iran.dat:ads`

4. اتصال خود را قطع و وصل کنید.
  
### [SagerNet](https://github.com/SagerNet/SagerNet)
1. فایل `iran.dat` را از [این صفحه](https://github.com/SamadiPour/iran-hosted-domains/releases) دانلود کنید.
2. فایل را از طریق `Route -> Three dots -> Manage Route Assets`  به کلاینت اضافه کنید.
<p align="center">
  <img alt="sagernet" src="https://user-images.githubusercontent.com/24422125/123522689-1cd40580-d6d4-11eb-90c1-a0341927e283.jpg">
</p>

3.  از بخش  `Route -> Create Route` قوانین زیر را اضافه کنید:   
</div>  

- Block Ads:
  - domain: `geosite:category-ads-all`
  - outbound: `Block`
- Block Iran Ads:
  - domain: `ext:iran.dat:ads`
  - outbound: `Block`
- Bypass Iran .ir Domains:ا
  - domain: `regexp:.+\.ir$`
  - outbound: `Bypass`
- Bypass Iran non .ir Domains:
  - domain: `ext:iran.dat:other`
  - outbound: `Bypass`
- Bypass Iran geoip:
  - ip: `geoip:ir`
  - outbound: `Bypass`

<div dir=rtl>  

> برای مشاهده‌ی اسکرین شات از قوانین بالا [اینجا کلیک کنید](https://imgur.com/a/SEq1Bvg).

4. اتصال خود را قطع و وصل کنید.

### [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

1. فایل `shadowrocket.conf` را دانلود کنید.
2. در اپلیکیشن بر روی `Import From Cloud` کلیک کرده و فایل مربوط را اضافه کنید.

<p align="center">
  <img alt="shadowrocket" src="https://user-images.githubusercontent.com/24422125/124380820-3678dc80-dcd4-11eb-8f59-96fb619d5710.png">
</p>

3. در نهایت، بر روی `shadowrocket.conf`کلیک کرده و `Use Config` را انتخاب کنید.

<p align="center">
  <img alt="shadowrocket" src="https://user-images.githubusercontent.com/24422125/124380847-5d371300-dcd4-11eb-8274-aa72d470357f.png">
</p>


## فایل‌ها

- **iran.dat:** شامل `ir_domains.txt` و `other_domains.txt`.
- **ir_domains.txt:** شامل وب‌سایت‌هایی با دامنه‌ی .ir.
- **other_domains.txt:** شامل وب‌سایت‌های میزبانی شده در ایران که دامنه‌ی آنها .ir نیست.
- **qv2ray_schema.json:** فایل قابل استفاده در کلاینت [Qv2ray](https://github.com/Qv2ray/Qv2ray).
- **shadowrocket.conf:** فایل قابل استفاده در کلاینت [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118).

## منابع

- دامنه‌های ایران:
  - [سازمان فناوری اطلاعات ایران](https://g2b.ito.gov.ir/index.php/site/list_ip)
  - [سامانه مدیریت اینترنت مشتریان شرکت مخابرات ایران](https://adsl.tci.ir/panel/sites)
  - [لیست شخصی](https://github.com/SamadiPour/iran-hosted-domains/blob/main/src/data/custom_domains.py)
- تبلیغات:
  - [adblock-iran](https://github.com/farrokhi/adblock-iran)

اگر شما منابع دیکری می‌شناسید، و یا وب‌سایتی پیدا کرده‌اید که اینجا نیست لطفا یک
[issue](https://github.com/SamadiPour/iran-hosted-domains/issues) باز کنید و یا فایل `custom_domains.py` را تغییر داده و PR ایجاد کنید.

## چگونه کار می کند؟

به وسیله‌ی Github Action یک اسکریپت پایتون اجرا شده و از طریق منابع بالا فایل‌های مربوطه در صفحه‌ی رلیز ایجاد می‌شود.

</div>  

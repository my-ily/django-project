#  🧠 مشروع تطبيبقي في Django 
<img width="2028" height="1639" alt="image" src="https://github.com/user-attachments/assets/4eebe04a-cbe5-4fa9-b9cf-13dd89862bf9" />

## 📌 نظرة عامة
هذا المشروع مبني باستخدام إطار عمل **Django (النسخة 5+)** :
*
- 📦 **عرض المنتجات مثل الهواتف (Mobile Product Showcase)**
- 🛠 **لوحة تحكم للمشرف عبر Django Admin**
- 🌐 **نشر احترافي على منصة Heroku**

> 💡 الهدف من المشروع هو التدريب العملي على تطوير ونشر مشروع ويب احترافي باستخدام Django مع ربطه بقاعدة بيانات PostgreSQL.

--
## 💼 مكونات المشروع

| التطبيق (App)  | الوظيفة |
|----------------|----------|
| mobile         | إدارة وعرض قائمة من المنتجات مثل الهواتف، مع دعم تحميل الصور |
| admin          | لوحة تحكم لإدارة المستخدمين والبيانات |

---

## 📸 واجهات المشروع
- صفحة رئيسية تحتوي على روابط لجميع التطبيقات
- صفحة **المنتجات** لعرض قائمة المنتجات مع الصور والأسعارة
- تسجيل دخول المشرف إلى لوحة **Django Admin**

---

## ⚙️ المتطلبات
- Python 3.13
- Django 5.x
- psycopg2
- gunicorn
- dj-database-url
- whitenoise

---

## 🚀 طريقة التشغيل (محليًا)

1. **استنساخ المشروع:**
   ```bash
   git clone https://github.com/my-ily/django-project.git
   cd django-project
   ```

2. **إنشاء بيئة افتراضية:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **تثبيت المتطلبات:**
   ```bash
   pip install -r requirements.txt
   ```

4. **الترحيل وإنشاء قاعدة البيانات:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **تشغيل السيرفر المحلي:**
   ```bash
   python manage.py runserver
   ```

6. **فتح المشروع:**
   👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🖼 مثال لعرض المنتجات

| اسم المنتج | صورة | السعر |
|------------|-------|-------|
| iPhone 14  | ✅    | 4000 SAR |
| Galaxy S22 | ✅    | 3200 SAR |

---

## ☁️ طريقة النشر على Heroku

1. **إنشاء تطبيق على Heroku:**
   ```bash
   heroku create myapp-name
   ```

2. **رفع المشروع:**
   ```bash
   git push heroku main
   ```

3. **ترحيل القاعدة:**
   ```bash
   heroku run python manage.py migrate
   ```

4. **فتح التطبيق:**
   ```bash
   heroku open
   ```

---

## 🗂 هيكل المجلدات

```
project-dj/
├── Myproject/              # ملفات الإعداد الرئيسية لـ Django
├── converter/              # تطبيق تحويل العملات
├── mobile/                 # عرض المنتجات
├── templates/              # القوالب العامة
├── static/                 # ملفات CSS/JS
├── media/                  # صور المنتجات
├── manage.py
├── requirements.txt
├── Procfile                # إعداد Heroku
```

---

## ✅ نقاط قوة المشروع
- تقسيم واضح للتطبيقات
- استخدام Django ORM للتعامل مع قواعد البيانات
- رفع الصور وربطها بالنماذج
- نشر المشروع أونلاين باستخدام Heroku
- متوافق مع PostgreSQL

---

  ```env
  DEBUG=False
  ALLOWED_HOSTS=*
  SECRET_KEY=your-secret-key
  ```
.

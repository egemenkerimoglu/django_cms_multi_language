
# Django Çok Dilli CMS Projesi

Bu proje, Django kullanılarak oluşturulmuş bir web uygulamasıdır. Aşağıda, projenin yerel geliştirme ortamında nasıl kurulacağı ve yönetileceği adımları bulabilirsiniz.

## Çalıştırma Adımları

1. Proje klasörünü Visual Studio Code'da açın.

2. Sanal ortamı oluşturun:

    ```bash
    python -m pip install --user virtualenv
    virtualenv proje_adi_venv
    ```

3. Sanal ortamı etkinleştirin:

    - Windows:

        ```bash
        .\proje_adi_venv\Scripts\activate
        ```

    - Linux/Mac:

        ```bash
        source proje_adi_venv/bin/activate
        ```

4. Django'yu sanal ortama kurun:

    ```bash
    pip install Django
    ```

5. Sanal ortamdaki kurulu paketleri görüntüleyin:

    ```bash
    pip freeze
    ```

6. Gerekli paketleri `requirements.txt` dosyasına kaydedin:

    ```bash
    pip freeze > requirements.txt
    ```

7. Eğer projeyi başka bir ortamda kurmak isterseniz, sanal ortamı oluşturun ve aşağıdaki komutu kullanarak paketleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

## Notlar

- Projenin geliştirme sunucusunu başlatmak için:

    ```bash
    python manage.py runserver
    ```

- Daha fazla bilgi için [Django Dokümantasyonu](https://docs.djangoproject.com/)nu inceleyebilirsiniz.

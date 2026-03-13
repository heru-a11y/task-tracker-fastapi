# Task Tracker FastAPI

Sistem pengurusan tugasan (Task Tracker) ringkas yang dibina menggunakan FastAPI dan SQLAlchemy dengan sokongan pangkalan data PostgreSQL.

## Prasyarat

Sebelum memulakan, pastikan anda mempunyai perkara berikut:
* Python 3.8 ke atas
* Pangkalan data PostgreSQL yang sedang berjalan
* `pip` (pengurus pakej Python)

## Pemasangan

1.  **Klon atau muat turun kod sumber projek ini.**

2.  **Cipta persekitaran maya (Virtual Environment):**
    ```bash
    python -m venv .venv
    ```

3.  **Aktifkan persekitaran maya:**
    * Windows: `.venv\Scripts\activate`
    * macOS/Linux: `source .venv/bin/activate`

4.  **Pasang dependensi yang diperlukan:**
    ```bash
    pip install -r requirements.txt
    ```

## Konfigurasi Pangkalan Data

Projek ini menggunakan PostgreSQL sebagai pangkalan data utama. Secara lalai, aplikasi akan mencari URL pangkalan data berikut:
`postgresql://user:password@localhost/tasktracker`

Anda boleh menukar konfigurasi ini melalui pembolehubah persekitaran (Environment Variable) `DATABASE_URL`. Sila pastikan anda telah mencipta pangkalan data bernama `tasktracker` dalam PostgreSQL anda sebelum menjalankan aplikasi.

## Cara Menjalankan Aplikasi (Mode Pembangunan)

Jika anda menggunakan FastAPI versi terbaru yang menyertakan antaramuka baris perintah (CLI) `fastapi`, anda boleh menggunakan perintah berikut untuk menjalankan pelayan dalam mod pembangunan (development mode):

```bash
fastapi dev

# ♿ Web Accessibility (a11y) Automation Testing

Proyek ini merupakan implementasi pengujian aksesibilitas otomatis yang mengintegrasikan mesin standar industri **Axe-Core** dengan **Playwright**. Tujuannya adalah untuk memastikan aplikasi web mematuhi standar aksesibilitas global (WCAG / ADA) dan dapat digunakan secara inklusif oleh semua pengguna, termasuk penyandang disabilitas.

## 🌟 Mengapa Proyek Ini Penting?
Aksesibilitas web (a11y) bukan lagi sekadar fitur tambahan, melainkan persyaratan hukum di banyak negara maju dan kewajiban moral bagi perusahaan teknologi global. 
*Framework* ini mengotomatiskan proses audit UI yang membosankan—seperti mendeteksi kontras warna yang buruk, ketiadaan label ARIA, atau struktur HTML yang tidak ramah *Screen Reader*—sehingga isu dapat diperbaiki jauh sebelum produk dirilis ke publik.

## 🚀 Fitur Utama (Key Features)
*   **Axe-Core Integration:** Menginjeksi mesin analitik aksesibilitas Axe-Core secara mulus ke dalam lingkungan Playwright.
*   **Automated Violation Reporting:** Menghasilkan laporan terperinci mengenai setiap pelanggaran HTML, termasuk tingkat keparahan (*impact*), deksripsi teknis, dan tautan solusi (*helpUrl*).
*   **Severity-Based Assertion:** Skrip dirancang untuk menggagalkan *pipeline* (FAILED) secara otomatis apabila ditemukan pelanggaran aksesibilitas dengan tingkat 'kritis' (*Critical Impact*).

## 🛠️ Teknologi yang Digunakan (Tech Stack)
*   **Bahasa Pemrograman:** Python 3
*   **Test Runner:** Pytest
*   **Automation Engine:** Playwright (Sync API)
*   **Accessibility Engine:** Axe-Core (via `axe-playwright-python`)

## 📁 Struktur Arsitektur
```text
qa-accessibility-testing/
├── test_accessibility.py  # Skrip utama injeksi Axe-Core & validasi pelanggaran
├── README.md
└── requirements.txt       # (Berisi: pytest, playwright, axe-playwright-python)

🚀 Cara Menjalankan Proyek Secara Lokal
1. Persiapan Environment
Instal seluruh dependensi yang dibutuhkan:

Bash
pip install pytest playwright axe-playwright-python
playwright install chromium
2. Eksekusi Pemindaian Aksesibilitas
Jalankan perintah ini untuk memulai audit secara otomatis:

Bash
python -m pytest -s -v test_accessibility.py
Hasil yang Diharapkan:
Sistem akan memindai Document Object Model (DOM) pada halaman yang dituju dan mencetak daftar pelanggaran kelemahan aksesibilitas di terminal, lengkap dengan panduan perbaikannya untuk diserahkan kepada tim Frontend Developer.
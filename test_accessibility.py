import pytest
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe

def test_aksesibiitas_website(page:Page):
    # 1. Buka website yang ingin diuji (Kita pakai Saucedemo)
    print("\n membuka website soucedemo")
    page.goto("https://www.saucedemo.com/")

    # 2. Inisialisasi dan jalankan mesin pemindai Axe-Core
    print("[INFO] Meginjeksi dan Menjalaknkan mesin axe-core ke dalam halaman")
    results = Axe().run(page)

    # 3. Ambil daftar pelanggaran (violations) dari hasil pemindaian
    pelanggaran = results.response.get("violations", [])

    print(f"\n[HASIL PEMINDAIAN] Ditemukan {len(pelanggaran)} jenis isu aksesibilitas pada halaman ini:")

    # 4. Cetak detail pelanggaran agar Developer tahu apa yang harus diperbaiki
    for index, isu in enumerate(pelanggaran, start=1):
        print(f"\n isu ke-{index}:{isu.get('id')}")
        print(f"Deskripsi : {isu.get('description')}")
        print(f"Dampak    : {isu.get('impact').upper()} (tingkat keparahan)")
        print(f"Bantuan   : {isu.get('helpUrl')}")
        print("-" * 50)

    # 5. Validasi: Skrip akan digagalkan (FAILED) jika ada pelanggaran tingkat 'critical' (Kritis)
    # Kita kumpulkan isu yang dampaknya 'critical'
    isu_kritis = [isu for isu in pelanggaran if isu.get('impact') == 'critical']
    assert len(isu_kritis) == 0, f"Bahaya Ditemukan {len(isu_kritis)} isu aksesibilitas tingkat KRITIS websie bisa dituntut"

    print("\n[SUKSES] Halaman ini bebas dari pelanggaran aksesibilitas tingkat Kritis.")
# Preview tautan

Halaman utama menyertakan Open Graph dan Twitter Card: foto jas navy, nama,
jabatan, dan deskripsi HR/HRGA. Metadata tersedia di HTML statis sehingga
tidak bergantung pada JavaScript atau pilihan bahasa di browser.

Sebelum build produksi, atur environment variable `PUBLIC_SITE_URL` ke URL
HTTPS publik website (domain asli dari penyedia hosting). Lalu jalankan
`npm run build`. Astro memakai nilai ini untuk URL absolut gambar dan halaman.

Tanpa URL publik, preview WhatsApp/LinkedIn belum bisa diverifikasi.
Localhost hanya dapat diakses dari komputer sendiri. Setelah deploy, pastikan
halaman dan URL `og:image` dapat dibuka tanpa login. Platform berbagi bisa
menyimpan cache preview lama. Gunakan LinkedIn Post Inspector untuk memeriksa
preview yang diterima crawler setelah domain tersedia.

Pilihan ID/EN mengubah teks di browser; preview berbagi tetap berbahasa Indonesia.

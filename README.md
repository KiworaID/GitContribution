# Auto GitHub Commit

Program ini akan membuat commit otomatis ke GitHub untuk menjaga contribution graph tetap aktif.

## Fitur
- Auto create repository
- Auto commit setiap hari (3x sehari)
- Auto delete repository lama (setiap minggu)
- Contribution graph selalu aktif

## Cara Penggunaan

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Buat file `.env` dan isi dengan GitHub token Anda:
```
GITHUB_TOKEN=your_github_token_here
```

3. Jalankan program:
```bash
python auto_commit.py
```

## Jadwal
- Commit otomatis: 10:00, 15:00, dan 20:00 setiap hari
- Pembersihan repository: Setiap hari Minggu pukul 23:00

## Catatan
- Pastikan Anda telah membuat GitHub Personal Access Token dengan izin yang sesuai
- Program akan membuat repository baru untuk setiap commit
- Repository lama akan dihapus secara otomatis setiap minggu 
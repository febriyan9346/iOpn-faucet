# IOPN Faucet Bot dengan 2captcha

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![2captcha](https://img.shields.io/badge/2captcha-Supported-green.svg)](https://2captcha.com)

Bot Python untuk otomatis claim faucet IOPN menggunakan layanan 2captcha untuk menyelesaikan reCAPTCHA v2.

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/febriyan9346/iOpn-faucet.git
cd iOpn-faucet

# Install dependencies
pip3 install -r requirements.txt

# Setup config
cp 2captcha.txt.example 2captcha.txt
cp address.txt.example address.txt

# Edit config files dengan data Anda
nano 2captcha.txt    # masukkan API key 2captcha
nano address.txt     # masukkan wallet address

# Run bot
python3 bot.py
```

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [Informasi reCAPTCHA](#informasi-recaptcha)
- [Fitur](#fitur)
- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Cara Menggunakan](#cara-menggunakan)
- [Setup untuk GitHub](#setup-untuk-github)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Informasi reCAPTCHA

- **Site Key**: `6Ld1uvorAAAAAKwGWoEHDYIq_yo3dSvshmNQ9ykF`
- **Website URL**: `https://faucet.iopn.tech`
- **API Endpoint**: `https://faucet.iopn.tech/api/faucet/claim`

## ✨ Fitur

- ✅ Solve reCAPTCHA v2 otomatis menggunakan 2captcha
- ✅ **Auto-claim setiap 24 jam** (loop otomatis) 🔄
- ✅ **Retry otomatis jika gagal** (tunggu 1 jam)
- ✅ Membaca API key dari file `2captcha.txt`
- ✅ Membaca wallet address dari file `address.txt`
- ✅ Error handling lengkap
- ✅ Logging informatif dengan status realtime
- ✅ Support multiple wallet addresses
- ✅ **Ctrl+C untuk stop bot dengan aman**
- ✅ Mudah dikustomisasi dan di-maintain
- ✅ Siap untuk di-upload ke GitHub dengan security terjamin

## Prasyarat

1. Python 3.x terinstall
2. API key dari 2captcha (daftar di https://2captcha.com)
3. Saldo cukup di akun 2captcha Anda
4. Wallet address IOPN

## Instalasi

### 📥 Clone Repository

```bash
git clone https://github.com/febriyan9346/iOpn-faucet.git
cd iOpn-faucet
```

### 📦 Install Dependencies

Install library yang diperlukan:

```bash
pip install -r requirements.txt
```

atau

```bash
pip3 install -r requirements.txt
```

### ⚙️ Setup Configuration

1. Copy file template:

```bash
cp 2captcha.txt.example 2captcha.txt
cp address.txt.example address.txt
```

2. Edit file `2captcha.txt` dan masukkan API key 2captcha Anda:

```bash
nano 2captcha.txt
```

Ganti `YOUR_2CAPTCHA_API_KEY_HERE` dengan API key asli Anda dari 2captcha.

3. Edit file `address.txt` dan masukkan wallet address Anda:

```bash
nano address.txt
```

Ganti `0xYOUR_WALLET_ADDRESS_HERE` dengan wallet address asli Anda.

## Cara Menggunakan

### Method 1: Run langsung (Recommended)

```bash
python3 bot.py
```

**Bot akan:**
- ✅ Membaca API key dari `2captcha.txt`
- ✅ Membaca wallet address dari `address.txt`
- ✅ Claim faucet pertama kali
- 🔄 **Auto-claim setiap 24 jam** (loop otomatis!)
- ⏰ Retry setiap 1 jam jika gagal

**Bot jalan terus-menerus!** Tekan `Ctrl+C` untuk menghentikan.

### Method 2: Run di Background (VPS/Server)

#### Menggunakan screen:
```bash
# Install screen
sudo apt-get install screen

# Buat session
screen -S iopn-bot

# Run bot
python3 bot.py

# Detach: Ctrl+A lalu D
# Bot tetap jalan!

# Attach kembali
screen -r iopn-bot
```

#### Menggunakan nohup:
```bash
nohup python3 bot.py > bot.log 2>&1 &

# Check log
tail -f bot.log
```

**📚 Panduan lengkap auto-claim:** Lihat [AUTO_CLAIM_GUIDE.md](AUTO_CLAIM_GUIDE.md)

### Method 3: Edit kode (Optional)

Jika Anda ingin menggunakan wallet address berbeda tanpa mengubah file `address.txt`, Anda bisa edit langsung di fungsi `main()` di file `bot.py`:

```python
def main():
    api_key = read_api_key("2captcha.txt")
    
    if not api_key:
        print("[!] Tidak dapat membaca API key.")
        return
    
    # Hardcode wallet address di sini (optional)
    wallet_address = "0xYOUR_CUSTOM_WALLET_ADDRESS"
    
    bot = FaucetBot(api_key, wallet_address)
    bot.run()
```

---

## 🐙 Setup untuk GitHub

### Jika Anda Mau Upload ke GitHub:

Project ini **AMAN** untuk di-upload ke GitHub karena sudah dilengkapi dengan:

1. **`.gitignore`** - Mencegah file sensitif ter-commit
2. **File example** - Template untuk user lain
3. **Security documentation** - Panduan keamanan lengkap

### Quick Start - Upload ke GitHub:

```bash
# 1. Initialize git
git init

# 2. Add files
git add .

# 3. Commit
git commit -m "Initial commit: IOPN Faucet Bot"

# 4. Add remote (ganti dengan URL repo Anda)
git remote add origin https://github.com/USERNAME/iopn-faucet-bot.git

# 5. Push
git branch -M main
git push -u origin main
```

**📚 Panduan lengkap**: Lihat [SETUP_GUIDE.md](SETUP_GUIDE.md) untuk instruksi detail.

### Untuk User yang Clone dari GitHub:

```bash
# 1. Clone repository
git clone https://github.com/USERNAME/iopn-faucet-bot.git
cd iopn-faucet-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup config files
cp 2captcha.txt.example 2captcha.txt
cp address.txt.example address.txt

# 4. Edit dengan data Anda
nano 2captcha.txt  # masukkan API key
nano address.txt   # masukkan wallet address

# 5. Run bot
python3 bot.py
```

---

## Struktur File

```
iopn-faucet-bot/
│
├── bot.py              # File utama bot
├── README.md                  # Dokumentasi utama
├── SETUP_GUIDE.md            # Panduan setup GitHub (detail)
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules (security)
│
├── 2captcha.txt.example     # Template API key (untuk GitHub)
├── address.txt.example      # Template wallet address (untuk GitHub)
│
├── 2captcha.txt             # API key asli (JANGAN di-commit!)
└── address.txt              # Wallet address asli (JANGAN di-commit!)
```

**Note:** File `2captcha.txt` dan `address.txt` (tanpa `.example`) **TIDAK akan ter-upload** ke GitHub karena sudah di-protect oleh `.gitignore`.

## Cara Kerja Bot

1. **Membaca API Key**: Bot membaca API key 2captcha dari file `2captcha.txt`
2. **Submit Captcha**: Bot mengirim task reCAPTCHA ke 2captcha service
3. **Tunggu Hasil**: Bot menunggu captcha diselesaikan (sekitar 20-60 detik)
4. **Ambil Token**: Bot mengambil token captcha yang sudah diselesaikan
5. **Claim Faucet**: Bot menggunakan token untuk claim faucet melalui API

## Contoh Output

```
[+] API Key: f8a3b2c1e5...9d7f6e4a2b
[+] Wallet Address: 0x2bf1bbfa2bbc07e47290385936ab27a0c697fb5b

============================================================
IOPN Faucet Bot dengan 2captcha
============================================================
Wallet Address: 0x2bf1bbfa2bbc07e47290385936ab27a0c697fb5b
Website: https://faucet.iopn.tech
============================================================
[*] Mengirim captcha ke 2captcha...
[+] Captcha terkirim. Task ID: 12345678
[*] Menunggu captcha diselesaikan...
[*] Attempt 1/30: Captcha belum siap, menunggu...
[*] Attempt 2/30: Captcha belum siap, menunggu...
[+] Captcha berhasil diselesaikan!
[*] Mencoba claim faucet...
[*] Status Code: 200
[*] Response: {"success": true, "message": "Claim successful"}
[+] Faucet claim berhasil!

[+] Bot berhasil menjalankan tugasnya!
```

## Biaya 2captcha

- reCAPTCHA v2: sekitar $2.99 per 1000 captcha
- Minimal deposit: $1-$3 tergantung metode pembayaran
- Website: https://2captcha.com/p/recaptcha

## Troubleshooting

### Error: "File 2captcha.txt tidak ditemukan"
- Pastikan file `2captcha.txt` ada di folder yang sama dengan `bot.py`

### Error: "File address.txt tidak ditemukan"
- Pastikan file `address.txt` ada di folder yang sama dengan `bot.py`

### Error: "Harap isi API key 2captcha"
- Edit file `2captcha.txt` dan masukkan API key asli Anda dari 2captcha

### Error: "Harap isi wallet address Anda"
- Edit file `address.txt` dan masukkan wallet address asli Anda
- Pastikan wallet address diawali dengan "0x"

### Error: "Wallet address harus diawali dengan '0x'"
- Format wallet address salah
- Pastikan address di file `address.txt` diawali dengan "0x"
- Contoh yang benar: `0x2bf1bbfa2bbc07e47290385936ab27a0c697fb5b`

### Error: "ERROR_WRONG_USER_KEY"
- API key 2captcha Anda salah atau tidak valid
- Periksa kembali API key di dashboard 2captcha

### Error: "ERROR_ZERO_BALANCE"
- Saldo 2captcha Anda habis
- Top up saldo di https://2captcha.com

### Captcha timeout
- Server 2captcha sedang sibuk
- Coba jalankan bot lagi setelah beberapa menit

### Claim faucet gagal (Status Code selain 200)
- Kemungkinan sudah claim sebelumnya (ada cooldown)
- Token captcha expired
- Server faucet sedang down
- Periksa response message untuk detail error

## Catatan Penting

1. **Rate Limiting**: Faucet biasanya memiliki cooldown time (misalnya 24 jam). Jangan spam claim.

2. **File Security**: 
   - Jangan share file `2captcha.txt` dan `address.txt` Anda
   - Jangan commit API key dan wallet address ke public repository
   - Tambahkan `2captcha.txt` dan `address.txt` ke `.gitignore` jika menggunakan git

3. **Biaya**: Setiap solve captcha menggunakan saldo 2captcha Anda. Pastikan saldo cukup.

4. **Legal**: Gunakan bot ini sesuai dengan Terms of Service dari faucet. Beberapa website mungkin melarang penggunaan bot.

## Kustomisasi

### Mengubah Timeout
Edit nilai di method `solve_captcha()`:

```python
time.sleep(20)  # Initial wait time (dalam detik)

for attempt in range(30):  # Jumlah percobaan
    time.sleep(10)  # Interval check (dalam detik)
```

### Menambahkan Loop Otomatis
Tambahkan loop di `main()` untuk claim berkala:

```python
import time

def main():
    # ... kode sebelumnya ...
    
    while True:
        bot.run()
        print("[*] Menunggu 24 jam untuk claim berikutnya...")
        time.sleep(86400)  # 24 jam
```

### Menambahkan Multiple Wallet
Buat list wallet di file `address.txt` (satu address per baris):

```
0x2bf1bbfa2bbc07e47290385936ab27a0c697fb5b
0xANOTHER_WALLET_ADDRESS
0xYET_ANOTHER_WALLET_ADDRESS
```

Kemudian modifikasi fungsi `main()`:

```python
def main():
    api_key = read_api_key("2captcha.txt")
    
    if not api_key:
        return
    
    # Read all wallet addresses
    with open("address.txt", 'r') as f:
        wallets = [line.strip() for line in f if line.strip()]
    
    for wallet in wallets:
        if wallet.startswith("0x"):
            print(f"\n[*] Processing wallet: {wallet}")
            bot = FaucetBot(api_key, wallet)
            bot.run()
            time.sleep(60)  # Delay antar wallet
```

## Support

Jika menemui masalah:
- 2captcha Support: https://2captcha.com/support
- IOPN Faucet Support: Cek website atau grup komunitas mereka

## Disclaimer

Bot ini dibuat untuk tujuan edukasi. Pengguna bertanggung jawab atas penggunaan bot ini. Pastikan penggunaan bot sesuai dengan Terms of Service dari layanan yang digunakan (2captcha dan IOPN Faucet).

## License

MIT License - Gunakan dengan bebas, tanpa jaminan.

---

**Happy Claiming! 🚀**

import requests
import time
import json
from typing import Optional

class FaucetBot:
    def __init__(self, api_key: str, wallet_address: str):
        """
        Initialize Faucet Bot with 2captcha API key and wallet address
        
        Args:
            api_key: 2captcha API key
            wallet_address: Your wallet address for claiming
        """
        self.api_key = api_key
        self.wallet_address = wallet_address
        self.captcha_api_url = "https://api.2captcha.com"
        self.faucet_url = "https://faucet.iopn.tech/api/faucet/claim"
        self.site_key = "6Ld1uvorAAAAAKwGWoEHDYIq_yo3dSvshmNQ9ykF"
        self.website_url = "https://faucet.iopn.tech"
        
    def solve_captcha(self) -> Optional[str]:
        """
        Solve reCAPTCHA v2 using 2captcha service
        
        Returns:
            Captcha token if successful, None otherwise
        """
        print("[*] Mengirim captcha ke 2captcha...")
        
        # Step 1: Submit captcha task
        payload = {
            "key": self.api_key,
            "method": "userrecaptcha",
            "googlekey": self.site_key,
            "pageurl": self.website_url,
            "json": 1
        }
        
        try:
            response = requests.post(f"{self.captcha_api_url}/in.php", data=payload)
            result = response.json()
            
            if result.get("status") != 1:
                print(f"[!] Error mengirim captcha: {result.get('request')}")
                return None
            
            task_id = result.get("request")
            print(f"[+] Captcha terkirim. Task ID: {task_id}")
            
            # Step 2: Wait and retrieve result
            print("[*] Menunggu captcha diselesaikan...")
            time.sleep(20)  # Wait minimum 20 seconds
            
            for attempt in range(30):  # Try for up to 5 minutes
                time.sleep(10)
                
                result_payload = {
                    "key": self.api_key,
                    "action": "get",
                    "id": task_id,
                    "json": 1
                }
                
                result_response = requests.get(f"{self.captcha_api_url}/res.php", params=result_payload)
                result_data = result_response.json()
                
                if result_data.get("status") == 1:
                    captcha_token = result_data.get("request")
                    print(f"[+] Captcha berhasil diselesaikan!")
                    return captcha_token
                elif result_data.get("request") == "CAPCHA_NOT_READY":
                    print(f"[*] Attempt {attempt + 1}/30: Captcha belum siap, menunggu...")
                else:
                    print(f"[!] Error: {result_data.get('request')}")
                    return None
            
            print("[!] Timeout: Captcha tidak selesai dalam waktu yang ditentukan")
            return None
            
        except Exception as e:
            print(f"[!] Exception saat solve captcha: {str(e)}")
            return None
    
    def claim_faucet(self, captcha_token: str) -> bool:
        """
        Claim faucet using solved captcha token
        
        Args:
            captcha_token: Solved captcha token from 2captcha
            
        Returns:
            True if claim successful, False otherwise
        """
        print("[*] Mencoba claim faucet...")
        
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "content-type": "application/json",
            "host": "faucet.iopn.tech",
            "origin": "https://faucet.iopn.tech",
            "pragma": "no-cache",
            "referer": "https://faucet.iopn.tech/",
            "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
        
        payload = {
            "address": self.wallet_address,
            "captchaToken": captcha_token
        }
        
        try:
            response = requests.post(self.faucet_url, headers=headers, json=payload)
            
            print(f"[*] Status Code: {response.status_code}")
            print(f"[*] Response: {response.text}")
            
            if response.status_code == 200:
                print("[+] Faucet claim berhasil!")
                return True
            else:
                print(f"[!] Faucet claim gagal: {response.text}")
                return False
                
        except Exception as e:
            print(f"[!] Exception saat claim faucet: {str(e)}")
            return False
    
    def run(self):
        """
        Main function to run the bot
        """
        print("=" * 60)
        print("IOPN Faucet Bot dengan 2captcha")
        print("=" * 60)
        print(f"Wallet Address: {self.wallet_address}")
        print(f"Website: {self.website_url}")
        print("=" * 60)
        
        # Step 1: Solve captcha
        captcha_token = self.solve_captcha()
        
        if not captcha_token:
            print("[!] Gagal mendapatkan captcha token. Bot berhenti.")
            return False
        
        # Step 2: Claim faucet
        success = self.claim_faucet(captcha_token)
        
        if success:
            print("\n[+] Bot berhasil menjalankan tugasnya!")
            return True
        else:
            print("\n[!] Bot gagal claim faucet.")
            return False


def read_api_key(filename: str = "2captcha.txt") -> Optional[str]:
    """
    Read API key from file
    
    Args:
        filename: Name of file containing API key
        
    Returns:
        API key string or None if file not found
    """
    try:
        with open(filename, 'r') as f:
            api_key = f.read().strip()
            return api_key
    except FileNotFoundError:
        print(f"[!] File {filename} tidak ditemukan!")
        return None


def read_wallet_address(filename: str = "address.txt") -> Optional[str]:
    """
    Read wallet address from file
    
    Args:
        filename: Name of file containing wallet address
        
    Returns:
        Wallet address string or None if file not found
    """
    try:
        with open(filename, 'r') as f:
            address = f.read().strip()
            return address
    except FileNotFoundError:
        print(f"[!] File {filename} tidak ditemukan!")
        return None


def main():
    """
    Main entry point with 24-hour auto-claim loop
    """
    # Read API key from file
    api_key = read_api_key("2captcha.txt")
    
    if not api_key:
        print("[!] Tidak dapat membaca API key. Pastikan file 2captcha.txt berisi API key Anda.")
        return
    
    if api_key == "YOUR_2CAPTCHA_API_KEY_HERE":
        print("[!] Harap isi API key 2captcha Anda di file 2captcha.txt")
        return
    
    # Read wallet address from file
    wallet_address = read_wallet_address("address.txt")
    
    if not wallet_address:
        print("[!] Tidak dapat membaca wallet address. Pastikan file address.txt berisi wallet address Anda.")
        return
    
    if wallet_address == "0xYOUR_WALLET_ADDRESS_HERE":
        print("[!] Harap isi wallet address Anda di file address.txt")
        return
    
    if not wallet_address.startswith("0x"):
        print("[!] Wallet address harus diawali dengan '0x'")
        return
    
    print(f"[+] API Key: {api_key[:10]}...{api_key[-10:]}")
    print(f"[+] Wallet Address: {wallet_address}")
    print()
    
    # Auto-claim loop (24 jam)
    claim_count = 0
    while True:
        claim_count += 1
        print("=" * 70)
        print(f"🔄 Claim #{claim_count} - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        # Create and run bot
        bot = FaucetBot(api_key, wallet_address)
        success = bot.run()
        
        if success:
            print("\n" + "=" * 70)
            print("✅ Claim berhasil!")
            print(f"⏰ Menunggu 24 jam untuk claim berikutnya...")
            print(f"📅 Claim berikutnya: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 86400))}")
            print("=" * 70)
            print("\n💡 Tips: Bot akan otomatis claim setiap 24 jam.")
            print("💡 Tekan Ctrl+C untuk menghentikan bot.\n")
            
            # Wait 24 hours (86400 seconds)
            time.sleep(86400)
        else:
            print("\n" + "=" * 70)
            print("❌ Claim gagal!")
            print("⏰ Menunggu 1 jam sebelum mencoba lagi...")
            print(f"📅 Percobaan berikutnya: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 3600))}")
            print("=" * 70)
            print("\n💡 Bot akan mencoba lagi dalam 1 jam.\n")
            
            # Wait 1 hour (3600 seconds) jika gagal
            time.sleep(3600)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print("⚠️  Bot dihentikan oleh user (Ctrl+C)")
        print("=" * 70)
        print("👋 Terima kasih telah menggunakan IOPN Faucet Bot!")
        print("=" * 70)

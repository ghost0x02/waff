import subprocess
import argparse
import os

def check_waf(url, advanced=False, output_file=None):
    try:
        command = ['wafw00f', url]

        if advanced:
            command.append('-a')

        if output_file:
            command.extend(['-o', output_file])

        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.returncode == 0:
            print(f"[+] {url} için WAF tespiti başarılı.")
            print(result.stdout)

            if output_file and os.path.exists(output_file):
                with open(output_file, 'r') as file:
                    print(f"[+] Ayrıntılı sonuçlar {output_file} dosyasında bulunmaktadır:")
                    print(file.read())
        else:
            print(f"[-] {url} için WAF tespiti başarısız. Hata Kodu: {result.returncode}")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"[-] {url} için WAF tespiti sırasında hata oluştu: {e}")

    except Exception as e:
        print(f"[!] İstek gönderilemedi: {e}")

def main():
    parser = argparse.ArgumentParser(description="WAF tespiti için araç")
    parser.add_argument('url', help="Kontrol edilecek URL")
    parser.add_argument('--advanced', action='store_true', help="Gelişmiş tarama yap")
    parser.add_argument('--output-file', help="Ayrıntılı sonuçları dosyaya kaydet")

    args = parser.parse_args()

    check_waf(args.url, args.advanced, args.output_file)

if __name__ == "__main__":
    main()

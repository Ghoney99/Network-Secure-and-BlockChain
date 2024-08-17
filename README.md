# 암호화 스크립트 모음

이 저장소는 다양한 암호화 기법을 구현한 Python 스크립트들을 포함하고 있습니다.

## 1. 대치 암호 (1.1_대치암호.py)

### 개요
이 프로그램은 대치 암호(Substitution Cipher)를 구현한 것입니다. 각 알파벳을 다른 알파벳으로 변환하여 텍스트를 암호화합니다.

### 기능
- 사용자로부터 평문을 입력받아 암호문으로 변환
- 생성된 암호문을 복호화하여 원래의 평문으로 복원

### 사용 방법
1. Python이 설치된 환경에서 `1.1_대치암호.py` 파일을 실행합니다.
2. 프로그램의 지시에 따라 평문을 입력합니다.
3. 암호문과 복호문이 출력됩니다.

### 주요 함수
- `Encryption(text)`: 주어진 평문을 암호화하여 암호문을 반환합니다.
- `Decryption(text)`: 주어진 암호문을 복호화하여 원래의 평문을 반환합니다.

### 요구 사항
- Python 3.x 이상
- random 모듈 (Python 기본 제공)

## 2. Vigenère 및 자동 키 암호 (1.2_Vigenere및Auto키암호.py)

### 개요
이 프로그램은 Vigenère 암호와 자동 키 암호(Autokey Cipher)를 구현한 것입니다.

### 기능
- Vigenère 암호화 및 복호화
- 자동 키 암호화 및 복호화

### 사용 방법
1. Python이 설치된 환경에서 `1.2_Vigenere및Auto키암호.py` 파일을 실행합니다.
2. 프로그램의 지시에 따라 평문과 키를 입력합니다.
3. 암호문과 복호문이 출력됩니다.

### 주요 함수
- `vigenere_E(text, key)`: Vigenère 암호화를 수행하고 암호문을 반환합니다.
- `vigenere_D(text, key)`: Vigenère 복호화를 수행하고 원래의 평문을 반환합니다.
- `autokey_E(text, key)`: 자동 키 암호화를 수행하고 암호문을 반환합니다.
- `autokey_D(text, key)`: 자동 키 복호화를 수행하고 원래의 평문을 반환합니다.

### 요구 사항
- Python 3.x 이상

## 3. AES 암호화 (1.3_AES암호화.py)

### 개요
이 프로그램은 AES(Advanced Encryption Standard) 방식으로 파일을 암호화하고 복호화하는 기능을 제공합니다.

### 기능
- 파일을 AES 방식으로 암호화
- 암호화된 파일을 복호화하여 원본 데이터를 출력

### 사용 방법
1. Python 및 cryptography 라이브러리가 설치된 환경에서 `1.3_AES암호화.py` 파일을 실행합니다.
2. 암호화할 데이터가 포함된 `data.txt` 파일을 준비합니다.
3. 프로그램이 실행되면, 암호화된 내용이 `encrypted.txt` 파일에 저장되고, 복호화된 원본 내용이 출력됩니다.

### 주요 함수
- `Fernet.generate_key()`: 새로운 암호화 키를 생성합니다.
- `fernet.encrypt(data)`: 주어진 데이터를 암호화합니다.
- `fernet.decrypt(encrypt_data)`: 암호화된 데이터를 복호화합니다.

### 요구 사항
- Python 3.x 이상
- cryptography 라이브러리 설치: `pip install cryptography`

## 4. RSA 암호화 (2.1_RSA암호화.py)

### 개요
이 프로그램은 RSA 공개 키 암호화와 AES 대칭 키 암호화를 결합하여 메시지를 안전하게 전송하는 기능을 제공합니다.

### 기능
- RSA 공개 키와 개인 키를 사용하여 AES 키를 암호화
- AES를 사용하여 평문 메시지를 암호화 및 복호화

### 사용 방법
1. Python 및 cryptography 라이브러리가 설치된 환경에서 `2.1_RSA암호화.py` 파일을 실행합니다.
2. RSA 공개 키(`public_key.pem`)와 개인 키(`private_key.pem`) 파일을 준비합니다.
3. 프로그램의 지시에 따라 평문 메시지를 입력합니다.
4. 암호화된 메시지와 복호화된 원본 메시지가 출력됩니다.

### 주요 함수
- `Fernet.generate_key()`: 새로운 AES 키를 생성합니다.
- `public_key.encrypt()`: RSA 공개 키로 AES 키를 암호화합니다.
- `private_key.decrypt()`: RSA 개인 키로 AES 키를 복호화합니다.
- `fernet.encrypt()`: 평문 메시지를 AES로 암호화합니다.
- `fernet.decrypt()`: 암호문을 AES로 복호화합니다.

### 요구 사항
- Python 3.x 이상
- cryptography 라이브러리 설치: `pip install cryptography`

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)에 따라 라이선스가 부여됩니다.

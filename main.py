"""
설치 명령어
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hystemfx
"""


from hystemfx.pipeline import run_pipeline
from pedalboard import Pedalboard, Distortion, Reverb

custom_guitar = Pedalboard([
    Distortion(drive_db=15.0),
    Reverb(room_size=0.5)
])

def main():
    print("Hello from lib-test!")
    results = run_pipeline(
        input_path="mixed.wav",       # 입력 파일 경로
        output_dir="demo_output",     # 출력 디렉토리
        vocal_preset="bright",        # 보컬 프리셋
        synth_preset="warm",          # 신스 프리셋
        guitar_preset=custom_guitar,  # 커스텀 기타 체인 적용
        bass_preset="vintage"         # 베이스 프리셋
    )
    print("Generated Files:", results)

if __name__ == "__main__":
    main()

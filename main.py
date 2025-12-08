"""
설치 명령어
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hystemfx==0.1.2
"""

from hystemfx.pipeline import run_pipeline, process_stem
from pedalboard import (
    Pedalboard, 
    Distortion, 
    Reverb, 
    Compressor, 
    Delay, 
    Chorus, 
    Phaser, 
    HighpassFilter, 
    Gain,
    Limiter,
)

vocal_chain = Pedalboard([
    HighpassFilter(cutoff_frequency_hz=150),

    Compressor(threshold_db=-20, ratio=4.0, attack_ms=5, release_ms=100),

    Distortion(drive_db=12.0),
    
    Gain(gain_db=-6.0),

    Delay(delay_seconds=0.5, feedback=0.1, mix=0.2),

    Reverb(room_size=0.4, wet_level=0.25, dry_level=0.8),
    
    Limiter(threshold_db=-1.0)
])

guitar_chain = Pedalboard([
    Compressor(threshold_db=-15, ratio=3),
    Distortion(drive_db=10.0),
    Chorus(rate_hz=1.0, depth=0.3, mix=0.4),
    Reverb(room_size=0.3, wet_level=0.3),
    Limiter(threshold_db=-1.0)
])

bass_chain = Pedalboard([
    Compressor(threshold_db=-20, ratio=4, attack_ms=10, release_ms=200),
    Distortion(drive_db=5.0),   
    Gain(gain_db=3.0),
    Limiter(threshold_db=-1.0)
])


synth_chain = Pedalboard([
    Compressor(threshold_db=-25, ratio=4.0, attack_ms=5, release_ms=100),
    
    Gain(gain_db=12.0),

    Phaser(rate_hz=0.5, depth=0.5, feedback=0.3, mix=0.4),

    Reverb(room_size=0.6, wet_level=0.4, dry_level=0.7),
    
    Limiter(threshold_db=-1.0)
])





def main():
    try:
        # 파이프라인 실행
        print("Running pipeline...")
        results = run_pipeline(
            input_path="AllSoulsMoon_UnmasteredWAV.wav",       # 입력 파일 경로
            output_dir="demo_output_check",
            vocal_preset=vocal_chain,
            synth_preset=synth_chain,
            guitar_preset=guitar_chain,
            bass_preset=bass_chain
        )

        print("Generated Files:", results)
        print("Quickstart code works successfully!")

    except Exception as e:
        print(f"Error running quickstart code: {e}")
        raise e

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Cinematic Audio Generator for IConSCEPT 2025 Welcome Video
Generates professional Indian English voice-over for each scene

Uses edge-tts (Microsoft Edge TTS) for high-quality neural voices
"""

import asyncio
from pathlib import Path

# Cinematic speech scripts - engaging and professional
# NOTE: "N I T" spelled out for correct pronunciation
SPEECH_SCRIPTS = [
    # Scene 1: Intro (Short, dramatic)
    """N. I. T. Puducherry... presents.""",

    # Scene 2: Main Title Reveal
    """I-Con-SCEPT 2025. The IEEE International Conference on Signal Processing,
    Computation, Electronics, Power, and Telecommunication.
    Technically co-sponsored by IEEE Madras Section.""",

    # Scene 3: NIT Puducherry
    """Welcome to the National Institute of Technology Puducherry.
    An Institute of National Importance, established in 2010.
    Our magnificent 388-acre campus in Karaikal blends coastal serenity
    with academic excellence, ranked 99th in NIRF Engineering 2025.
    Here, we nurture the next generation of technology leaders.""",

    # Scene 4: Conference Overview
    """I-Con-SCEPT 2025 is where innovation meets collaboration.
    A global platform bringing together brilliant minds, researchers,
    industry experts, and visionaries from across the world.
    This hybrid conference offers both in-person and virtual participation,
    with all accepted papers indexed in IEEE Xplore.
    Connect, collaborate, and create the future of technology.""",

    # Scene 5: Research Tracks
    """Explore eight cutting-edge research tracks.
    From Artificial Intelligence and Data Analytics, to IoT and Blockchain.
    Cyber-Physical Systems and Augmented Reality.
    5G and beyond wireless communications.
    Signal Processing and VLSI design.
    Power Electronics and Electric Vehicles.
    Renewable Energy and Industry 4.0.
    Your research finds its home here.""",

    # Scene 6: Keynote Speakers
    """Be inspired by our distinguished keynote speakers.
    Professor Alejandro Frery from Victoria University of Wellington, New Zealand.
    Dr. Arun Kumar Sangaiah from National Yunlin University, Taiwan.
    Dr. Ravi Nath Tripathi from Kyushu Institute of Technology, Japan.
    And Professor Bratin Ghosh from I I T Kharagpur, India.
    World-class expertise, groundbreaking insights.""",

    # Scene 7: Grand Welcome (Emotional, exciting)
    """On behalf of the entire organizing committee,
    we are honored to welcome you to I-Con-SCEPT 2025.
    December 6th and 7th, at N. I. T. Puducherry, Karaikal.
    The conference begins... tomorrow!
    Together, let us shape the future of technology.
    Welcome to I-Con-SCEPT 2025!"""
]

OUTPUT_DIR = Path(__file__).parent / "audio"


async def generate_audio():
    """Generate audio using Microsoft Edge TTS"""
    try:
        import edge_tts

        print("=" * 60)
        print("IConSCEPT 2025 - Cinematic Audio Generator")
        print("=" * 60)
        print("\nGenerating professional Indian English narration...")
        print("Voice: en-IN-NeerjaNeural (Female, Professional)")
        print("Fixed: N.I.T. pronounced as 'N-I-T'\n")

        OUTPUT_DIR.mkdir(exist_ok=True)

        # Using Indian English Neural voice
        voice = "en-IN-NeerjaNeural"

        for i, script in enumerate(SPEECH_SCRIPTS, 1):
            print(f"Scene {i}: Generating audio...")
            clean_script = ' '.join(script.split())

            # Create communicate object with voice settings
            communicate = edge_tts.Communicate(
                clean_script,
                voice,
                rate="-5%",  # Slightly slower for clarity
                pitch="+0Hz"
            )

            await communicate.save(str(OUTPUT_DIR / f"slide{i}.mp3"))
            print(f"  ✓ slide{i}.mp3 created")

        print("\n" + "=" * 60)
        print("✅ All audio files generated successfully!")
        print(f"   Location: {OUTPUT_DIR}")
        print(f"   Voice: {voice}")
        print("=" * 60)

    except ImportError:
        print("edge-tts not installed. Run: pip install edge-tts")
    except Exception as e:
        print(f"Error: {e}")


def main():
    asyncio.run(generate_audio())


if __name__ == "__main__":
    main()

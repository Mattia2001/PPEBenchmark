import argparse
import subprocess
import zipfile
from pathlib import Path


KAGGLE_DATASET = "mugheesahmad/sh17-dataset-for-ppe-detection"


def run_command(command: list[str]) -> None:
    print("Running:", " ".join(command))
    subprocess.run(command, check=True)


def download_sh17(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    zip_path = output_dir / "sh17-dataset-for-ppe-detection.zip"
    extract_dir = output_dir / "kaggle_dataset"

    if not zip_path.exists():
        run_command([
            "kaggle",
            "datasets",
            "download",
            "-d",
            KAGGLE_DATASET,
            "-p",
            str(output_dir)
        ])
    else:
        print(f"ZIP already exists: {zip_path}")

    if not extract_dir.exists():
        print(f"Extracting to: {extract_dir}")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
    else:
        print(f"Dataset already extracted: {extract_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=str,
        required=True,
        help="Output directory for SH17 raw dataset"
    )
    args = parser.parse_args()

    download_sh17(Path(args.output_dir))


if __name__ == "__main__":
    main()
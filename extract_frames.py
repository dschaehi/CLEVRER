import os
from pathlib import Path

from tqdm.auto import tqdm

clevrer_path = Path("/data/CLEVRER")
video_paths = sorted((clevrer_path / "videos").glob("**/*.mp4"))

for video_path in tqdm(video_paths):
    video_idx = video_path.stem.split("_")[-1]
    image_folder_path = clevrer_path / "video_frames" / ("sim_" + video_idx)
    image_folder_path.mkdir(parents=True, exist_ok=True)

    # Create PNG images from the input video
    os.system(
        f"ffmpeg -i {video_path.as_posix()} {image_folder_path.as_posix()}/frame_%05d.png -hide_banner"  # noqa: E501
    )
    for image_path in sorted(image_folder_path.glob("*.png")):
        image_idx = int(image_path.stem.split("_")[-1])
        image_path_new = image_path.parent / f"frame_{image_idx-1:05d}.png"
        image_path.rename(image_path_new)

import requests
import os
import tqdm
import logging
from pydantic import BaseModel
from typing import List, Optional, Dict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

def download_file(url: str, dest_path: str, show_progress_bars: bool = True):
    """downloads a file and shows a progress bar. allow resuming a download"""
    file_size = 0
    req = requests.get(url, stream=True, timeout=600)
    req.raise_for_status()

    total_size = int(req.headers.get('content-length', 0))
    temp_path = dest_path + ".temp"

    if os.path.exists(dest_path):
        logger.info(f"file already exists: {dest_path}")
        file_size = os.stat(dest_path).st_size
        if file_size == total_size:
            return dest_path

    if os.path.exists(temp_path):
        file_size = os.stat(temp_path).st_size

        if file_size < total_size:
            # Download incomplete
            logger.info("resuming download")
            resume_header = {'Range': f'bytes={file_size}-'}
            req = requests.get(url, headers=resume_header, stream=True,
                               verify=False, allow_redirects=True, timeout=600)
        else:
            # Error, delete file and restart download
            logger.error(f"deleting file {dest_path} and restarting")
            os.remove(temp_path)
            file_size = 0
    else:
        # File does not exist, starting download
        logger.info("starting download")

    # write dataset to file and show progress bar
    pbar = tqdm.tqdm(total=total_size, unit='B', unit_scale=True,
                     desc=dest_path, disable=not show_progress_bars)
    # Update progress bar to reflect how much of the file is already downloaded
    pbar.update(file_size)
    with open(temp_path, "ab") as dest_file:
        for chunk in req.iter_content(1024):
            dest_file.write(chunk)
            pbar.update(1024)
    # move temp file to target destination
    os.replace(temp_path, dest_path)
    return dest_path


class ErrorResponse(BaseModel):
    error: str
    type: Optional[str]


class ModelInfoResponse(BaseModel):
    coin_id: int
    correlation: int
    correlations: List[int]
    created: str
    id: int
    name: str
    status: str
    target: str
    updated: str
    ranks: Dict[str, str]


class ModelInfoShortResponse(BaseModel):
    id: int
    correlation: int
    name: str
    coin: int
    target: str


class AccountInfoResponse(BaseModel):
    api_key: bool
    joined: str
    models: List[ModelInfoShortResponse]
    user_id: str
    username: str


class EvaluateModelResponse(BaseModel):
    metrics: Dict[str, float]
    model_id: int
    class Config:
        protected_namespaces = ()

class GenerateApiKeyResponse(BaseModel):
    api_key: str


class DataInfoResponse(BaseModel):
    data: Dict[str, Dict[str, List[str]]]
    coins: List[int]
    targets: List[str]

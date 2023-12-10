from fastapi import UploadFile

def split_into_chapters(file: UploadFile, chapters: str):
    return [file]
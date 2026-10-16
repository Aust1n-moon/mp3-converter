#!/usr/bin/env python3
"""Usage: yt2mp3.py URL [URL ...] [-o OUTDIR]"""
import argparse
import yt_dlp

p = argparse.ArgumentParser(description="Download YouTube audio as MP3.")
p.add_argument("urls", nargs="+")
p.add_argument("-o", "--outdir", default=".")
args = p.parse_args()

opts = {
    "format": "bestaudio/best",
    "outtmpl": f"{args.outdir}/%(title)s.%(ext)s",
    "noplaylist": True,
    "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
}
with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download(args.urls)

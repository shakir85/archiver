"""tar command wrappers for simple backup tasks"""
import os
import sys
import logging
from app.discord import notify
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT


LOG_DIR = f"{os.getenv('HOME')}/syncdir"


def set_logging():
    if not os.path.exists(LOG_DIR):
        os.mkdir(path=LOG_DIR, mode=0o0777)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=f"{LOG_DIR}/syncdir.log", filemode="a")


def compress_to_dest(src: str, dst: str, job_name: str, dry_run=False) -> None:
    """
    Compresses 'the content' of a directory and stores the output .tar.gz to a destination directory.
    """
    today = datetime.today().strftime('%b-%d-%Y')

    set_logging()
    logging.info("Logging set successfully.")

    # dst = /mediaserver/config
    tar_file = f"{dst}/{job_name}-{today}-backup.tar.gz"
    if not dry_run:
        try:
            tar = f"tar czf {tar_file} --absolute-names -C {src} ."
            process = Popen(tar, shell=True, stdout=PIPE, stderr=STDOUT)

            if os.path.isfile(tar_file):
                logging.info("Archive with the same timestamp exists, Exiting...")
                notify(job_name=job_name, status="exited")
                sys.exit(0)

            with process.stdout:
                for i in iter(process.stdout.readline, b''):
                    logging.info(i.decode("utf-8").strip())

                # Close logging and send notification
                logging.info(f"Archiving job: [{job_name}] completed.")
                notify(job_name=job_name, status="success")

        except OSError as e:
            logging.error(f"Compress job: [{job_name}] failed\n{e}")
    else:
        print("[dry_run] Attempting to compress:\n"
              f"[dry_run] directory: {src}\n"
              f"[dry_run] and move it to: {dst}\n"
              f"[dry_run] Final tar file: {tar_file}\n"
              f"[dry_run] Job name: {job_name}\n")

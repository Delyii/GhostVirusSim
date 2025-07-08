import os
import sys
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

REPLICATION_DIR = os.path.abspath("sandbox/replicas")
LOG_FILE = os.path.abspath("ghostsim.log")

os.makedirs(REPLICATION_DIR, exist_ok=True)

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

def replicate():
    for i in range(3):
        replica_name = f"ghost_{i}.ghost"
        path = os.path.join(REPLICATION_DIR, replica_name)
        with open(path, "w") as f:
            f.write("GHOST FILE")
        log(f"Replicated: {path}")

def activate_kill_switch():
    log("=== KILL SWITCH ACTIVATED ===")
    messagebox.showinfo("Kill Switch", "Simulation ended. Logs saved.")

def show_logs():
    if os.path.exists(LOG_FILE):
        os.startfile(LOG_FILE) if sys.platform.startswith('win') else os.system(f"open '{LOG_FILE}'")
    else:
        messagebox.showinfo("Logs", "No log file found.")

def open_replica_dir():
    if os.path.exists(REPLICATION_DIR):
        os.startfile(REPLICATION_DIR) if sys.platform.startswith('win') else os.system(f"open '{REPLICATION_DIR}'")
    else:
        messagebox.showinfo("Directory", "No replication directory found.")

def delete_replicas():
    if messagebox.askyesno("Confirm Deletion", "Delete all replicas?"):
        deleted = 0
        for filename in os.listdir(REPLICATION_DIR):
            if filename.endswith(".ghost"):
                os.remove(os.path.join(REPLICATION_DIR, filename))
                deleted += 1
        log(f"Deleted {deleted} replicas.")
        messagebox.showinfo("Deletion", f"Deleted {deleted} replicas.")

def run_simulation():
    replicate()
    log("Simulation started.")

root = tk.Tk()
root.title("GhostSim Console")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Run Simulation", width=30, command=run_simulation).pack(pady=5)
tk.Button(frame, text="Activate Kill Switch", width=30, command=activate_kill_switch).pack(pady=5)
tk.Button(frame, text="Show Logs", width=30, command=show_logs).pack(pady=5)
tk.Button(frame, text="Show Replication Folder", width=30, command=open_replica_dir).pack(pady=5)
tk.Button(frame, text="Delete All Replicas", width=30, command=delete_replicas).pack(pady=5)

root.mainloop()

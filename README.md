# PC SUPER OPTIMIZER v3.0
### Windows Performance, Gaming & System Optimization Tool

---

## What Is This?

**PC Super Optimizer** is a free, open-source Windows optimization tool built in Python. It gives you a clean terminal menu to run powerful system tweaks — all in one place, no bloatware, no ads, no subscriptions.

It handles everything from cleaning junk files and optimizing RAM, to creating a custom "Unlimited Performance" power plan and tuning your PC for hardcore gaming.

---

## Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10 or Windows 11 |
| **Python** | 3.8 or higher — [python.org](https://python.org) |
| **Privileges** | Administrator (script auto-requests this) |
| **Dependencies** | None — uses only Python standard library |

---

## How to Run

1. Download or clone this folder
2. Make sure `optimizer.py` and `RUN.bat` are in the **same folder**
3. **Double-click `RUN.bat`**
4. Click **Yes** on the UAC prompt (Administrator required)
5. Pick an option from the menu

> **No Python?** Download it free from [python.org](https://python.org).
> During install, check **"Add Python to PATH"** — this is required.

---

## Menu Options

```
[1]  Create System Restore Point
[2]  Optimize System Performance
[3]  Hardcore Gaming Optimizer
[4]  Delete All Caches and Junk Files
[5]  Create and Apply UNLIMITED Power Plan
[6]  Deep Clean Registry
[7]  Optimize RAM and Virtual Memory
[8]  Optimize Network and DNS
[9]  FULL NUKE - Run ALL Optimizations
[0]  Exit
```

---

## What Each Module Does

### [1] Create System Restore Point
Creates a Windows System Restore Point before any changes are made.
- Enables System Restore on C:\ if disabled
- Labels the restore point "PC Super Optimizer - Backup"
- Lets you roll back all changes via Control Panel → Recovery → System Restore

---

### [2] Optimize System Performance
Tunes Windows for maximum speed and responsiveness.
- Sets Visual Effects to **Best Performance** (disables animations, transparency)
- Removes menu delay (0ms response)
- Reduces app kill timeout to 2 seconds
- Disables Windows telemetry (DiagTrack)
- Tunes CPU scheduling to prioritize foreground apps
- Disables SysMain (Superfetch) — reduces disk thrashing
- Disables Windows Search indexer
- Runs `sfc /scannow` in background to repair system files

---

### [3] Hardcore Gaming Optimizer
Everything your PC needs to squeeze out maximum FPS and lowest latency.
- Activates **UNLIMITED PERFORMANCE** power plan
- Sets GPU scheduling priority to maximum (GPU Priority: 8)
- Disables network throttling — lowest possible ping
- Disables Game DVR, Game Bar, and background recording
- Disables fullscreen optimizations — true exclusive fullscreen
- Disables mouse acceleration — pure 1:1 raw input
- Stops background services: SysMain, DiagTrack, WSearch, Fax, MapsBroker
- Locks CPU at 100% — no throttling
- Clears NVIDIA and AMD shader caches for fresh build
- Flushes DNS cache

---

### [4] Delete All Caches and Junk Files
Wipes all temporary, cached, and junk files Windows accumulates over time.
- User and Windows TEMP folders
- Windows Prefetch cache
- Internet Explorer and Edge browser cache
- Windows thumbnail cache database
- NVIDIA DXCache and GLCache (shader cache)
- AMD DxCache (shader cache)
- Recycle Bin (all drives)
- Windows Update download cache
- Font cache (rebuilt automatically on next boot)
- Runs Windows built-in `cleanmgr` Disk Cleanup

---

### [5] Create and Apply UNLIMITED Power Plan
Creates a brand-new custom Windows power plan with zero compromises.
- Duplicates the **Ultimate Performance** base plan
- Names it **"UNLIMITED PERFORMANCE"**
- Locks CPU minimum and maximum at **100%**
- Enables **Turbo Boost** at maximum policy
- Disables CPU idle states
- Disables **sleep**, **hibernate**, and **hybrid sleep** — never interrupts you
- Screen timeout set to **Never**
- Hard disk spindown set to **Never**
- USB selective suspend **disabled** — controllers stay powered
- Activates the plan immediately

> After running this, you'll see "UNLIMITED PERFORMANCE" in Windows Power Options.

---

### [6] Deep Clean Registry
Removes stale, obsolete, and privacy-sensitive registry entries.
- Clears Run / RunMRU history
- Clears Recent Documents list
- Clears Explorer address bar typed paths
- Removes orphaned font cache registry entries
- Removes stale thumbnail cache pointers
- Disables Remote Registry service (security hardening)
- Clears Windows Error Reporting cache

---

### [7] Optimize RAM and Virtual Memory
Frees up RAM and tunes memory management.
- Flushes DNS resolver cache
- Purges Windows **standby memory list** via NT kernel API
- Trims working sets of all running processes
- Sets page file to **system-managed** (optimal sizing)
- Disables **memory compression** (frees CPU cycles)
- Shows MB freed before and after

---

### [8] Optimize Network and DNS
Lowers latency and improves network reliability.
- Flushes DNS cache
- Releases and renews IP address
- Resets TCP/IP stack (`netsh int ip reset`)
- Resets Winsock catalog (`netsh winsock reset`)
- Disables network throttling (NetworkThrottlingIndex)
- Disables **Nagle algorithm** — lower TCP latency for gaming/VoIP
- Sets DNS to **Cloudflare 1.1.1.1 / 1.0.0.1** (fastest public DNS)

---

### [9] FULL NUKE — Run All Optimizations
Runs all 8 modules sequentially in one go.
- Creates a restore point first (safety)
- Runs every module automatically
- Offers to **restart your PC** when complete for maximum effect

---

## Safety & Restore

> **Always run option [1] before [9] (Full Nuke).**

All tweaks are reversible:
- **System Restore** — undoes all registry and system changes
- **Power Plan** — delete "UNLIMITED PERFORMANCE" in Power Options to restore default
- **Services** — re-enable any service via `services.msc`
- **DNS** — reset via `netsh interface ip set dns "adapter" dhcp`

---

## File Structure

```
📁 PC Super Optimizer/
├── optimizer.py      ← Main Python script (all logic)
├── RUN.bat           ← Double-click launcher
└── README.md         ← This file
```

---

## FAQ

**Q: The BAT file opens and closes instantly.**
A: Python is not installed or not in PATH. Install from python.org and check "Add Python to PATH".

**Q: I get a UAC prompt — is that normal?**
A: Yes. Administrator rights are required to modify registry keys, services, and power plans.

**Q: Will this break my PC?**
A: Unlikely. All changes are standard Windows tweaks. Create a restore point first (option 1) for peace of mind.

**Q: Can I undo the changes?**
A: Yes. Use System Restore (Control Panel → Recovery → System Restore) to roll everything back.

**Q: The UNLIMITED power plan isn't showing.**
A: Run option [5] again. Some systems require Ultimate Performance to be unlocked first via `powercfg -duplicatescheme`.

**Q: My antivirus flagged this.**
A: Some AV software flags scripts that modify registry or services. This tool does not connect to the internet, does not install anything, and contains no malware. You can read every line of `optimizer.py` yourself.

---

## License

Free to use, modify, and share. No warranties expressed or implied.
Use at your own risk. Always create a restore point before running.

---

*Built with Python 3 | Windows 10/11 | No dependencies*
"# pc-optimzier" 

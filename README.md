# PC SUPER OPTIMIZER v4.0
### Windows Performance, Gaming & System Optimization Tool

> Comprehensive system tuning for maximum FPS and minimal input lag — deep bloatware removal and background process refinement — advanced power management and thermal optimization — network stabilization for competitive gaming.

---

## What Is This?

**PC Super Optimizer** is a free, open-source Windows optimization utility built entirely in Python. It provides a clean, colorful terminal interface with 8 powerful modules that cover every aspect of PC performance — from GPU scheduling and input lag reduction, to bloatware removal, thermal management, and competitive network tuning.

No bloatware. No ads. No internet connection required. No third-party dependencies. Every line of code is readable in `optimizer.py`.

---

## Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10 or Windows 11 (64-bit recommended) |
| **Python** | 3.8 or higher — [python.org](https://python.org) |
| **Privileges** | Administrator — script auto-requests elevation on launch |
| **Dependencies** | None — Python standard library only |

---

## How to Run

1. Place `optimizer.py` and `RUN.bat` in the **same folder**
2. Install Python from [python.org](https://python.org) if needed — tick **"Add Python to PATH"** during install
3. **Double-click `RUN.bat`**
4. Click **Yes** on the UAC (Administrator) prompt
5. Choose a number from the menu and press ENTER
6. **Restart your PC** after running optimizations for maximum effect

---

## Menu Options

```
[1]  Create System Restore Point
[2]  Optimize System Performance
[3]  Max FPS + Input Lag Reduction
[4]  Bloatware + Background Process Removal
[5]  Power + Thermal Optimization
[6]  Competitive Network Stabilization
[7]  Delete All Caches and Junk Files
[8]  Deep Clean Registry + RAM
[9]  FULL NUKE - Run ALL Optimizations
[0]  Exit
```

---

## What Each Module Does

### [1] Create System Restore Point
Safety first — creates a restore point before any changes so you can always roll back.
- Enables System Restore on C:\ if it was disabled
- Labels the point `"PC Super Optimizer v4.0"`
- Roll back at any time via: Control Panel → Recovery → System Restore

---

### [2] Optimize System Performance
Core Windows responsiveness and CPU tuning.
- Visual Effects set to **Best Performance** — animations, transparency, Aero Peek all off
- Menu delay removed (0ms), app kill timeout reduced to 1 second
- `WaitToKillServiceTimeout` reduced to 2 seconds
- CPU scheduling tuned to prioritize foreground apps (`Win32PrioritySeparation = 38`)
- CPU core parking disabled — all cores stay active
- SysMain (Superfetch) stopped and disabled
- Windows Search indexer stopped and disabled
- DiagTrack and dmwappushservice (telemetry) stopped and disabled
- `sfc /scannow` launched in background to repair any system file corruption

---

### [3] Max FPS + Input Lag Reduction
Comprehensive system tuning for maximum FPS and minimal input lag.

**GPU & Rendering**
- GPU task scheduler set to maximum priority (GPU Priority: 8, Clock Rate: 10000)
- `Background Only` set to False — OS never de-prioritizes game threads
- Hardware-Accelerated GPU Scheduling (HAGS) enabled via registry
- Fullscreen optimizations disabled globally — true exclusive fullscreen on all games
- Game DVR, Game Bar, and background recording fully disabled
- NVIDIA DXCache, GLCache, and OptixCache cleared
- AMD DxCache cleared

**Mouse & Input**
- Mouse acceleration fully disabled — pure 1:1 raw input
- Enhance Pointer Precision turned off
- System timer resolution locked to **1ms** via `timeBeginPeriod` API call
- USB selective suspend disabled per HID device (mouse and keyboard stay instant)

**Multimedia Profile**
- `SystemResponsiveness` set to 0 — game threads get full CPU time slices
- `NetworkThrottlingIndex` set to max — no OS-level network throttling
- `NoLazyMode` enabled — OS cannot put the multimedia timer to sleep

---

### [4] Bloatware + Background Process Removal
Deep bloatware removal and background process refinement.

**Services Disabled (24 total)**
DiagTrack, dmwappushservice, SysMain, WSearch, TabletInputService, MapsBroker, Fax, RetailDemo, RemoteRegistry, WerSvc, PcaSvc, XblAuthManager, XblGameSave, XboxNetApiSvc, XboxGipSvc, lfsvc (geolocation), SharedAccess, PhoneSvc, WpcMonSvc (parental controls), wisvc (Insider service), TrkWks, PrintNotify, stisvc (Windows Image Acquisition), WMPNetworkSvc

**UWP Apps Removed (32 packages)**
Bing News, Bing Weather, Bing Finance, Bing Sports, Get Help, Get Started, Solitaire Collection, Office Hub, OneNote, OneConnect, People, Skype, Feedback Hub, Maps, Xbox TCUI, Xbox App, Xbox Game Overlay, Xbox Gaming Overlay, Xbox Identity Provider, Xbox Speech-to-Text, Your Phone, Groove Music, Movies & TV, Microsoft Teams, Clipchamp, To Do, Power Automate, Sound Recorder, Cortana, Mixed Reality Portal, 3D Viewer, Print 3D

Also removed as **provisioned packages** so they won't reinstall for new user accounts.

**Additional Background Hardening**
- Background app access disabled globally
- Cortana disabled via policy
- Windows tips, ads, and suggestions disabled
- Telemetry data collection set to 0 via policy registry
- Activity history and location tracking disabled
- Startup app delay removed (`StartupDelayInMSec = 0`)

---

### [5] Power + Thermal Optimization
Advanced power management and thermal optimization.

**UNLIMITED PERFORMANCE Power Plan**
- Duplicates the Ultimate Performance base plan
- Names it **"UNLIMITED PERFORMANCE"** (visible in Power Options after)
- CPU minimum and maximum locked at **100%**
- Turbo Boost enabled at maximum boost policy (`PERFBOOSTMODE = 2`, `PERFBOOSTPOL = 100`)
- CPU idle states disabled (`IDLEDISABLE = 1`)
- Performance step-up policy set to aggressive (`PERFINCPOL = 2`)
- Sleep, Hibernate, Hybrid Sleep set to **Never**
- Screen timeout set to **Never**
- Hard disk and SSD spindown set to **Never**
- USB selective suspend disabled — all peripherals stay fully powered
- Plan activated immediately

**Thermal Management**
- Cooling policy set to **Active** — fan priority over performance reduction
- Thermal throttle notification delay removed
- Connected Standby / Modern Standby disabled — no surprise power state drops
- Processor autonomous mode enabled for fastest frequency ramp-up

---

### [6] Competitive Network Stabilization
Network stabilization for competitive gaming — lower ping, stable packets, no throttling.

**TCP/IP Stack Reset**
- DNS cache flushed
- IP released and renewed
- TCP/IP stack reset (`netsh int ip reset`)
- Winsock catalog reset
- IPv6 stack reset

**Latency & Packet Tuning**
- Nagle algorithm disabled — `TcpAckFrequency = 1`, `TCPNoDelay = 1`, `TcpDelAckTicks = 0`
- Network throttling index removed (`NetworkThrottlingIndex = 0xFFFFFFFF`)
- RSS (Receive Side Scaling) enabled for multi-core NIC performance
- TCP auto-tuning set to normal
- ECN (Explicit Congestion Notification) enabled for better congestion handling
- MTU locked to 1500 bytes per active adapter (standard Ethernet)

**DNS**
- DNS set to **Cloudflare 1.1.1.1 / 1.0.0.1** on all active adapters
- Negative DNS cache time set to 0 — no stale NXDOMAIN blocks
- DNS max cache TTL capped at 1 hour
- DNS flushed after all changes

**NIC Power & QoS**
- QoS 20% bandwidth reservation removed (`NonBestEffortLimit = 0`)
- NIC Wake-on-LAN and Wake-on-Pattern disabled — prevents micro-stutters
- Interrupt moderation disabled per adapter — lower per-packet latency
- NIC receive buffers set to 2048
- IPv6 disabled on active adapters — removes dual-stack DNS lookup delay

---

### [7] Delete All Caches and Junk Files
Wipes every cache and junk pile Windows accumulates over time.
- User TEMP and Windows TEMP folders
- Windows Prefetch cache
- IE / Edge INetCache
- Windows Explorer thumbnail database
- DirectX Shader Cache (D3DSCache)
- NVIDIA DXCache, GLCache, OptixCache
- AMD DxCache
- Windows Error Reports
- Chrome cache
- Edge cache
- Firefox profiles cache
- Recycle Bin (all drives)
- Windows Update download cache (`SoftwareDistribution\Download`)
- Font cache (automatically rebuilds on next boot)
- Windows Disk Cleanup (`cleanmgr /sagerun:1`)

---

### [8] Deep Clean Registry + RAM
Registry cleanup combined with live RAM reclamation — shows freed MB before and after.

**Registry**
- Run / RunMRU history cleared
- Recent Documents list cleared
- Explorer typed paths cleared
- Stale font cache registry entries removed
- Stale thumbnail cache pointers removed
- Remote Registry service disabled
- Windows Error Reporting queue cleared

**RAM**
- Standby memory list purged via `NtSetSystemInformation` kernel API
- Process working sets trimmed across all running processes
- Page file set to system-managed (optimal automatic sizing)
- Memory compression disabled (frees CPU cycles)
- DNS cache flushed
- Before/after RAM usage displayed in MB

---

### [9] FULL NUKE — Run All Optimizations
Runs all 8 modules sequentially in a single pass.
- Creates restore point first for safety
- Runs every module automatically without pausing
- Shows module-by-module progress
- Offers to **restart your PC** (15-second countdown, cancellable) for maximum effect

---

## Coverage Summary

| Pillar | Covered By |
|---|---|
| Max FPS + minimal input lag | Modules 2, 3, 5 |
| Bloatware + background process removal | Module 4 |
| Advanced power + thermal management | Module 5 |
| Network stabilization for competitive gaming | Module 6 |
| System cleanliness + RAM | Modules 7, 8 |

---

## Safety & Restore

> **Always run option [1] before option [9] (Full Nuke).**

All changes are reversible:

| What to undo | How |
|---|---|
| All registry + system changes | System Restore → Control Panel → Recovery → System Restore |
| UNLIMITED PERFORMANCE plan | Delete it in Power Options, reactivate Balanced |
| Disabled services | Re-enable via `services.msc` (search "Services" in Start) |
| DNS changes | `netsh interface ip set dns "Ethernet" dhcp` |
| Visual effects | Control Panel → System → Advanced → Performance → Visual Effects |
| Removed UWP apps | Reinstall from Microsoft Store individually |

---

## File Structure

```
📁 PC Super Optimizer/
├── optimizer.py    ← Main Python script — all 8 modules and terminal UI
├── RUN.bat         ← 6-line launcher — checks Python, then runs optimizer.py
└── README.md       ← This file
```

---

## FAQ

**Q: RUN.bat opens and closes instantly.**
A: Python is not installed or not in PATH. Download from python.org — check "Add Python to PATH" during install.

**Q: UAC prompt appears — is that normal?**
A: Yes. Administrator rights are required to modify registry keys, services, and power plans. This is expected behavior.

**Q: Will this break my PC?**
A: All tweaks are standard Windows registry and `powercfg` commands used by performance enthusiasts. Run option [1] first to create a restore point and you can always roll back.

**Q: Can I undo everything?**
A: Yes. System Restore (Control Panel → Recovery → System Restore) undoes all registry and system changes in one step.

**Q: UNLIMITED PERFORMANCE plan is not in Power Options.**
A: Run option [5] again. On some systems, Ultimate Performance needs to be unlocked first via `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61` in an admin CMD.

**Q: My antivirus flagged the script.**
A: Some AV tools flag scripts that modify registry, services, or power plans. This tool does not connect to the internet, installs nothing, and contains no malware. Every line of `optimizer.py` is human-readable.

**Q: Some apps I want were removed in Module 4.**
A: Reinstall any removed app directly from the Microsoft Store. Module 4 only removes pre-installed Microsoft apps, not anything you installed yourself.

**Q: Module 6 changed my DNS — will this affect browsing?**
A: Cloudflare 1.1.1.1 is faster and more private than most ISP DNS. If you want to revert: `netsh interface ip set dns "Ethernet" dhcp` in an admin CMD.

---

---

## WINDOWS OS UPDATE (OPTIONAL)
- Use Atlas OS for better performace safe to use and better for gaming

---

## Changelog

### v4.0
- Module 3 rebuilt: HAGS enabled, 1ms timer resolution, USB HID selective suspend disabled, full GPU task scheduler config
- Module 4 added: 24 services disabled, 32 UWP apps removed + de-provisioned, full telemetry hardening
- Module 5 expanded: Active cooling policy, Connected Standby disabled, aggressive CPU step-up policy
- Module 6 expanded: Nagle `TcpDelAckTicks=0`, NIC interrupt moderation, receive buffers, QoS reservation removed, IPv6 disabled, per-adapter DNS
- Module 7 expanded: DirectX shader cache, OptixCache, Firefox, Chrome, WER added
- All modules now use direct `winreg` API calls instead of `reg add` shell commands

### v3.0
- Rewrote from BAT to Python for reliability
- ANSI color terminal UI
- 8-module architecture with Full Nuke mode

---

## License

Free to use, modify, and share. No warranties expressed or implied.
Use at your own risk. Always create a restore point before running.

---

*PC Super Optimizer v4.0 — Built with Python 3 — Windows 10 / 11 — No dependencies*
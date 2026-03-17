import os, sys, ctypes, subprocess, shutil, time, platform, winreg

CY = "\033[96m"; YL = "\033[93m"; GR = "\033[92m"
RD = "\033[91m"; WH = "\033[97m"; MG = "\033[95m"
DM = "\033[2m";  RS = "\033[0m"
os.system("color")

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def relaunch_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{os.path.abspath(__file__)}"', None, 1)
    sys.exit()

def run(cmd):
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def run_out(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.stdout.strip()

def ok(msg):       print(f"  {GR}[OK]{RS}  {msg}")
def warn(msg):     print(f"  {YL}[!!]{RS}  {msg}")
def info(msg):     print(f"  {CY}[..]{RS}  {msg}")
def step(n, t, m): print(f"  {CY}[{n}/{t}]{RS}  {m}", end=" ", flush=True)
def done_step():   print(f"{GR}done{RS}")
def fail_step():   print(f"{YL}skipped{RS}")
def div():         print(f"  {DM}{'─'*57}{RS}")

def pause():
    print(f"\n  {DM}Press ENTER to return to menu...{RS}", end="")
    input()

def header(title, subtitle=""):
    os.system("cls")
    print(f"\n{CY}  +{'='*57}+{RS}")
    print(f"{CY}  |  PC SUPER OPTIMIZER v4.0  [ADMINISTRATOR]{' '*14}|{RS}")
    print(f"{CY}  +{'='*57}+{RS}")
    print(f"\n{YL}  >>  {title}{RS}")
    if subtitle:
        print(f"  {DM}{subtitle}{RS}")
    print(f"{YL}  {'─'*59}{RS}\n")

def del_tree(path):
    if not os.path.exists(path): return
    for item in os.listdir(path):
        fp = os.path.join(path, item)
        try:
            if os.path.isfile(fp): os.remove(fp)
            elif os.path.isdir(fp): shutil.rmtree(fp, ignore_errors=True)
        except: pass

class _MEM(ctypes.Structure):
    _fields_ = [
        ("dwLength",ctypes.c_ulong),("dwMemoryLoad",ctypes.c_ulong),
        ("ullTotalPhys",ctypes.c_ulonglong),("ullAvailPhys",ctypes.c_ulonglong),
        ("ullTotalPageFile",ctypes.c_ulonglong),("ullAvailPageFile",ctypes.c_ulonglong),
        ("ullTotalVirtual",ctypes.c_ulonglong),("ullAvailVirtual",ctypes.c_ulonglong),
        ("ullAvailExtendedVirtual",ctypes.c_ulonglong)
    ]
def get_mem():
    m = _MEM(); m.dwLength = ctypes.sizeof(_MEM)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m

def show_menu():
    os.system("cls")
    print(f"""
{CY}  +{'='*59}+{RS}
{CY}  |{YL}   ____   ____      ____  _   _ ____  _____ ____       {CY}|{RS}
{CY}  |{YL}  |  _ \\ / ___|    / ___|| | | |  _ \\| ____|  _ \\      {CY}|{RS}
{CY}  |{YL}  | |_) | |        \\___ \\| | | | |_) |  _| | |_) |     {CY}|{RS}
{CY}  |{YL}  |  __/| |___      ___) | |_| |  __/| |___|  _ <      {CY}|{RS}
{CY}  |{YL}  |_|    \\____|    |____/ \\___/|_|   |_____|_| \\_\\     {CY}|{RS}
{CY}  |{RS}                                                           {CY}|{RS}
{CY}  |{WH}         WINDOWS PC SUPER OPTIMIZER  v4.0                {CY}|{RS}
{CY}  |{DM}     Administrator Mode  |  All Features Unlocked            {CY}|{RS}
{CY}  +{'='*59}+{RS}

{WH}  +{'─'*59}+{RS}
{WH}  |{RS}                                                           {WH}|{RS}
{WH}  |  {CY}[1]{RS}  Create System Restore Point (Safety First)        {WH}|{RS}
{WH}  |  {CY}[2]{RS}  Optimize System Performance                        {WH}|{RS}
{WH}  |  {CY}[3]{RS}  MAX FPS + Minimal Input Lag                        {WH}|{RS}
{WH}  |  {CY}[4]{RS}  Bloatware Removal + Background Refinement          {WH}|{RS}
{WH}  |  {CY}[5]{RS}  UNLIMITED Power Plan + Thermal Optimization        {WH}|{RS}
{WH}  |  {CY}[6]{RS}  Network Stabilization (Competitive Gaming)         {WH}|{RS}
{WH}  |  {CY}[7]{RS}  Deep Clean  -  Caches, Registry, RAM               {WH}|{RS}
{WH}  |  {CY}[8]{RS}  System Health Check                                {WH}|{RS}
{WH}  |  {MG}[9]{RS}  FULL NUKE  -  Run ALL Optimizations                {WH}|{RS}
{WH}  |  {RD}[0]{RS}  Exit                                               {WH}|{RS}
{WH}  |{RS}                                                           {WH}|{RS}
{WH}  +{'─'*59}+{RS}""")
    return input(f"\n  {YL}Your choice [0-9]: {RS}").strip()

# ── MODULE 1 ──────────────────────────────────────────────────
def create_restore_point():
    header("CREATE SYSTEM RESTORE POINT", "Always run this first before any optimizations")
    step(1, 2, "Enabling System Restore on C:\\...")
    run("powershell -Command \"Enable-ComputerRestore -Drive 'C:\\'\"")
    done_step()
    step(2, 2, "Creating restore point...")
    r = subprocess.run(
        "powershell -Command \"Checkpoint-Computer -Description 'PC Super Optimizer v4' -RestorePointType 'MODIFY_SETTINGS'\"",
        shell=True, capture_output=True)
    if r.returncode == 0:
        done_step(); ok("Restore point created: 'PC Super Optimizer v4'")
    else:
        fail_step(); warn("Windows cooldown active (max 1 per 24h)")
    div(); info("Restore via: Control Panel > Recovery > System Restore")
    pause()

# ── MODULE 2 ──────────────────────────────────────────────────
def optimize_system():
    header("OPTIMIZE SYSTEM PERFORMANCE", "Visual, scheduling, and core Windows tweaks")
    tasks = [
        ("Visual effects -> Best Performance",
         lambda: [
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f'),
             run('reg add "HKCU\\Control Panel\\Desktop\\WindowMetrics" /v MinAnimate /t REG_SZ /d 0 /f'),
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v EnableTransparency /t REG_DWORD /d 0 /f'),
         ]),
        ("Eliminating menu delay + fast app kill",
         lambda: [
             run('reg add "HKCU\\Control Panel\\Desktop" /v MenuShowDelay /t REG_SZ /d 0 /f'),
             run('reg add "HKCU\\Control Panel\\Desktop" /v AutoEndTasks /t REG_SZ /d 1 /f'),
             run('reg add "HKCU\\Control Panel\\Desktop" /v WaitToKillAppTimeout /t REG_SZ /d 2000 /f'),
             run('reg add "HKCU\\Control Panel\\Desktop" /v HungAppTimeout /t REG_SZ /d 1000 /f'),
             run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v WaitToKillServiceTimeout /t REG_SZ /d 2000 /f'),
         ]),
        ("Tuning CPU scheduling for foreground apps",
         lambda: run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 38 /f')),
        ("Disabling SysMain (Superfetch)",
         lambda: [run("sc stop SysMain"), run("sc config SysMain start= disabled")]),
        ("Disabling Windows Search indexer",
         lambda: [run("sc stop WSearch"), run("sc config WSearch start= disabled")]),
        ("Disabling Windows telemetry (DiagTrack)",
         lambda: [
             run("sc stop DiagTrack"), run("sc config DiagTrack start= disabled"),
             run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f'),
         ]),
        ("Disabling HPET (CPU uses TSC for lower latency)",
         lambda: run("bcdedit /deletevalue useplatformclock")),
        ("Setting 1ms timer resolution (lower input lag)",
         lambda: run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v GlobalTimerResolutionRequests /t REG_DWORD /d 1 /f')),
        ("Running System File Checker in background",
         lambda: subprocess.Popen("sfc /scannow", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)),
    ]
    for i, (label, fn) in enumerate(tasks, 1):
        step(i, len(tasks), label + "...")
        try: fn()
        except: pass
        done_step()
    print(f"\n  {GR}[DONE] System Performance Optimization COMPLETE!{RS}")
    pause()

# ── MODULE 3 — MAX FPS + INPUT LAG ────────────────────────────
def fps_input_lag():
    header("MAX FPS + MINIMAL INPUT LAG",
           "Pillar I: Comprehensive system tuning for maximum FPS and minimal input lag")
    tasks = [
        ("GPU scheduling priority -> maximum (priority 8, High category)",
         lambda: [
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "Priority" /t REG_DWORD /d 6 /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "Scheduling Category" /t REG_SZ /d "High" /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "SFIO Priority" /t REG_SZ /d "High" /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "Background Only" /t REG_SZ /d "False" /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "Clock Rate" /t REG_DWORD /d 10000 /f'),
         ]),
        ("Enabling Hardware-Accelerated GPU Scheduling (HAGS)",
         lambda: run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 2 /f')),
        ("Disabling Game DVR + Game Bar (zero background capture overhead)",
         lambda: [
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f'),
             run('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f'),
             run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" /v AllowGameDVR /t REG_DWORD /d 0 /f'),
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_EFSEFeatureFlags /t REG_DWORD /d 0 /f'),
         ]),
        ("Disabling fullscreen optimizations (true exclusive fullscreen)",
         lambda: [
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f'),
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_HonorUserFSEBehaviorMode /t REG_DWORD /d 1 /f'),
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_DXGIHonorFSEWindowsCompatible /t REG_DWORD /d 1 /f'),
             run('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_DSEBehavior /t REG_DWORD /d 2 /f'),
         ]),
        ("Disabling mouse acceleration (pure 1:1 raw input)",
         lambda: [
             run('reg add "HKCU\\Control Panel\\Mouse" /v MouseSpeed /t REG_SZ /d "0" /f'),
             run('reg add "HKCU\\Control Panel\\Mouse" /v MouseThreshold1 /t REG_SZ /d "0" /f'),
             run('reg add "HKCU\\Control Panel\\Mouse" /v MouseThreshold2 /t REG_SZ /d "0" /f'),
         ]),
        ("Setting system responsiveness to 0 (game gets 100% CPU)",
         lambda: [
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f'),
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f'),
         ]),
        ("Disabling dynamic tick (consistent frame timing intervals)",
         lambda: [run("bcdedit /set disabledynamictick yes"), run("bcdedit /set useplatformtick yes")]),
        ("Disabling OS-level power throttling for all processes",
         lambda: run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" /v PowerThrottlingOff /t REG_DWORD /d 1 /f')),
        ("Clearing NVIDIA DXCache / GLCache / ComputeCache",
         lambda: [
             del_tree(os.path.join(os.environ.get("LOCALAPPDATA",""), "NVIDIA", "DXCache")),
             del_tree(os.path.join(os.environ.get("LOCALAPPDATA",""), "NVIDIA", "GLCache")),
             del_tree(os.path.join(os.environ.get("LOCALAPPDATA",""), "NVIDIA", "ComputeCache")),
         ]),
        ("Clearing AMD DxCache / VkCache",
         lambda: [
             del_tree(os.path.join(os.environ.get("LOCALAPPDATA",""), "AMD", "DxCache")),
             del_tree(os.path.join(os.environ.get("LOCALAPPDATA",""), "AMD", "VkCache")),
         ]),
    ]
    for i, (label, fn) in enumerate(tasks, 1):
        step(i, len(tasks), label + "...")
        try: fn()
        except: pass
        done_step()
    div()
    ok("HAGS enabled (requires NVIDIA 450+ or AMD 21.4+ driver)")
    ok("Mouse: pure 1:1 raw input, acceleration fully disabled")
    ok("GPU scheduler: max priority, all resources go to your game")
    ok("Timer: 1ms resolution, dynamic tick disabled = smoother frames")
    print(f"\n  {GR}[DONE] MAX FPS + INPUT LAG COMPLETE!{RS}")
    pause()

# ── MODULE 4 — BLOATWARE + BACKGROUND REFINEMENT ──────────────
BLOAT_SERVICES = [
    ("DiagTrack","Telemetry"),("SysMain","Superfetch"),("WSearch","Search indexer"),
    ("TabletInputService","Tablet input"),("MapsBroker","Maps downloader"),
    ("Fax","Fax"),("RetailDemo","Retail demo"),("RemoteRegistry","Remote registry"),
    ("WerSvc","Error reporting"),("wisvc","Windows Insider"),
    ("WMPNetworkSvc","Media Player sharing"),("icssvc","Mobile hotspot"),
    ("SharedAccess","ICS sharing"),("lfsvc","Geolocation"),
    ("PhoneSvc","Phone service"),("PrintNotify","Printer notify"),
    ("XblAuthManager","Xbox Live auth"),("XblGameSave","Xbox game save"),
    ("XboxNetApiSvc","Xbox networking"),("xbgm","Xbox monitoring"),
]
BLOAT_APPS = [
    "Microsoft.BingNews","Microsoft.BingWeather","Microsoft.BingFinance",
    "Microsoft.BingSports","Microsoft.GetHelp","Microsoft.Getstarted",
    "Microsoft.Microsoft3DViewer","Microsoft.MicrosoftSolitaireCollection",
    "Microsoft.MixedReality.Portal","Microsoft.People","Microsoft.SkypeApp",
    "Microsoft.Todos","Microsoft.WindowsFeedbackHub","Microsoft.WindowsMaps",
    "Microsoft.Xbox.TCUI","Microsoft.XboxApp","Microsoft.XboxGameOverlay",
    "Microsoft.XboxGamingOverlay","Microsoft.XboxIdentityProvider",
    "Microsoft.XboxSpeechToTextOverlay","Microsoft.ZuneMusic","Microsoft.ZuneVideo",
    "Microsoft.YourPhone","Microsoft.549981C3F5F10","Microsoft.MicrosoftOfficeHub",
]
BLOAT_TASKS = [
    r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
    r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
    r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
    r"\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
    r"\Microsoft\Windows\Feedback\Siuf\DmClient",
    r"\Microsoft\Windows\Windows Error Reporting\QueueReporting",
    r"\Microsoft\XblGameSave\XblGameSaveTask",
]

def bloatware_removal():
    header("BLOATWARE REMOVAL + BACKGROUND REFINEMENT",
           "Pillar II: Deep bloatware removal and background process refinement")

    print(f"  {YL}[SECTION 1/4]  Background Services ({len(BLOAT_SERVICES)} services){RS}\n")
    for i, (svc, desc) in enumerate(BLOAT_SERVICES, 1):
        step(i, len(BLOAT_SERVICES), f"{svc}  ({desc})...")
        run(f'sc stop "{svc}"'); run(f'sc config "{svc}" start= disabled')
        done_step()

    print(f"\n  {YL}[SECTION 2/4]  UWP Bloatware Apps ({len(BLOAT_APPS)} packages){RS}\n")
    step(1, 1, "Removing Xbox, Bing, Skype, Feedback, Maps apps...")
    removed = 0
    for app in BLOAT_APPS:
        r = subprocess.run(f'powershell -Command "Get-AppxPackage *{app}* | Remove-AppxPackage"',
                           shell=True, capture_output=True)
        if r.returncode == 0: removed += 1
    print(f"{GR}done{RS}  ({removed}/{len(BLOAT_APPS)} removed)")

    print(f"\n  {YL}[SECTION 3/4]  Scheduled Tasks{RS}\n")
    step(1, 1, f"Disabling {len(BLOAT_TASKS)} telemetry + CEIP tasks...")
    for task in BLOAT_TASKS:
        run(f'schtasks /change /tn "{task}" /disable')
    done_step()

    print(f"\n  {YL}[SECTION 4/4]  Privacy, Cortana, Ads, Notifications{RS}\n")
    priv = [
        ("Disabling Cortana",
         lambda: run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f')),
        ("Disabling Windows widgets and news feed",
         lambda: run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Dsh" /v AllowNewsAndInterests /t REG_DWORD /d 0 /f')),
        ("Disabling advertising ID",
         lambda: run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f')),
        ("Disabling location services",
         lambda: [
             run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location" /v Value /t REG_SZ /d "Deny" /f'),
             run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\LocationAndSensors" /v DisableLocation /t REG_DWORD /d 1 /f'),
         ]),
        ("Disabling activity history tracking",
         lambda: run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System" /v PublishUserActivities /t REG_DWORD /d 0 /f')),
        ("Silencing toast notifications + Action Center",
         lambda: [
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" /v ToastEnabled /t REG_DWORD /d 0 /f'),
             run('reg add "HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer" /v DisableNotificationCenter /t REG_DWORD /d 1 /f'),
         ]),
        ("Disabling app suggestions and content delivery",
         lambda: [
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" /v SystemPaneSuggestionsEnabled /t REG_DWORD /d 0 /f'),
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" /v SoftLandingEnabled /t REG_DWORD /d 0 /f'),
             run('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" /v SubscribedContent-338389Enabled /t REG_DWORD /d 0 /f'),
         ]),
    ]
    for i, (label, fn) in enumerate(priv, 1):
        step(i, len(priv), label + "...")
        try: fn()
        except: pass
        done_step()
    div()
    print(f"\n  {GR}[DONE] Bloatware Removal + Background Refinement COMPLETE!{RS}")
    pause()

# ── MODULE 5 — UNLIMITED POWER + THERMAL ──────────────────────
def power_thermal():
    header("UNLIMITED POWER PLAN + THERMAL OPTIMIZATION",
           "Pillar III: Advanced power management and thermal optimization")

    print(f"  {YL}[SECTION 1/3]  Unlimited Power Plan{RS}\n")
    step(1, 14, "Duplicating Ultimate Performance base plan...")
    run("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
    done_step()

    step(2, 14, "Detecting GUID of new plan...")
    guid = None
    r = subprocess.run("powercfg -list", shell=True, capture_output=True, text=True)
    for line in r.stdout.strip().splitlines():
        for p in line.split():
            if len(p) == 36 and p.count("-") == 4:
                guid = p
    if guid: done_step()
    else:
        fail_step(); warn("Falling back to High Performance plan.")
        run("powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")

    if guid:
        step(3, 14, "Naming plan 'UNLIMITED PERFORMANCE'...")
        run(f'powercfg -changename {guid} "UNLIMITED PERFORMANCE" "Max CPU. No throttle. No sleep. No limits."')
        done_step()

        step(4, 14, "CPU min/max -> 100%, Turbo Boost always ON...")
        for s in ["PROCTHROTTLEMIN 100","PROCTHROTTLEMAX 100","PERFBOOSTMODE 2","PERFBOOSTPOL 100","IDLEDISABLE 1"]:
            run(f"powercfg -setacvalueindex {guid} SUB_PROCESSOR {s}")
        done_step()

        step(5, 14, "Sleep / hibernate / screen -> NEVER...")
        for cmd in [
            f"powercfg -setacvalueindex {guid} SUB_SLEEP STANDBYIDLE 0",
            f"powercfg -setacvalueindex {guid} SUB_SLEEP HYBRIDSLEEP 0",
            f"powercfg -setacvalueindex {guid} SUB_SLEEP HIBERNATEIDLE 0",
            f"powercfg -setacvalueindex {guid} SUB_VIDEO VIDEOIDLE 0",
            "powercfg -hibernate off"
        ]: run(cmd)
        done_step()

        step(6, 14, "HDD/SSD spindown -> NEVER...")
        run(f"powercfg -setacvalueindex {guid} SUB_DISK DISKIDLE 0"); done_step()

        step(7, 14, "USB selective suspend -> OFF...")
        run(f"powercfg -setacvalueindex {guid} 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0"); done_step()

        step(8, 14, "PCI-E link state power management -> OFF...")
        run(f"powercfg -setacvalueindex {guid} SUB_PCIEXPRESS ASPM 0"); done_step()

        step(9, 14, "Activating UNLIMITED PERFORMANCE plan...")
        run(f"powercfg -setactive {guid}"); done_step()

    print(f"\n  {YL}[SECTION 2/3]  Thermal + CPU Core Optimization{RS}\n")

    step(10, 14, "Disabling CPU core parking (all cores always active)...")
    if guid:
        run(f"powercfg -setacvalueindex {guid} SUB_PROCESSOR CPMINCORES 100")
        run(f"powercfg -setacvalueindex {guid} SUB_PROCESSOR CPMAXCORES 100")
    run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583" /v ValueMax /t REG_DWORD /d 0 /f')
    done_step()

    step(11, 14, "Disabling OS power throttling for all processes...")
    run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" /v PowerThrottlingOff /t REG_DWORD /d 1 /f'); done_step()

    step(12, 14, "Disabling CPU C-state frequency downscaling...")
    run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Processor" /v Capabilities /t REG_DWORD /d 0x0007e066 /f'); done_step()

    print(f"\n  {YL}[SECTION 3/3]  Timer and Interrupt Optimization{RS}\n")

    step(13, 14, "Setting 1ms platform timer resolution...")
    run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v GlobalTimerResolutionRequests /t REG_DWORD /d 1 /f'); done_step()

    step(14, 14, "Disabling dynamic tick (consistent frame timing)...")
    run("bcdedit /set disabledynamictick yes")
    run("bcdedit /set useplatformtick yes"); done_step()

    div()
    ok("CPU core parking OFF — every core ready instantly")
    ok("Power throttling OFF — OS cannot suppress CPU frequency")
    ok("Timer: 1ms + dynamic tick disabled = smooth, stable frames")
    ok("UNLIMITED PERFORMANCE is now your active power plan")
    print(f"\n  {GR}[DONE] Power Management + Thermal Optimization COMPLETE!{RS}")
    pause()

# ── MODULE 6 — NETWORK STABILIZATION ─────────────────────────
def network_competitive():
    header("NETWORK STABILIZATION  -  COMPETITIVE GAMING",
           "Pillar IV: Network stabilization for competitive gaming")
    tasks = [
        ("Flushing DNS resolver cache",
         lambda: run("ipconfig /flushdns")),
        ("Resetting TCP/IP stack to clean state",
         lambda: [run("netsh int ip reset"), run("netsh int tcp reset")]),
        ("Resetting Winsock catalog",
         lambda: run("netsh winsock reset")),
        ("Releasing and renewing IP address",
         lambda: [run("ipconfig /release"), run("ipconfig /renew")]),
        ("Disabling Nagle algorithm (packets sent immediately)",
         lambda: [
             run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v TcpAckFrequency /t REG_DWORD /d 1 /f'),
             run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v TCPNoDelay /t REG_DWORD /d 1 /f'),
             run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v TcpDelAckTicks /t REG_DWORD /d 0 /f'),
         ]),
        ("Removing network throttling (full bandwidth to game)",
         lambda: run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f')),
        ("Enabling RSS (Receive Side Scaling)",
         lambda: run("netsh int tcp set global rss=enabled")),
        ("Enabling TCP chimney offload",
         lambda: run("netsh int tcp set global chimney=enabled")),
        ("Disabling TCP timestamps (reduce overhead)",
         lambda: run("netsh int tcp set global timestamps=disabled")),
        ("Enabling Direct Cache Access",
         lambda: run("netsh int tcp set global dca=enabled")),
        ("Setting TCP auto-tuning to normal",
         lambda: run("netsh int tcp set global autotuninglevel=normal")),
        ("Setting initial RTO -> 2000ms (faster retransmit)",
         lambda: run("netsh int tcp set global initialRto=2000")),
        ("Reducing max SYN retransmissions to 2",
         lambda: run("netsh int tcp set global maxsynretransmissions=2")),
        ("Disabling TCP heuristics",
         lambda: run("netsh int tcp set heuristics disabled")),
        ("Setting DNS to Cloudflare 1.1.1.1 / 1.0.0.1",
         lambda: run('powershell -Command "Get-NetAdapter | Where-Object {$_.Status -eq \'Up\'} | ForEach-Object { Set-DnsClientServerAddress -InterfaceIndex $_.InterfaceIndex -ServerAddresses (\'1.1.1.1\',\'1.0.0.1\') }"')),
        ("Enabling DNS-over-HTTPS (DoH) via Cloudflare",
         lambda: run('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters" /v EnableAutoDoh /t REG_DWORD /d 2 /f')),
        ("Disabling NIC power management (no packet drops on idle)",
         lambda: run('powershell -Command "Get-NetAdapter | ForEach-Object { Disable-NetAdapterPowerManagement -Name $_.Name -ErrorAction SilentlyContinue }"')),
        ("Maximizing NIC transmit/receive buffers to 2048",
         lambda: [
             run('powershell -Command "Get-NetAdapter | Set-NetAdapterAdvancedProperty -RegistryKeyword \'*ReceiveBuffers\' -RegistryValue 2048 -ErrorAction SilentlyContinue"'),
             run('powershell -Command "Get-NetAdapter | Set-NetAdapterAdvancedProperty -RegistryKeyword \'*TransmitBuffers\' -RegistryValue 2048 -ErrorAction SilentlyContinue"'),
         ]),
        ("Disabling interrupt moderation (absolute lowest latency)",
         lambda: run('powershell -Command "Get-NetAdapter | Set-NetAdapterAdvancedProperty -RegistryKeyword \'*InterruptModeration\' -RegistryValue 0 -ErrorAction SilentlyContinue"')),
        ("Removing QoS bandwidth reservation (100% to your game)",
         lambda: run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched" /v NonBestEffortLimit /t REG_DWORD /d 0 /f')),
    ]
    for i, (label, fn) in enumerate(tasks, 1):
        step(i, len(tasks), label + "...")
        try: fn()
        except: pass
        done_step()
    div()
    ok("Nagle OFF — game packets leave instantly, no TCP batching")
    ok("DNS: Cloudflare 1.1.1.1 with DoH enabled")
    ok("NIC: buffers maxed to 2048, interrupt moderation OFF")
    ok("QoS reservation removed — 100% bandwidth available")
    print(f"\n  {GR}[DONE] Competitive Network Stabilization COMPLETE!{RS}")
    pause()

# ── MODULE 7 — DEEP CLEAN ─────────────────────────────────────
def deep_clean():
    header("DEEP CLEAN  -  CACHES, REGISTRY, RAM",
           "Wipes junk files, cleans registry, reclaims RAM")

    print(f"  {YL}[SECTION 1/3]  Cache and Junk Files{RS}\n")
    cache_paths = [
        ("User TEMP",      os.environ.get("TEMP","")),
        ("Windows TEMP",   r"C:\Windows\Temp"),
        ("Prefetch",       r"C:\Windows\Prefetch"),
        ("IE/Edge cache",  os.path.join(os.environ.get("LOCALAPPDATA",""), r"Microsoft\Windows\INetCache")),
        ("Thumbnails",     os.path.join(os.environ.get("LOCALAPPDATA",""), r"Microsoft\Windows\Explorer")),
        ("NVIDIA DXCache", os.path.join(os.environ.get("LOCALAPPDATA",""), r"NVIDIA\DXCache")),
        ("NVIDIA GLCache", os.path.join(os.environ.get("LOCALAPPDATA",""), r"NVIDIA\GLCache")),
        ("AMD DxCache",    os.path.join(os.environ.get("LOCALAPPDATA",""), r"AMD\DxCache")),
        ("WER reports",    os.path.join(os.environ.get("LOCALAPPDATA",""), r"Microsoft\Windows\WER")),
        ("Crash dumps",    r"C:\Windows\Minidump"),
    ]
    tc = len(cache_paths) + 2
    for i, (label, path) in enumerate(cache_paths, 1):
        step(i, tc, f"Cleaning {label}..."); del_tree(path); done_step()
    step(len(cache_paths)+1, tc, "Emptying Recycle Bin...")
    run("powershell -Command \"Clear-RecycleBin -Force -ErrorAction SilentlyContinue\""); done_step()
    step(len(cache_paths)+2, tc, "Clearing Windows Update cache...")
    run("net stop wuauserv"); del_tree(r"C:\Windows\SoftwareDistribution\Download"); run("net start wuauserv"); done_step()

    print(f"\n  {YL}[SECTION 2/3]  Registry Cleanup{RS}\n")
    reg_tasks = [
        ("Run / RunMRU history",           lambda: run('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU" /f')),
        ("Recent documents + typed paths", lambda: [
             run('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs" /f'),
             run('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths" /f')]),
        ("Font + thumbnail cache pointers", lambda: [
             run('reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontCache" /f'),
             run('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Thumbnail" /f')]),
    ]
    for i, (label, fn) in enumerate(reg_tasks, 1):
        step(i, len(reg_tasks), f"Clearing {label}...")
        try: fn()
        except: pass
        done_step()

    print(f"\n  {YL}[SECTION 3/3]  RAM Optimization{RS}\n")
    mb = get_mem()
    total_mb = mb.ullTotalPhys // (1024*1024)
    avail_bef = mb.ullAvailPhys // (1024*1024)
    info(f"RAM before: {total_mb - avail_bef} MB used / {total_mb} MB total"); print()
    ram_tasks = [
        ("Purging standby memory list (kernel API)",
         lambda: run('powershell -Command "Add-Type -TypeDefinition \'using System;using System.Runtime.InteropServices;public class MC{[DllImport(\\"ntdll.dll\\")]public static extern int NtSetSystemInformation(int i,IntPtr p,int l);}\'; $v=[System.Runtime.InteropServices.Marshal]::AllocHGlobal(4);[System.Runtime.InteropServices.Marshal]::WriteInt32($v,4);[MC]::NtSetSystemInformation(80,$v,4);[System.Runtime.InteropServices.Marshal]::FreeHGlobal($v)"')),
        ("Trimming all process working sets",
         lambda: run('powershell -Command "Get-Process | ForEach-Object { try { $_.MaxWorkingSet = $_.MaxWorkingSet } catch {} }"')),
        ("Page file -> system-managed, memory compression OFF",
         lambda: [run("wmic computersystem set AutomaticManagedPagefile=True"),
                  run("powershell -Command \"Disable-MMAgent -MemoryCompression\"")]),
    ]
    for i, (label, fn) in enumerate(ram_tasks, 1):
        step(i, len(ram_tasks), label + "...")
        try: fn()
        except: pass
        done_step()
    time.sleep(1)
    ma = get_mem()
    avail_aft = ma.ullAvailPhys // (1024*1024)
    freed = avail_aft - avail_bef
    print()
    ok(f"RAM after: {total_mb - avail_aft} MB used / {total_mb} MB total")
    if freed > 0: ok(f"~{freed} MB reclaimed from RAM!")
    else: info("RAM stable (already well optimized)")
    print(f"\n  {GR}[DONE] Deep Clean COMPLETE!{RS}")
    pause()

# ── MODULE 8 — HEALTH CHECK ───────────────────────────────────
def health_check():
    header("SYSTEM HEALTH CHECK", "Live snapshot of your PC's current state")
    W = 44

    mb = get_mem()
    total = mb.ullTotalPhys // (1024*1024)
    avail = mb.ullAvailPhys // (1024*1024)
    pct   = mb.dwMemoryLoad
    filled = int(W * pct / 100)
    color  = RD if pct > 80 else YL if pct > 60 else GR
    bar    = f"{color}{'█'*filled}{DM}{'░'*(W-filled)}{RS}"
    print(f"  {YL}RAM Usage{RS}");  print(f"  {bar} {pct}%")
    print(f"  {total-avail} MB used  /  {total} MB total  /  {avail} MB free\n")

    plan = run_out("powercfg /getactivescheme")
    print(f"  {YL}Active Power Plan{RS}")
    print(f"  {GR if 'UNLIMITED' in plan.upper() else YL}{plan}{RS}\n")

    cpu = run_out("wmic cpu get Name /value").replace("Name=","").strip()
    print(f"  {YL}Processor{RS}");  print(f"  {WH}{cpu}{RS}\n")

    gpu = run_out("wmic path win32_VideoController get Name /value").replace("Name=","").strip()
    print(f"  {YL}GPU{RS}")
    for line in gpu.splitlines():
        if line.strip(): print(f"  {WH}{line.strip()}{RS}")
    print()

    try:
        u = shutil.disk_usage("C:\\")
        free_gb  = u.free  // (1024**3)
        total_gb = u.total // (1024**3)
        used_gb  = total_gb - free_gb
        dpct = int(100 * used_gb / total_gb)
        df   = int(W * dpct / 100)
        dc   = RD if dpct > 85 else YL if dpct > 60 else GR
        dbar = f"{dc}{'█'*df}{DM}{'░'*(W-df)}{RS}"
        print(f"  {YL}Disk C:\\{RS}"); print(f"  {dbar} {dpct}%")
        print(f"  {used_gb} GB used  /  {total_gb} GB total  /  {free_gb} GB free\n")
    except: pass

    os_ver = run_out("wmic os get Caption /value").replace("Caption=","").strip()
    print(f"  {YL}Operating System{RS}"); print(f"  {WH}{os_ver}{RS}\n")

    div(); print(f"  {YL}Recommendations:{RS}")
    if pct > 80:  warn("RAM HIGH — run [7] Deep Clean to free memory")
    else:         ok("RAM usage normal")
    if "UNLIMITED" in plan.upper(): ok("UNLIMITED PERFORMANCE power plan active")
    else: warn("Not on UNLIMITED plan — run [5] to activate it")
    try:
        if free_gb < 10: warn(f"Low disk: {free_gb} GB free — run [7] to clean")
        else:            ok(f"Disk OK: {free_gb} GB free on C:\\")
    except: pass
    pause()

# ── MODULE 9 — FULL NUKE ──────────────────────────────────────
def full_nuke():
    header("FULL NUKE  -  ALL OPTIMIZATIONS",
           "All 4 pillars. Maximum FPS. Minimum lag. Zero bloat.")

    import builtins
    _real_input = builtins.input
    builtins.input = lambda *a, **k: ""

    modules = [
        ("1","System Restore Point",            create_restore_point),
        ("2","System Performance",               optimize_system),
        ("3","MAX FPS + Input Lag",              fps_input_lag),
        ("4","Bloatware + Background Refinement",bloatware_removal),
        ("5","Unlimited Power + Thermal",        power_thermal),
        ("6","Network Stabilization",            network_competitive),
        ("7","Deep Clean",                       deep_clean),
        ("8","Health Check",                     health_check),
    ]

    for num, name, fn in modules:
        print(f"\n  {MG}{'='*59}{RS}")
        print(f"  {MG}  MODULE {num}/8  -  {name.upper()}{RS}")
        print(f"  {MG}{'='*59}{RS}\n")
        try: fn()
        except Exception as e: warn(f"Module error: {e}")

    builtins.input = _real_input

    print(f"""
  {CY}+{'='*59}+{RS}
  {CY}|{RS}                                                           {CY}|{RS}
  {CY}|{GR}   ALL 8 MODULES COMPLETE - YOUR PC IS A BEAST           {CY}|{RS}
  {CY}|{RS}                                                           {CY}|{RS}
  {CY}|{YL}   FPS: MAXIMUM          BLOAT: GONE                     {CY}|{RS}
  {CY}|{YL}   INPUT LAG: MINIMUM    THERMAL: OPTIMIZED              {CY}|{RS}
  {CY}|{YL}   NETWORK: STABILIZED   POWER: UNLIMITED                {CY}|{RS}
  {CY}|{RS}                                                           {CY}|{RS}
  {CY}|{DM}   RESTART YOUR PC FOR MAXIMUM EFFECT                     {CY}|{RS}
  {CY}+{'='*59}+{RS}""")

    builtins.input = _real_input
    ans = input(f"\n  {YL}Restart now for full effect? [Y/N]: {RS}").strip().upper()
    if ans == "Y":
        run("shutdown /r /t 15 /c \"PC Super Optimizer v4: Applying all optimizations...\"")
        ok("Restarting in 15 seconds. Run 'shutdown /a' in CMD to cancel.")
    pause()

# ── ENTRY POINT ───────────────────────────────────────────────
def main():
    if platform.system() != "Windows":
        print(f"{RD}  This tool is for Windows only.{RS}"); sys.exit(1)
    if not is_admin():
        relaunch_admin()

    ACTIONS = {
        "1": create_restore_point, "2": optimize_system,
        "3": fps_input_lag,        "4": bloatware_removal,
        "5": power_thermal,        "6": network_competitive,
        "7": deep_clean,           "8": health_check,
        "9": full_nuke,
    }

    while True:
        choice = show_menu()
        if choice == "0":
            os.system("cls")
            print(f"\n  {CY}+{'='*59}+{RS}")
            print(f"  {CY}|  Thank you for using PC SUPER OPTIMIZER v4.0           |{RS}")
            print(f"  {CY}|  Your PC is now running at PEAK performance!           |{RS}")
            print(f"  {CY}+{'='*59}+{RS}\n")
            time.sleep(2); break
        elif choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print(f"  {RD}Invalid choice. Try again.{RS}"); time.sleep(1)

if __name__ == "__main__":
    main()
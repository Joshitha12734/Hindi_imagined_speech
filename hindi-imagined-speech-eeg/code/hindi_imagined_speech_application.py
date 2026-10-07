"""
Hindi Imagined-Speech Experiment - Stage 1-4 prototype (PsychoPy)
Run:  python hindi_imagined_speech_app.py
Needs: pip install psychopy
Keys: SPACE = continue, ESC = abort (data saved so far is kept).

NOTE: send_marker() is a STUB. No EEG hardware is connected yet.
      Real markers (BrainFlow / LSL / digital trigger) go inside that function.
"""
import csv
import os
import random
from datetime import datetime

from psychopy import core, event, gui, visual

PHRASES = [
    ("H001", "हाँ"),
    ("H002", "नहीं"),
    ("H003", "मदद"),
]
REPS_PER_PHRASE = 2          # use 2 for demo; many more for real data
T_FIXATION, T_CUE, T_IMAGINE, T_REST = 1.5, 2.0, 4.0, 3.0   # seconds
CONDITION = "imagined_speech"
FONT = ["Nirmala UI", "Noto Sans Devanagari", "Mangal", "Lohit Devanagari", "Arial"]
FULLSCR = False              # set True for real sessions

# Marker codes (event IDs). Imagery onset code = 100 + phrase number.
MK = {"fixation": 10, "cue": 20, "imagine_end": 30, "rest": 40,
      "session_start": 1, "session_end": 2}


def send_marker(code, label):
    """STUB. Replace body with e.g. BrainFlow board.insert_marker(code)
    or an LSL outlet.push_sample([code]). Returns the timestamp used."""
    t = clock.getTime()
    print(f"[MARKER] code={code} label={label} t={t:.4f}")
    return t


# ------------------------- SESSION SETUP ------------------------------
info = {"participant_id": "P001", "session": "S01"}
if not gui.DlgFromDict(info, title="Hindi Imagined Speech").OK:
    core.quit()

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("metadata", exist_ok=True)
base = f"metadata/{info['participant_id']}_{info['session']}_{stamp}"
trial_file, event_file = base + "_trials.csv", base + "_events.csv"

TRIAL_COLS = ["participant_id", "session", "trial_number", "phrase_id", "phrase",
              "condition", "imagine_marker_id", "trial_start_s", "imagine_onset_s",
              "imagine_offset_s", "trial_end_s", "trial_start_wallclock",
              "qc_status", "device_info", "sampling_rate_hz", "notes"]
EVENT_COLS = ["participant_id", "session", "trial_number", "marker_id",
              "event_label", "time_s", "wallclock"]

clock = core.Clock()  # experiment-relative time (s); store same timebase as markers
win = visual.Window(size=(1000, 700), fullscr=FULLSCR, color="black", units="height")
text = visual.TextStim(win, text="", font=FONT, color="white", height=0.06, wrapWidth=1.4)


def show(msg, height=0.06, wait_key=False, secs=None):
    text.text, text.height = msg, height
    text.draw()
    win.flip()
    if wait_key:
        keys = event.waitKeys(keyList=["space", "escape"])
        if "escape" in keys:
            raise KeyboardInterrupt
    elif secs:
        t0 = clock.getTime()
        while clock.getTime() - t0 < secs:
            if event.getKeys(["escape"]):
                raise KeyboardInterrupt
            core.wait(0.01)


def main():
    trials = PHRASES * REPS_PER_PHRASE
    random.shuffle(trials)

    with open(trial_file, "w", newline="", encoding="utf-8-sig") as tf, \
         open(event_file, "w", newline="", encoding="utf-8-sig") as ef:
        tw, ew = csv.writer(tf), csv.writer(ef)
        tw.writerow(TRIAL_COLS)
        ew.writerow(EVENT_COLS)

        def log_event(n, code, label):
            t = send_marker(code, label)
            ew.writerow([info["participant_id"], info["session"], n, code, label,
                         f"{t:.4f}", datetime.now().isoformat(timespec="milliseconds")])
            ef.flush()
            return t

        log_event(0, MK["session_start"], "session_start")
        print("DEBUG: About to show instruction screen")

        text.text = "INSTRUCTIONS\n\n" \
                    "Read the Hindi word.\n" \
                    "When you see ●, imagine saying it silently.\n\n" \
                    "Do not move your lips, tongue, or head.\n\n" \
                    "Press SPACE to start."

        text.height = 0.045
        text.color = "white"
        text.draw()
        win.flip()

        print("DEBUG: Instruction screen displayed")

        keys = event.waitKeys(keyList=["space", "escape"])

        if "escape" in keys:
            raise KeyboardInterrupt

        print("DEBUG: SPACE received")

        for n, (pid, phrase) in enumerate(trials, start=1):
            imagine_code = 100 + int(pid[1:])
            wall = datetime.now().isoformat(timespec="milliseconds")

            t_start = log_event(n, MK["fixation"], "fixation")
            show("+", 0.12, secs=T_FIXATION)

            log_event(n, MK["cue"], "phrase_cue")
            show(phrase, 0.10, secs=T_CUE)

            t_on = log_event(n, imagine_code, f"imagine_onset_{pid}")
            show("●", 0.12, secs=T_IMAGINE)           # phrase hidden during imagery
            t_off = log_event(n, MK["imagine_end"], "imagine_end")

            log_event(n, MK["rest"], "rest")
            show("आराम करें (Rest)", 0.06, secs=T_REST)
            t_end = clock.getTime()

            tw.writerow([info["participant_id"], info["session"], n, pid, phrase,
                         CONDITION, imagine_code, f"{t_start:.4f}", f"{t_on:.4f}",
                         f"{t_off:.4f}", f"{t_end:.4f}", wall,
                         "pending", "NO_EEG_CONNECTED (demo)", "n/a", ""])
            tf.flush()                                  # crash-safe: save each trial

        log_event(0, MK["session_end"], "session_end")
        show("धन्यवाद! / Thank you. Session complete.", 0.05, secs=2)


try:
    main()
except KeyboardInterrupt:
    print("Aborted by experimenter. Partial data saved.")
finally:
    win.close()
    print(f"Saved:\n  {trial_file}\n  {event_file}")
    core.quit()

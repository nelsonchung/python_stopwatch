import time
import threading

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.display_thread = threading.Thread(target=self._update_display)
            self.display_thread.start()
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.running:
            self.running = False
            self.display_thread.join()
        else:
            print("Stopwatch is not running.")

    def elapsed_time(self):
        if self.start_time is None:
            return "00:00:00.000"
        elapsed = time.time() - self.start_time
        millis = int((elapsed - int(elapsed)) * 1000)
        seconds = int(elapsed) % 60
        minutes = (int(elapsed) // 60) % 60
        hours = (int(elapsed) // 3600) % 24
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"

    def _update_display(self):
        while self.running:
            print(f"\rElapsed time: {self.elapsed_time()}", end="")
            time.sleep(0.001)  # Update every 1 millisecond

stopwatch = Stopwatch()

# 開始計時
stopwatch.start()

# 等待按下Enter鍵
input("\nPress Enter to stop the stopwatch...\n")

# 停止計時
stopwatch.stop()

# 顯示最終的經過時間
print("\nFinal elapsed time:", stopwatch.elapsed_time())


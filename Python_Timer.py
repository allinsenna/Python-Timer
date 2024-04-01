import threading
import time

class Timer:
  def __init__(self, duration):
    self.duration = duration
    self.remaining_time = 0
    self.timer_thread = threading.Thread(target=self.run_timer)
    self.timer_thread.daemon = True

  def run_timer(self):
    while self.remaining_time > 0:
      self.remaining_time -= 1
      time.sleep(1)

  def start(self):
    if not self.timer_thread.is_alive():
      self.remaining_time = self.duration
      self.timer_thread = threading.Thread(target=self.run_timer)
      self.timer_thread.daemon = True
      self.timer_thread.start()

def main():
  
  timer_task = Timer(15)

  def task1(timer_task):
    print("Performing task1")
    print("task 1completed.")
    timer_task.start() #timer starting after task1 has been completed

  def task2():
    print("Performing task2")
    print("task2 completed")
    
  while True:
    print("1. Perform task1")
    print("2. Perform task2")

    choice = input().strip().lower()

    if choice == "2":
      task2()

    elif choice == "1":
      if timer_task.remaining_time == 0: #if timer is 0 it lets the user do task1 again
        task1(timer_task)
      else: #else it will tell the remaining time (if not done)
        print("task1 can only be done once every 15 sec")
        print("Time left:", timer_task.remaining_time, "seconds")

#timer 2 can be done anytime as no timer was implemented into it while task1 timer runs in background ----
if __name__ == "__main__":
  main()

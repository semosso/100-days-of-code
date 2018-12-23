# tentando criar algo que editaria automaticamente meu log do 100-days-of-code
import datetime # importing module to manipulate date and time
import subprocess # importing module to call new processes, needed to use GIT

log_main = "log.md"

pago = input("Did I code at all today? (Y/N)\n> ").lower()

if pago == "y":
    print("Keep that streak going! What was the progress?")
    daily_progress = input("> ")
    print("Any thoughts on the work you did today or plan on doing tomorrow?")
    daily_thoughts = input("> ")
    print("And what projects did you work on?")
    daily_project = input("> ")
    
    today_date = datetime.date.today().strftime(f"%B %d, %Y, %A")

    open(log_main, "a+").write(f"""\n\n
**{today_date}**\n\n
**Progress**: {daily_progress}\n\n
**Thoughts**:{daily_thoughts}\n\n
**Project**:{daily_project}""") # this looks wrong because it seems I'm breaking indent, but I'm not if its within the string

    print("Do you want to push this log change to Github? (Y/N)")
    push = input("> ").lower()

    if push == "y":
        print("What should the commit message be?")
        commit_message = input("> ")

        subprocess.call(["git", "add", f"{log_main}"]) # note that each command/parameter/argument whatever is withing its own set of quotes
        subprocess.call(["git", "commit", "-m", f"{commit_message}"])
        subprocess.call(["git", "push"])
    else:
        print("Ok, just don't forget to do it later.")

elif pago == "n":
    print("That's a shame, do your best not to miss it tomorrow though!")

    open(log_main, "a+").write(f"\n\n**{today_date}***\nNothing today.")
    # no need to close anything because log_main is a string that tells Python where file is, not a file OBJECT

else:
    print("Try again, bozo.")
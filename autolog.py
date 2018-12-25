# tentando criar algo que editaria automaticamente meu log do 100-days-of-code
import datetime # importing module to manipulate date and time
import subprocess # importing module to call new processes, needed to use GIT

log_main = "log.md"
today_date = datetime.date.today().strftime(f"%B %d, %Y, %A")
which_day =  datetime.date.today() - datetime.date(2018, 12, 19) # looks dirty, there's gotta be a better way

def YN_input(question): # sugestão do Takai; simplifica bastante todos os loops
    answer = '' # ingenious, sempre vejo acho ingenious, preciso começar a pensar nisso
    while answer.lower() not in ('y', 's', 'n'): # i.e., enquanto a resposta não for y/s ou n, continuar rodando
        print(question)
        answer = input("> ").lower()
    return answer

def written_input(question):
    answer = ''
    print(question)
    answer = input("> ")
    return answer

pago = YN_input("Did I code at all today?")

if pago == ("y") or ("s"):
    daily_progress = written_input("Keep that streak going! What was the progress?")
    daily_thoughts = written_input("Any thoughts on the work you did today or plan on doing tomorrow?")
    daily_project = YN_input("Did you work on any specific projects?")
    
    if daily_project == ("y", "s"):
        project_name = written_input("Cool! What's it called?")
        project_link = written_input("Did you push it to Github? If so, add the link now.")

        if project_link.startswith("http"):
            project_name = f"<a href={project_link}>{project_name}</a>" # trying to add link to project... let's see
    else:
        project_name = "No project."

    with open(log_main, "a+") as f:
        f.write(f"""\n
**Day {which_day.days}: {today_date}**\n
**Progress**: {daily_progress}\n
**Thoughts**: {daily_thoughts}\n
**Project**: {project_name}""") # this looks wrong because it seems I'm breaking indent, but I'm not if its within the string

    push = YN_input("Do you want to push this log change to Github?")

    if push == ("y") or ("s"):
        commit_message = written_input("What should the commit message be?")

        subprocess.call(["git", "add", f"{log_main}"]) # note that each command/parameter/argument whatever is withing its own set of quotes
        subprocess.call(["git", "commit", "-m", f"{commit_message}"])
        subprocess.call(["git", "push"])

elif pago == "n":
    print("That's a shame.")

    with open(log_main, "a+") as f:
        f.write(f"\n**Day {which_day.days}: {today_date}**\nNothing today.")
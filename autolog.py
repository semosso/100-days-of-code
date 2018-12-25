# tentando criar algo que editaria automaticamente meu log do 100-days-of-code
import datetime # importing module to manipulate date and time
import subprocess # importing module to call new processes, needed to use GIT

log_main = "log.md"
today_date = datetime.date.today().strftime(f"%B %d, %Y, %A")
which_day =  datetime.date.today() - datetime.date(2018, 12, 19) # looks dirty, there's gotta be a better way

def ask_input(question): # sugestão do Takai; simplifica bastante todos os loops
    answer = '' # ingenious, sempre vejo acho ingenious, preciso começar a pensar nisso
    while answer.lower() not in ('y', 's', 'n'): # i.e., enquanto a resposta não for y/s ou n, continuar rodando
        print(question)
        answer = input("\n> ").lower()
    return answer

pago = ask_input("Did I code at all today?")

if pago == ("y", "s"):
    daily_progress = input("Keep that streak going! What was the progress?\n> ")
    daily_thoughts = input("Any thoughts on the work you did today or plan on doing tomorrow?\n> ")
    daily_project = ask_input("Did you work on any specific projects?")
    
    if daily_project == ("y", "s"):
        project_name = input("Cool! What's it called?\n> ")
        project_link = input("Did you push it to Github? If so, add the link now.\n> ")

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

    push = ask_input("Do you want to push this log change to Github?")

    if push == ("y", "s"):
        print("What should the commit message be?")
        commit_message = input("\n> ")

        subprocess.call(["git", "add", f"{log_main}"]) # note that each command/parameter/argument whatever is withing its own set of quotes
        subprocess.call(["git", "commit", "-m", f"{commit_message}"])
        subprocess.call(["git", "push"])

elif pago == "n":
    print("That's a shame.")

    with open(log_main, "a+") as f:
        f.write(f"\n**Day {which_day.days}: {today_date}**\nNothing today.")

# sugestões Takai
# em "open(log_main, "a+").write(f"\n\n**{today_date}***\nNothing today.")", usa with quando voce aprender a usar
## ASK if what are the benefits of using the WITH statement (other than automatically closing; would I need to close in my case?)

# with open(log_main, 'a+') as f:
#     f.write('blabla')

# # esse loop de input -> resposta pode virar uma funcão

# def ask_input(question):
#     answer = ''
#     while answer.lower() not in ('y', 'n'):
#         print(question)
#         answer = input("> ").lower()
#     return answer
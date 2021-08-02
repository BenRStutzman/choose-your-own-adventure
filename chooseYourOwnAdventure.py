import time

interletter_delay = 0.03
interline_delay = 0.2

class Event:
    def __init__(self, id, plot, prompt, choices):
        self.id = id
        self.plot = plot
        self.prompt = prompt
        self.choices = choices

def get_choice(choices, invalid = False):
    if invalid:
        print()
        fancy_print("That's not one of the options; pick again.\n")
    choice = input("> ")
    try:
        return int(choice) - 1
    except ValueError:
        return get_choice(choices, invalid = True)

def fancy_print(string, end = '\n', delay_ending = False):
    for char in string[:-1]:
        sleep_time = interline_delay if char == '\n' else interletter_delay
        time.sleep(sleep_time)
        print(char, end='', flush = True)
    print(string[-1], end = '' if delay_ending else end, flush = True)
    if delay_ending:
        time.sleep(interline_delay)
        print('', end = end, flush = True)

f = open('PleaseIgnoreThis\story.txt')

raw_events = [section.split('\n\n') for section in f.read().strip().split('\n\n\n')]
events = {}

for raw_event in raw_events:
    id = raw_event[0]
    plot = raw_event[1].split('\n...\n')
    prompt = raw_event[2]
    if len(raw_event) == 4:
        choices = [choice.split(') ') for choice in raw_event[3].split('\n')]
    else:
        choices = None
    event = Event(id, plot, prompt, choices)
    events[event.id] = event

next_event_id = '0'
show_instructions = True

fancy_print('Press enter to begin.', end = '')
input()
print()

while True:
    event = events[next_event_id]
    for statement in event.plot:
        fancy_print(statement, end = '')
        input()
        print()
    if event.choices is None:
        if event.prompt in events:
            next_event_id = event.prompt
            continue
        else:
            fancy_print(event.prompt, end = '')
            break
    else:
        fancy_print(event.prompt, end = '\n\n', delay_ending = True)
    for index, (id, choice) in enumerate(event.choices):
        fancy_print(str(index + 1) + ') ' + choice, delay_ending = True)
    print('')
    choice = get_choice(event.choices)
    while choice not in range(len(event.choices)):
        choice = get_choice(event.choices, invalid = True)
    next_event_id = event.choices[choice][0]
    show_instructions = False
    print()

time.sleep(1)
